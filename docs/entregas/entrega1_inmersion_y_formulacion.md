# Entrega 1: Inmersión y formulación

> Resumen de la guía publicada en Canvas (curso 689430). La guía original manda; esto es para tenerla a la mano.
> Estado: **entregada el 12 de noviembre de 2026** (PDF "Entendiendo la Variabilidad de Entrada al Skinpass").

## Qué era
El primer hallazgo del reto: Ternium preguntó por el **Skinpass** (dado un producto y su condición de entrada, ¿qué combinación de bending, elongación, fuerza, tensión y velocidad se asocia con la mejor calidad?), pero los 24 archivos de 2025 solo describen el **Molino Caliente 4 de Pesquería** (~150 mil rollos, 280 columnas). Sin configuraciones ni calidad del Skinpass, la pregunta original no se puede responder. No es un fracaso: el objetivo era encontrar una pregunta que los datos sí respondan y que siga siendo relevante para Ternium.

Es una **investigación científica preliminar**, no un inventario de estadísticas ni una competencia de modelos. Al terminar había que poder defender:
1. qué representa cada variable usada y cómo se generó;
2. qué pregunta responderán y por qué importa a Ternium y al campo;
3. qué se sabe sobre la pregunta y cuál es el vacío;
4. qué evidencia preliminar indica que es viable;
5. qué no puede responderse con estos datos y qué información faltaría.

## Lista rápida
1. Leer y auditar los 24 archivos con un proceso reproducible.
2. Mapa del proceso y diccionario razonado.
3. Población de estudio, jerarquía de producto y subpoblación con destino al Skinpass.
4. Revisión sistemática (no exhaustiva) de 10 a 15 fuentes académicas.
5. Explorar al menos 3 fenómenos (1 y 2 obligatorios, el tercero libre).
6. Pregunta de investigación precisa con diagrama causal.
7. Documento de máximo 10 páginas + anexos + repositorio reproducible.

## Componentes y peso

| Componente | Peso | Criterios |
|---|---|---|
| 1. Proceso, variables y población | 20% | Precisión del diccionario 8%, comprensión física 6%, caracterización honesta 6% |
| 2. Literatura y posicionamiento | 25% | Comprensión 10%, calidad de fuentes 5%, pensamiento crítico 5%, posicionamiento 5% |
| 3. Exploración estratégica | 40% | Parsimonia 10%, conexión teoría-datos 10%, rigor interpretativo 15%, originalidad 5% |
| 4. Pregunta de investigación | 15% | Especificidad y viabilidad 5%, diagrama causal y respondibilidad 5%, originalidad 3%, honestidad sobre limitaciones 2% |

### Componente 1: Inmersión en el proceso y los datos
- **Mapa del proceso** (máx. 1 página): horno, descascarado, desbaste R1/R2, barra de transferencia, tren acabador F1-F7, loopers, enfriamiento, enrollado, inspección; ubicar dónde se genera cada grupo de variables y extender hasta el Skinpass según `Ruta Teórica`.
- **Diccionario razonado** (anexo): significado, unidades, punto de generación, calidad y tipo. Distinguir consigna, medición y etiqueta derivada; palanca, respuesta, característica del material y variable posterior al resultado. Si es un resumen por rollo, decir qué resume.
- **Caracterización de la población** (máx. 1.5 páginas): cobertura temporal, continuidad, rollos por periodo, jerarquía de producto, subpoblación con destino al Skinpass, patrón de faltantes. Definir qué es "producto" y "tipo de material".
- **Preguntas al Socio Formador** (anexo): no inferir variables ambiguas por el nombre.

### Componente 2: Literatura y posicionamiento
- Conectar dos conversaciones: física y control de laminación, y razonamiento causal con datos observacionales.
- 10 a 15 fuentes; libros de referencia y artículos arbitrados (no blogs ni Wikipedia). Síntesis por temas, no resúmenes aislados.
- Productos: síntesis temática, tabla de 4 a 7 marcos teóricos (proposición, variables, evidencia, limitaciones), 2 o 3 vacíos o tensiones, *contribution statement* preliminar ("Este trabajo se ubica en... A diferencia de... nosotros... Esto permite...").

### Componente 3: Exploración estratégica
Explorar con preguntas y mecanismos plausibles; **todavía no se piden modelos predictivos**. Por fenómeno: pregunta, análisis (sin código en el documento), hallazgos cuantitativos, interpretación con literatura, implicaciones para el diseño. Máximo 6 figuras en total, cada una con un hallazgo y unidades. Notebook que corra de principio a fin sobre los 24 archivos, semillas fijas, limpieza documentada, sección de **callejones sin salida**.

Los seis fenómenos de la guía:

| # | Fenómeno | Pregunta guía | Pista preliminar de la guía (verificar, no citar como propia) |
|---|---|---|---|
| 1 | ¿Qué significa "calidad"? (obligatorio) | ¿Qué variables de calidad miden una condición del rollo y cuáles son reglas aplicadas a otras columnas? | ~88% de rollos con algún defecto; ~mitad RETENIDO; 3 de cada 4 registros automáticos |
| 2 | ¿De dónde sale la "receta"? (obligatorio) | Dentro de un producto, ¿cambian las consignas y qué explica el cambio? | ≥29 celdas con >200 rollos y 2 o 3 temperaturas objetivo (580 / 620 °C) |
| 3 | La receta única vista desde la entrada | ¿Los productos de una familia llegan parecidos al Skinpass? | Llegar distinto no prueba que respondan distinto: nivel no es interacción |
| 4 | Programa de laminación como experimento no diseñado | ¿La posición en el programa se relaciona con el resultado, separándola del producto? | ~1,800 programas, mediana ~65 rollos; ancho 1,260 → 1,510 → <1,000 mm; óxido de rodillos <2% → >14% |
| 5 | Efectos que cambian de signo | ¿La consigna alta se asocia siempre con más óxido? | Un producto 41% vs 4%; otro pequeño; otro invertido |
| 6 | La calidad del dato como hallazgo | ¿Los problemas de datos son al azar o siguen el proceso? | Columnas vacías, centinelas, imposibles, duplicados |

**Resultado esperado por fenómeno:** (1) definición operativa de calidad + variables prohibidas + qué resultados de MC4 importan al Skinpass; (2) mapa de variación de consignas clasificado en aprovechable / sospechoso de confusión / irrelevante; (3) heterogeneidad de entrada por familia y la afirmación máxima sin datos del Skinpass; (6) diagnóstico de faltantes y protocolo de depuración.

### Componente 4: Formulación de la pregunta
Una oración precisa + justificación teórica (vacío, 2-3 fuentes) + justificación empírica + **diagrama causal preliminar** (material, especificación/cliente, consignas, mediciones, contexto operativo, resultado; marcar no observadas; explicar flechas y caminos de confusión) + argumento de respondibilidad (variación, origen, traslape, supuestos) + versión modesta + limitaciones anticipadas + contribución esperada.

Ejemplos de la guía:
- **Engañosa:** "¿Podemos predecir el dictamen con ML?" (el dictamen sale de reglas sobre las mismas variables).
- **Descriptiva viable:** fracción de la variación en corona relativa y acuñamiento explicada por producto y por posición en el programa, y si cambia entre familias.
- **Promete demasiado:** "¿Cuál es la temperatura de enrollado óptima por producto?"
- **Causal defendible:** en productos donde la consigna cambió en el tiempo sin cambiar el cliente, ¿se asocia con defectos de óxido y sobrevive a un control negativo?
- **Metodológica útil:** ¿los defectos térmicos automáticos contienen información que no esté en los resúmenes por rollo?

## Estructura del documento (máx. 10 páginas)
| Sección | Extensión | Contenido |
|---|---|---|
| 1. Introducción | 0.5 p | Problema original, limitación, propósito |
| 2. Proceso y datos | 2 p | Mapa, población, jerarquía de producto, naturaleza de los datos |
| 3. Literatura y posicionamiento | 2 p | Síntesis, marcos, tensiones, contribución |
| 4. Exploración estratégica | 3.5 p | Tres fenómenos, evidencia, interpretación, implicaciones |
| 5. Pregunta de investigación | 2 p | Pregunta, justificaciones, diagrama, respondibilidad, límites |

Referencias en APA, mínimo 10 académicas, todas verificadas (una inventada = plagio). Anexos: diccionario razonado y preguntas al Socio Formador.

## Repositorio reproducible
Código desde los archivos originales sin ediciones manuales; `requirements.txt`; rutas configurables e instrucciones en `README.md`; reglas de limpieza documentadas antes de ver resultados; **sin datos de Ternium en repos públicos**. Estructura sugerida por el profesor: `notebooks/01..04`, `src/carga.py`, `src/depuracion.py`, `src/visualizacion.py`, `outputs/figuras/`, `README.md`. Este repo la simplifica: un solo `src/ternium.py` y `figuras/` en la raíz.

## Checklist antes de entregar
- ¿La pregunta se responde con las variables disponibles?
- ¿Definieron "producto", "calidad" y población?
- ¿Distinguen consignas, mediciones y etiquetas derivadas?
- ¿Evitaron información posterior o tautológica para explicar el resultado?
- ¿Cada afirmación importante tiene evidencia cuantitativa?
- ¿Diferencian "observamos" de "concluimos"?
- ¿Documentaron resultados negativos, incertidumbres y exclusiones?
- ¿El repo corre sin exponer datos confidenciales?

## Marcos de literatura sugeridos
Perfil, corona y planeza (Ginzburg; Roberts; Shohet y Townsend) · Laminación de temple / Skinpass (Ginzburg y Ballas; Lenard) · Temperatura, cascarilla y microestructura · Datos de ocasión (Box; Box, Hunter y Hunter) · Inferencia causal observacional (Hernán y Robins; Rosenbaum y Rubin) · Heterogeneidad y estimación parcial · Fuga de información · Ciencia de datos en manufactura.

## Preguntas frecuentes (resumen)
- **Sin datos del Skinpass, ¿sirve?** Sí: cuantificar cómo llegan los productos, cómo se asignan recetas y qué datos faltan; el marco se reutiliza cuando existan datos del Skinpass.
- **¿Se puede cambiar la pregunta?** Refinarla sí; un cambio de raíz requiere justificación y aprobación docente.
- **¿Cuántos fenómenos?** Mínimo tres; tres profundos valen más que seis superficiales.
- **¿Excluir rollos con datos malos?** Sí, documentando criterio, conteo y si la exclusión se relaciona con el resultado.
- **Sofisticación esperada:** tablas cruzadas, proporciones y medias con intervalos, descomposiciones de varianza, buenas visualizaciones. Modelos complejos en etapas posteriores.

## Qué entregamos nosotros (resumen)
- Población: 149,734 rollos; 50,016 con `SKP_PSQ` en ruta; producto = Norma | Grado | rango de Espesor Objetivo.
- Fenómenos elegidos: 1 (calidad), 2 (receta) y 4 (programa de laminación).
- Hallazgos clave: 76% de registros de defecto automáticos; la consigna de enrollado la fija PRAM (100% de la varianza dentro de producto); dentro de producto la posición explica 1.5% de la varianza de la corona, el producto 28% y el programa 45%.
- Pregunta: fracción de la variación de Corona y Acuñamiento de salida explicada por historia térmica (Temp. Enrollado) vs desgaste (Secuencia), y si cambia por grado.
- Pendientes detectados: la sección 5.3 dice 138,131 rollos con destino al Skinpass (debe ser 50,016); la pregunta usa Secuencia y temperatura aunque nuestros propios hallazgos muestran que la primera explica poco y la segunda sigue al cliente.
