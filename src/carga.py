"""Carga de los archivos crudos de MC4 y Skinpass.

La primera lectura de los Excel tarda ~1 minuto; después se guarda una copia
en data/interim/*.parquet y las siguientes cargas tardan segundos.

    from src.carga import cargar_mc4, cargar_skp, unir_mc4_skp
    mc4 = cargar_mc4()
    skp = cargar_skp()
    rollos = unir_mc4_skp(mc4, skp)
"""
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
RAW = RAIZ / "data" / "raw"
INTERIM = RAIZ / "data" / "interim"

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


def _orden(ruta: Path):
    partes = ruta.stem.split()
    return (MESES.index(partes[1]), ruta.name)


def _leer_carpeta(carpeta: Path, patron: str) -> pd.DataFrame:
    archivos = sorted(carpeta.glob(patron), key=_orden)
    if not archivos:
        raise FileNotFoundError(
            f"No hay archivos en {carpeta}. Corre primero: python scripts/descargar_datos.py")
    partes = []
    for ruta in archivos:
        df = pd.read_excel(ruta, engine="calamine")
        df["Archivo Origen"] = ruta.name
        df["Mes Archivo"] = ruta.stem.split()[1]
        partes.append(df)
    df = pd.concat(partes, ignore_index=True)
    # columnas de texto mezclado -> str, para poder guardar en parquet
    for c in df.columns[df.dtypes == object]:
        df[c] = df[c].astype("string")
    return df


def _cargar(nombre: str, carpeta: Path, patron: str, recargar: bool) -> pd.DataFrame:
    cache = INTERIM / f"{nombre}.parquet"
    if cache.exists() and not recargar:
        return pd.read_parquet(cache)
    df = _leer_carpeta(carpeta, patron)
    INTERIM.mkdir(parents=True, exist_ok=True)
    df.to_parquet(cache, index=False)
    return df


def cargar_mc4(recargar: bool = False) -> pd.DataFrame:
    """149,734 rollos del Molino Caliente 4 (una fila por rollo, 2025)."""
    return _cargar("mc4", RAW / "mc4", "MC4_PSQ*.xlsx", recargar)


def cargar_skp(recargar: bool = False) -> pd.DataFrame:
    """~58,786 piezas procesadas en el Skinpass (2025).

    Un rollo de MC4 puede salir del Skinpass en 2 o 3 piezas (sufijos PS100, PS101...).
    """
    return _cargar("skp", RAW / "skp", "SKP_PSQ*.xlsx", recargar)


def unir_mc4_skp(mc4: pd.DataFrame, skp: pd.DataFrame,
                 columnas_mc4: list[str] | None = None) -> pd.DataFrame:
    """Une cada pieza del Skinpass con su rollo de MC4.

    Llave: SKP["Material Entrada"] == MC4["Material Salida"] (se liga ~97%).
    Las columnas de MC4 llevan el sufijo " MC4" para no confundirse con las del Skinpass.
    """
    if columnas_mc4 is None:
        columnas_mc4 = list(mc4.columns)
    if "Material Salida" not in columnas_mc4:
        columnas_mc4 = ["Material Salida", *columnas_mc4]
    lado_mc4 = mc4[columnas_mc4].rename(
        columns={c: f"{c} MC4" for c in columnas_mc4 if c != "Material Salida"})
    lado_mc4 = lado_mc4.rename(columns={"Material Salida": "Material Entrada"})
    return skp.merge(lado_mc4, on="Material Entrada", how="inner", validate="many_to_one")
