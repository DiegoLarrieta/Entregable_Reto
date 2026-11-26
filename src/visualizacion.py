"""Estilo común para que todas las figuras se vean igual (artículo y presentaciones)."""
from pathlib import Path

import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parents[1]
FIGURAS = RAIZ / "outputs" / "figuras"

COLORES = {"acero": "#2d5d86", "caliente": "#e2470f", "gris": "#7d8790", "ok": "#2f7a4b"}


def estilo(tamano_letra: int = 14):
    """Llamar una vez al inicio del notebook. Usen 18 para slides."""
    plt.rcParams.update({
        "figure.dpi": 110, "savefig.dpi": 300, "savefig.bbox": "tight",
        "font.size": tamano_letra, "axes.titlesize": tamano_letra + 2,
        "axes.labelsize": tamano_letra, "xtick.labelsize": tamano_letra - 2,
        "ytick.labelsize": tamano_letra - 2, "legend.fontsize": tamano_letra - 2,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.prop_cycle": plt.cycler(color=list(COLORES.values())),
    })


def guardar(fig, nombre: str):
    """Guarda en outputs/figuras/<nombre>.png y .pdf (el PDF va al LaTeX)."""
    FIGURAS.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(FIGURAS / f"{nombre}.{ext}")
    return FIGURAS / f"{nombre}.png"
