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
def _leer(carpeta: Path, patron: str) -> pd.DataFrame:
    archivos = sorted(carpeta.glob(patron), key=lambda p: (MESES.index(p.stem.split()[1]), p.name))
    if not archivos:
        raise FileNotFoundError(f"No hay archivos {patron} en {carpeta}")
    return pd.concat(
        [pd.read_excel(a, engine="calamine").assign(Origen_Archivo=a.name) for a in archivos],
        ignore_index=True,
    )


def cargar_mc4() -> pd.DataFrame:
    """24 archivos quincenales del Molino Caliente 4 (149,734 rollos, 2025)."""
    return _leer(DATOS / "mc4", "MC4_PSQ*.xlsx")


def cargar_skp() -> pd.DataFrame:
    """12 archivos mensuales del Skinpass (58,786 piezas, 2025)."""
    return _leer(DATOS / "skp", "SKP_PSQ*.xlsx")


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
    """Guarda la figura en figuras/<nombre>.png y .pdf (el PDF va al LaTeX)."""
    FIGURAS.mkdir(exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(FIGURAS / f"{nombre}.{ext}")
