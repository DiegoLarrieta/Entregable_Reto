"""Reglas de depuración y definiciones del proyecto.

Todas las decisiones se fijaron ANTES de mirar resultados (ver docs/plan_de_analisis.md).
Si cambian una regla, cámbienla aquí y documenten por qué.
"""
import numpy as np
import pandas as pd

# --- Umbrales -------------------------------------------------------------
CORONA_VALIDA_UM = (0, 300)       # fuera de este rango es físicamente imposible
CORTES_ESPESOR_MM = [0, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 13]

# --- Variables prohibidas como explicativas ------------------------------
# Se generan con el resultado o después de él (Fenómeno 1 de la Entrega 1).
PROHIBIDAS_BASE = ["Dictamen", "Resolución", "Calidad Sugerida", "Observaciones",
                   "Observaciones Calidad", "Fecha Registro"]
PREFIJOS_DEFECTO = ["Codigo defecto", "Defecto", "Causa", "Calidad", "Dictamen",
                    "Resolución", "Observaciones", "Fecha Registro", "Registro Automatico"]


def columnas_prohibidas(df: pd.DataFrame) -> list[str]:
    """Columnas que NUNCA deben entrar como variable explicativa."""
    fuera = [c for c in df.columns if c in PROHIBIDAS_BASE]
    fuera += [c for c in df.columns if any(c.startswith(p + " (") for p in PREFIJOS_DEFECTO)]
    return sorted(set(fuera))


# --- Definiciones ---------------------------------------------------------
def destino_skinpass(mc4: pd.DataFrame) -> pd.Series:
    """True si la Ruta Teórica incluye el Skinpass. Es intención, no recorrido confirmado."""
    return mc4["Ruta Teórica"].astype("string").str.contains("SKP_PSQ", na=False)


def rango_espesor(espesor_objetivo: pd.Series) -> pd.Series:
    """Rango de espesor objetivo (NO usar máximo - mínimo de tolerancia)."""
    return pd.cut(espesor_objetivo, CORTES_ESPESOR_MM).astype("string")


def producto(df: pd.DataFrame, norma="Norma", grado="Grado",
             espesor_obj="Espesor Objetivo") -> pd.Series:
    """Producto = Norma | Grado | rango de Espesor Objetivo."""
    return (df[norma].astype("string") + " | " + df[grado].astype("string")
            + " | " + rango_espesor(df[espesor_obj]))


def corona_valida(corona_um: pd.Series) -> pd.Series:
    lo, hi = CORONA_VALIDA_UM
    return corona_um.between(lo, hi)


def corona_relativa(corona_um: pd.Series, espesor_mm: pd.Series) -> pd.Series:
    """Corona como % del espesor."""
    return corona_um / 1000 / espesor_mm * 100


def defectos_largo(df: pd.DataFrame, id_col="Material Salida") -> pd.DataFrame:
    """Pasa los 5 bloques de defecto a formato largo: una fila por defecto registrado."""
    partes = []
    for k in range(1, 6):
        cols = {f"Defecto ({k})": "Defecto", f"Linea Origen ({k})": "Linea Origen",
                f"Causa ({k})": "Causa", f"Registro Automatico ({k})": "Automatico"}
        for calidad in (f"Calidad ({k})", f"Dictamen ({k})"):
            if calidad in df.columns:
                cols[calidad] = "Calidad"
        presentes = {c: n for c, n in cols.items() if c in df.columns}
        parte = df[[id_col, *presentes]].rename(columns=presentes)
        parte = parte[parte["Defecto"].notna()]
        parte["Bloque"] = k
        partes.append(parte)
    return pd.concat(partes, ignore_index=True)


def skinpass_primera_pasada(skp: pd.DataFrame) -> pd.DataFrame:
    """Filas del Skinpass en modo SKP, sin reprocesos, una por rollo de entrada."""
    f = skp[(skp["Modo"] == "SKP") & (skp["Es Reproceso"] == 0)]
    return f.sort_values("Fecha Inicio").drop_duplicates("Material Entrada")
