<p align="center"><img src="docs/img/ternium_logo.png" alt="Ternium" width="320"></p>

# Ternium MC4 → Skinpass

Proyecto del curso *Desarrollo de aplicaciones avanzadas de ciencias computacionales* (Tec de Monterrey, Ago-Dic 2026), con datos de Ternium Pesquería.

**Equipo:** Francisco Vaquera Saavedra · Armando Calzada Delgado · María José Vital Castillo · Luis Diego Dominguez Larrieta

## El proyecto en una frase
Ternium pregunta si conviene diferenciar recetas del Skinpass por producto. Ligamos un año de rollos del Molino Caliente 4 (MC4) con su paso por el Skinpass para medir qué tanto la condición de entrada explica lo que el Skinpass tuvo que hacer, más allá de la receta.

## El proceso en 30 segundos

<table>
<tr>
<td width="50%"><img src="docs/img/molino_caliente.png" alt="Molino caliente laminando una barra al rojo vivo"></td>
<td width="50%"><img src="docs/img/skinpass.png" alt="Castillo de laminación tipo Skinpass con rodillos de trabajo y de apoyo"></td>
</tr>
<tr>
<td><b>1. Molino Caliente 4 (MC4).</b> El planchón se calienta a ~1,200 °C, se adelgaza en desbaste (R1, R2) y en el tren acabador (F1 a F7), se enfría en la mesa y se enrolla. Aquí se define la <b>corona</b> (centro más grueso que los bordes), el acuñamiento y la temperatura de enrollado. <i>Datos: 24 archivos MC4_PSQ.</i></td>
<td><b>2. Skinpass.</b> Días después (~5), el rollo pasa por un laminado en frío muy ligero: lo estira apenas 1 a 2% (<b>elongación</b>) con una <b>fuerza</b>, <b>tensiones</b> y <b>bending</b> (doblado de los rodillos) para corregir planeza y dar el acabado final. <i>Datos: 12 archivos SKP_PSQ.</i></td>
</tr>
</table>

**La pregunta de Ternium:** hoy el Skinpass usa una receta por tipo de material. ¿Conviene diferenciarla por producto según cómo llega cada rollo del MC4? Para eso ligamos cada rollo del MC4 con su paso por el Skinpass.

<sub>Imágenes ilustrativas: molino caliente (foto de AHMSA) y castillo de laminación (ilustración de SMS Siemag); no son las líneas de Pesquería.</sub>

## Cómo correrlo

**En Colab (lo más fácil):** abre el notebook y dale *Entorno de ejecución → Ejecutar todo*. La primera celda descarga el repo con los datos e instala lo necesario; no pide token ni login.

**Investigación MC4–Skinpass** (propuesta de validación metodológica):

| Notebook | |
|---|---|
| 00 · Auditoría de datos y definiciones | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiegoLarrieta/Entregable_Reto/blob/main/notebooks/00_Auditoria_Datos.ipynb) |
| 01 · Exploración por bloques (EDA) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiegoLarrieta/Entregable_Reto/blob/main/notebooks/01_EDA_MC4_Skinpass.ipynb) |
| 02 · Correlaciones dentro de producto y PCA | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiegoLarrieta/Entregable_Reto/blob/main/notebooks/02_Correlaciones_y_PCA.ipynb) |
| 03 · Ingeniería de variables y base analítica | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiegoLarrieta/Entregable_Reto/blob/main/notebooks/03_Feature_Engineering.ipynb) |
| 04 · Modelos del esfuerzo mecánico (LMM y GBDT) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiegoLarrieta/Entregable_Reto/blob/main/notebooks/04_Modelos_Esfuerzo_Mecanico.ipynb) |
| 05 · Modelos de retenciones (B1, B2 y administrativa) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiegoLarrieta/Entregable_Reto/blob/main/notebooks/05_Modelos_Retenciones.ipynb) |
| 06 · Análisis causal: mediación y Double ML | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiegoLarrieta/Entregable_Reto/blob/main/notebooks/06_Analisis_Causal_y_Mediacion.ipynb) |
| 07 · Experimento natural: desgaste del rodillo | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiegoLarrieta/Entregable_Reto/blob/main/notebooks/07_Experimento_Natural_Rodillos.ipynb) |
| 08 · Evaluación final y diseño del experimento en planta | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiegoLarrieta/Entregable_Reto/blob/main/notebooks/08_Diseno_Experimental_Planta.ipynb) |

**Antecedentes** (Entrega 1):

| Notebook | |
|---|---|
| 01 · Datos, reglas y población | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiegoLarrieta/Entregable_Reto/blob/main/notebooks/antecedentes/01_datos.ipynb) |
| 02 · Calidad | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiegoLarrieta/Entregable_Reto/blob/main/notebooks/antecedentes/02_calidad.ipynb) |
| 03 · Receta | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiegoLarrieta/Entregable_Reto/blob/main/notebooks/antecedentes/03_receta.ipynb) |
| 04 · Programa de laminación | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiegoLarrieta/Entregable_Reto/blob/main/notebooks/antecedentes/04_programa.ipynb) |

**En local:**

```bash
git clone https://github.com/DiegoLarrieta/Entregable_Reto.git
cd Entregable_Reto
pip install -r requirements.txt
```

Abre cualquier notebook de `notebooks/` o `notebooks/antecedentes/` (Jupyter o VS Code con un kernel de Python local) y dale *Run All*. Los Excel ya vienen en `data/`, no hay que descargar nada. Cada notebook tarda alrededor de un minuto en cargar los datos.

## Estructura

```
Entregable_Reto/
├── data/
│   ├── mc4/          # 24 Excel quincenales del Molino Caliente 4 (149,734 rollos)
│   └── skp/          # 12 Excel mensuales del Skinpass (58,786 piezas)
├── notebooks/
│   ├── 00_… 08_…           # investigación MC4–Skinpass (propuesta de validación metodológica), en construcción
│   └── antecedentes/       # trabajo previo (Entrega 1), se conserva tal cual
│       ├── 01_datos.ipynb      # carga, auditoría, reglas de limpieza, población, liga MC4 → Skinpass
│       ├── 02_calidad.ipynb    # Fenómeno 1: qué significa "calidad" (figura 1)
│       ├── 03_receta.ipynb     # Fenómeno 2: de dónde sale la receta (figura 2)
│       ├── 04_programa.ipynb   # Fenómeno 4: el programa de laminación (figura 3)
│       └── investigacion.ipynb # ¿el defecto nace en el MC4 o en el Skinpass?
├── src/
│   └── ternium.py    # carga de datos, reglas de limpieza y estilo de figuras: todo lo compartido
├── figuras/          # PNG de cada figura; se regeneran al correr los notebooks
├── docs/             # guías de las entregas, plan de análisis, preguntas a Ternium
└── requirements.txt
```

| Figura | Notebook | Qué muestra |
|---|---|---|
| `fig0_cobertura` | 01 | Un año completo y continuo de datos en MC4 y Skinpass |
| `fig1_calidad` | 02 | Los defectos más frecuentes son reglas automáticas |
| `fig2_receta` | 03 | La consigna de enrollado la fija el PRAM (ligado al cliente) |
| `fig3_programa` | 04 | La posición en el programa arrastra la mezcla de producto |

**Siguientes notebooks** (entrega final): `05_skinpass` (preset contra real), `06_modelo` (análisis principal con errores agrupados por programa) y `07_comprobaciones` (control negativo, robustez, estabilidad en el tiempo).

## Entregas
| Entrega | Qué pide | Estado |
|---|---|---|
| [Entrega 1: Inmersión y formulación](docs/entregas/entrega1_inmersion_y_formulacion.md) | Proceso, literatura, 3 fenómenos, pregunta con diagrama causal (máx. 10 p) | Entregada 12/nov |
| [Entrega final: el artículo](docs/entregas/entrega_final_articulo.md) | Análisis principal con validación, traducción a Ternium, propuesta de experimento | En curso |

## Reglas del equipo
1. Nadie edita los Excel. Toda regla de limpieza va en `src/ternium.py`.
2. Si una función se usa en 2 notebooks, va a `src/ternium.py`.
3. Las figuras se guardan con `guardar(fig, "nombre")`, nunca capturas de pantalla.
4. Cada notebook: una pregunta, markdown breve antes de cada paso y un "Qué vemos" después de cada tabla o figura.
5. Trabajen en una rama (`git checkout -b diego/fenomeno2`) y abran Pull Request a `main`.
6. Antes de hacer commit de un notebook: *Restart & Run All* y verifiquen que no imprima tablas enormes de datos.

## Datos: llave y definiciones
- **Llave MC4 ↔ Skinpass:** `SKP["Material Entrada"] == MC4["Material Salida"]` (se liga ~97%).
- **Destino Skinpass:** `Ruta Teórica` contiene `SKP_PSQ` (50,016 rollos; 47,410 sí pasaron).
- **Producto:** Norma | Grado | rango de Espesor Objetivo (cortes 1.5, 2, 2.5, 3, 4, 5, 6, 8, 13 mm).
- **Corona válida:** 0 a 300 µm.
