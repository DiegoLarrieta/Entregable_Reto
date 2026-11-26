# Ternium MC4 → Skinpass

Proyecto del curso *Desarrollo de aplicaciones avanzadas de ciencias computacionales* (Tec de Monterrey, Ago-Dic 2026), con datos de Ternium Pesquería.

**Equipo:** Francisco Vaquera Saavedra · Armando Calzada Delgado · María José Vital Castillo · Luis Diego Dominguez Larrieta

> ⚠️ **Confidencial. Este repositorio debe seguir siendo PRIVADO.** Incluye los 36 Excel originales de Ternium en `data/raw/`, cubiertos por un acuerdo de confidencialidad. No lo hagan público, no lo forkeen a cuentas personales públicas y no suban los datos a ningún otro lado. Si algún día se hace público, primero hay que borrar `data/raw/` de todo el historial.

## El proyecto en una frase
Ternium pregunta si conviene diferenciar recetas del Skinpass por producto. Ligamos un año de rollos del Molino Caliente 4 (MC4) con su paso por el Skinpass para medir qué tanto la condición de entrada explica lo que el Skinpass tuvo que hacer, más allá de la receta.

## Arranque rápido (5 minutos)

```bash
git clone https://github.com/DiegoLarrieta/Entregable_Reto.git
cd Entregable_Reto
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# los 36 Excel ya vienen en data/raw/; si faltara alguno:
python scripts/descargar_datos.py
```

Luego, en cualquier notebook:

```python
import sys; sys.path.insert(0, "..")   # si el notebook está en notebooks/
from src.carga import cargar_mc4, cargar_skp, unir_mc4_skp
mc4 = cargar_mc4()   # 1a vez ~1 min; después segundos (cache en data/interim/)
skp = cargar_skp()
```

### En Google Colab
```python
!git clone https://github.com/DiegoLarrieta/Entregable_Reto.git   # pide token si el repo es privado
%cd Entregable_Reto
!pip install -q python-calamine
# los Excel ya vienen en data/raw/ al clonar
```

## Estructura

```
Entregable_Reto/
├── data/                      # raw/ sí está en el repo (privado); interim/ no
│   ├── raw/mc4/               # 24 Excel quincenales del MC4 (149,734 rollos)
│   ├── raw/skp/               # 12 Excel mensuales del Skinpass (58,786 piezas)
│   └── interim/               # caché .parquet que genera src/carga.py
├── notebooks/
│   └── 00_colab_original_EDA.ipynb   # el Colab de la Entrega 1, tal cual
├── src/                       # código compartido: se importa, no se copia
│   ├── carga.py               # leer MC4 y SKP, unirlos rollo a rollo
│   ├── depuracion.py          # reglas fijas: corona válida, producto, variables prohibidas
│   └── visualizacion.py       # estilo común de figuras y guardado
├── scripts/
│   └── descargar_datos.py     # baja los 36 archivos del Drive
├── outputs/
│   ├── figuras/               # cada figura del artículo, regenerable
│   └── tablas/                # tabla completa de contrastes, etc.
├── docs/
│   ├── entregas/              # resumen de lo que pide cada entrega
│   ├── plan_de_analisis.md    # decisiones fijadas antes de ver resultados
│   └── preguntas_socio_formador.md
└── requirements.txt
```

### Notebooks planeados (se irán llenando)
| Notebook | Contenido | Viene de |
|---|---|---|
| `01_carga_y_auditoria` | Conteos, faltantes, llave MC4↔SKP, cobertura de ruta teórica | Entrega 1 §2 |
| `02_diccionario_y_poblacion` | Variables usadas, definición de producto, población final | Entrega 1 §2.3 |
| `03_fenomeno1_etiquetas_de_calidad` | Defectos automáticos vs manuales, variables prohibidas | Entrega 1 §4.1 |
| `04_fenomeno2_asignacion_de_consignas` | PRAM fija la consigna; soporte por producto | Entrega 1 §4.2 |
| `05_programa_de_laminacion` | Secuencia, programa como grupo | Entrega 1 §4.3 |
| `06_skinpass_preset_vs_real` | Fuerza, bending, tensión: preset contra real | Nuevo |
| `07_modelo_principal` | Regresión de efectos mixtos + validación por programa | Entrega final |
| `08_comprobaciones` | Control negativo, robustez, estabilidad temporal | Entrega final |

Regla: **un notebook = una pregunta**, nombrado con número para que se lea en orden, y que corra de principio a fin con *Restart & Run All*.

## Entregas
| Entrega | Qué pide | Estado |
|---|---|---|
| [Entrega 1: Inmersión y formulación](docs/entregas/entrega1_inmersion_y_formulacion.md) | Proceso, literatura, 3 fenómenos, pregunta con diagrama causal (máx. 10 p) | Entregada 12/nov |
| [Entrega final: el artículo](docs/entregas/entrega_final_articulo.md) | Análisis principal con validación, traducción a Ternium, propuesta de experimento | En curso |

## Reglas del equipo
1. Nadie edita los Excel. Toda limpieza va en `src/depuracion.py`.
2. Si una función se usa en 2 notebooks, va a `src/`.
3. Las figuras se guardan con `src.visualizacion.guardar(fig, "nombre")`, nunca capturas de pantalla.
4. Trabajen en una rama (`git checkout -b diego/fenomeno2`) y abran Pull Request a `main`.
5. Antes de hacer commit de un notebook: *Restart & Run All* y verifiquen que no imprima tablas enormes de datos.

## Datos: llave y definiciones
- **Llave MC4 ↔ Skinpass:** `SKP["Material Entrada"] == MC4["Material Salida"]` (se liga ~97%).
- **Destino Skinpass:** `Ruta Teórica` contiene `SKP_PSQ` (50,016 rollos; 47,410 sí pasaron).
- **Producto:** Norma | Grado | rango de Espesor Objetivo (cortes 1.5, 2, 2.5, 3, 4, 5, 6, 8, 13 mm).
- **Corona válida:** 0 a 300 µm.
