"""Funciones compartidas por los notebooks del proyecto Ternium MC4 → Skinpass.

Uso desde un notebook en notebooks/:
    import sys; sys.path.append('..')
    from src.ternium import *
"""
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
DATOS = RAIZ / "data"
FIGURAS = RAIZ / "figuras"

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Reglas de limpieza: fijadas antes de mirar resultados (Entrega 1).
CORONA_VALIDA_UM = (0, 300)
CORTES_ESPESOR_MM = [0, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 13, 30]

warnings.simplefilter("ignore", pd.errors.PerformanceWarning)

COLORES = {"azul": "#1f4e79", "naranja": "#e2470f", "gris": "#8a8f94", "rojo": "#c0504d"}


# ---------------------------------------------------------------- carga
# Leer los 36 Excel tarda ~40 s. La primera lectura guarda una copia en data/cache/<nombre>.parquet
# (se lee en ~1 s). La copia se invalida sola si cambian los Excel: se compara la lista de archivos
# con sus tamaños, que no cambia al clonar el repo (las fechas de modificación sí).
CACHE = DATOS / "cache"


def _archivos(carpeta: Path, patron: str) -> list:
    archivos = sorted(carpeta.glob(patron), key=lambda p: (MESES.index(p.stem.split()[1]), p.name))
    if not archivos:
        raise FileNotFoundError(f"No hay archivos {patron} en {carpeta}")
    return archivos


def _huella(archivos: list) -> str:
    return ";".join(f"{a.name}:{a.stat().st_size}" for a in archivos)


def _homogeneo(df: pd.DataFrame) -> pd.DataFrame:
    """Pasa a texto las columnas que mezclan texto y números (solo topSpyOnT, un código)."""
    for c in df.columns[df.dtypes == object]:
        if df[c].dropna().map(type).nunique() > 1:
            df[c] = df[c].map(lambda v: v if pd.isna(v) else str(v))
    return df


def _leer(carpeta: Path, patron: str, nombre: str, usar_cache: bool = True) -> pd.DataFrame:
    archivos = _archivos(carpeta, patron)
    cache, huella = CACHE / f"{nombre}.parquet", _huella(archivos)
    if usar_cache and cache.exists():
        import pyarrow.parquet as pq
        if pq.read_schema(cache).metadata.get(b"huella", b"").decode() == huella:
            return pd.read_parquet(cache)
    df = pd.concat(
        [pd.read_excel(a, engine="calamine").assign(Origen_Archivo=a.name) for a in archivos],
        ignore_index=True,
    )
    df = _homogeneo(df)
    try:
        import pyarrow as pa
        import pyarrow.parquet as pq
        tabla = pa.Table.from_pandas(df, preserve_index=False)
        tabla = tabla.replace_schema_metadata({**(tabla.schema.metadata or {}), b"huella": huella.encode()})
        CACHE.mkdir(exist_ok=True)
        pq.write_table(tabla, cache, compression="zstd")
    except Exception as e:   # sin pyarrow o sin permiso de escritura: se sigue sin caché
        warnings.warn(f"No se pudo guardar la caché {cache.name}: {e}")
    return df


def cargar_mc4(usar_cache: bool = True) -> pd.DataFrame:
    """24 archivos quincenales del Molino Caliente 4 (149,734 rollos, 2025)."""
    return _leer(DATOS / "mc4", "MC4_PSQ*.xlsx", "mc4", usar_cache)


def cargar_skp(usar_cache: bool = True) -> pd.DataFrame:
    """12 archivos mensuales del Skinpass (58,786 piezas, 2025)."""
    return _leer(DATOS / "skp", "SKP_PSQ*.xlsx", "skp", usar_cache)


# ---------------------------------------------------------------- reglas
def aplicar_reglas(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega las columnas derivadas que usan todos los análisis.

    SKP       : la Ruta Teórica incluye el Skinpass (intención, no recorrido confirmado).
    corC      : Corona Salida depurada; fuera de 0-300 µm pasa a faltante (no se borran filas).
    Mes       : mes real de laminación.
    RangoEsp  : rango de Espesor Objetivo.
    Producto  : Norma | Grado | RangoEsp.
    """
    lo, hi = CORONA_VALIDA_UM
    nuevas = pd.DataFrame({
        "SKP": df["Ruta Teórica"].astype("string").str.contains("SKP_PSQ", na=False),
        "corC": df["Corona Salida"].where(df["Corona Salida"].between(lo, hi)),
        "Mes": df["Fecha Inicio"].dt.month,
        "RangoEsp": pd.cut(df["Espesor Objetivo"], CORTES_ESPESOR_MM).astype(str),
    }, index=df.index)
    nuevas["Producto"] = df["Norma"].astype(str) + " | " + df["Grado"].astype(str) + " | " + nuevas["RangoEsp"]
    return pd.concat([df, nuevas], axis=1)


def defectos_largo(df: pd.DataFrame) -> pd.DataFrame:
    """Un renglón por defecto registrado (los 5 bloques Defecto (k) apilados).

    Columnas: d (defecto), a (1 = registro automático), r (dictamen del defecto),
    obs (texto del sistema), ret (True si RETENIDO), row (índice del rollo).
    """
    partes = []
    for k in range(1, 6):
        t = df[[f"Defecto ({k})", f"Registro Automatico ({k})", f"Dictamen ({k})", f"Observaciones ({k})"]].copy()
        t.columns = ["d", "a", "r", "obs"]
        t["row"] = df.index
        partes.append(t.dropna(subset=["d"]))
    D = pd.concat(partes)
    D["d"] = D["d"].str.rstrip(".")   # 'TEMPERATURA DE ENROLLADO (+/-).' = sin punto
    D["ret"] = D["r"] == "RETENIDO"
    return D


def tiene_defecto(df: pd.DataFrame, nombre: str) -> np.ndarray:
    """True si el rollo tiene el defecto en cualquiera de sus 5 posiciones."""
    m = np.zeros(len(df), bool)
    for k in range(1, 6):
        m |= (df[f"Defecto ({k})"] == nombre).values
    return m


def unir_mc4_skp(mc4: pd.DataFrame, skp: pd.DataFrame) -> pd.DataFrame:
    """Liga cada pieza del Skinpass con su rollo de MC4.

    Llave: SKP['Material Entrada'] == MC4['Material Salida']. Columnas de MC4 con sufijo ' MC4'.
    """
    lado = mc4.rename(columns={c: f"{c} MC4" for c in mc4.columns if c != "Material Salida"})
    lado = lado.rename(columns={"Material Salida": "Material Entrada"})
    return skp.merge(lado, on="Material Entrada", how="inner")


# ---------------------------------------------------------------- diccionario de columnas
# Cada columna se asigna al primer grupo cuya lista de fragmentos coincide con su nombre.
# El orden importa: "Temp Enrollado Obj" es especificación, "Temp Enrollado Real" es medición.
GRUPOS = [
    ("Defectos (5 bloques)", [r"\(\d\)$"]),
    ("Identificación y trazabilidad", ["^Material", "ID Salida", "Programa", "Secuencia", "Orden", "Necesidad",
                                       "^PRO$", "PRAM", "Colada", "Cliente", "Usuario", "Nro de Carro", "Origen_Archivo",
                                       "OFA", "Sociedad", "Rodillo de Trabajo$", "Rodillo de Trabajo Pareja$",
                                       "Rodillo Apoyo Superior$", "Rodillo Apoyo Pareja$"]),
    ("Tiempo", ["Fecha", "Tiempo"]),
    ("Temperaturas medidas", ["Temp.* Real", r"Temp\. F", r"Tempe\. F", r"Temp\. Acabador"]),
    ("Actuadores y operación", ["Canteo", "SSP", "Looper", "Offset", "Rodillo", "Enrollador", "Uso Modelo",
                                "Uso Cubierta", "Uso Aceite", "Kelk", "Barra Transferencia", "Spy", "Preset",
                                "Bending", "Real Prom", "Modo", "Medidor", "Fuente", "Taper Plc", r"^Ins\.", "Flejes"]),
    ("Calidad y dictamen", ["Dictamen", "Resolución", "Calidad", "Muestre", "Inspección", "Mal Enrollado",
                            "Superposición", "Observaciones", "Reproceso", "Empaque", "Solución", "Spring Back"]),
    ("Entrada (planchón al MC4, rollo al Skinpass)", ["Planchón", "Entrada", "Horno", "Descarga", "DAT", "Origen Peso"]),
    ("Especificación del pedido", ["Objetivo", "Obj", "Mínimo", "Máximo", "Min$", "Max$", "Teórico", "Teorico",
                                   "Norma", "Grado", "Subnorma", "Calibre", "Uso General", "Forma", "Criticidad",
                                   "Ruta", "Superficie", "Acabado", "Cara", "Posición", "Diam Interior",
                                   "Código", "Bordes", "Estado"]),
    ("Mediciones del rollo o pieza", ["Espesor", "Ancho", "Peso", "Largo", "Corona", "Acuñamiento", "Diam",
                                      "Taper", "Elongación", "Reflectividad", "Dividido", "RFID", "Corte"]),
]


def grupo_columna(col: str) -> str:
    """Grupo temático de una columna del MC4 o del Skinpass (ver GRUPOS)."""
    import re
    for grupo, fragmentos in GRUPOS:
        if any(re.search(f, col) for f in fragmentos):
            return grupo
    return "Otros"


def perfil_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """Una fila por columna: grupo, tipo, % lleno, valores distintos y un ejemplo."""
    return pd.DataFrame({
        "grupo": [grupo_columna(c) for c in df.columns],
        "tipo": df.dtypes.astype(str).str.replace("64", "").str.replace("[ns]", "", regex=False).values,
        "% lleno": (100 * df.notna().mean()).round(1).values,
        "distintos": df.nunique().values,
        "ejemplo": [str(df[c].dropna().iloc[0])[:30] if df[c].notna().any() else "" for c in df.columns],
    }, index=pd.Index(df.columns, name="columna"))


def r2_por_grupo(y: pd.Series, grupos: pd.Series) -> float:
    """Fracción de la varianza de y que explican las medias de cada grupo."""
    medias = y.groupby(grupos).transform("mean")
    return 1 - ((y - medias) ** 2).sum() / ((y - y.mean()) ** 2).sum()


# ---------------------------------------------------------------- figuras
def estilo(tamano: int = 11):
    plt.rcParams.update({
        "figure.dpi": 110, "savefig.dpi": 200, "savefig.bbox": "tight",
        "font.size": tamano, "axes.titlesize": tamano + 1, "axes.titlelocation": "left",
        "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False,
    })


def guardar(fig, nombre: str):
    """Guarda la figura en figuras/<nombre>.png."""
    FIGURAS.mkdir(exist_ok=True)
    fig.savefig(FIGURAS / f"{nombre}.png")
