# Entrega final: el artículo

> Resumen de la guía publicada en Canvas (assignment 23918895). La guía original manda.
> Pregunta guía: **¿qué puedo afirmar con honestidad, qué significa para Ternium y qué propongo probar?**

Responder la pregunta de la Entrega 1 y contarlo como artículo científico casi publicable (español, plantilla LaTeX de una revista real: JMS, Computers in Industry, Quality Engineering, JQT, Steel Research International, IEEE CASE). **Un análisis principal bien hecho con 2 o 3 comprobaciones serias**, no un catálogo de modelos.

## Orden de trabajo
1. Decidir el tipo de contribución.
2. Convertir la exploración de la E1 en un argumento.
3. Cerrar el análisis principal (decisiones, validación, incertidumbre).
4. Traducir a la decisión de Ternium sin exagerar.
5. Proponer validación y los datos del Skinpass que faltan.
6. Escribir.

## Evaluación
| Criterio | Peso | Excelente |
|---|---|---|
| Rigor metodológico | 25% | Resultado sin etiquetas tautológicas; ajuste derivado del diagrama; soporte antes de estimar; dependencia tratada |
| Validación e incertidumbre | 20% | Intervalos o variación entre particiones vs línea base; ≥2 anclajes con criterio de refutación; confusión no medida; multiplicidad |
| Traducción y propuesta de validación | 20% | Peldaño correcto; indicadores secundarios; experimento con unidad de bloqueo y volumen; datos del Skinpass |
| Pregunta, contribución y argumento | 15% | Una afirmación central; cada sección la sirve |
| Literatura y escritura | 10% | Por temas; figuras autocontenidas; registro de la revista |
| Reproducibilidad | 10% | Un tercero regenera todas las figuras y tablas sin intervención |

## Secciones
Título (hallazgo, no tema) · Resumen ~250 palabras (al final) · Introducción (giro de E1 como hallazgo + contribuciones verificables) · Literatura (por temas) · Datos y metodología (población, producto, depuración con conteos, resultado y prohibidas, diagrama y ajuste, soporte, dependencia, método, validación, sensibilidad) · Resultados (soporte → estimación → comprobaciones; máx. 6 figuras/tablas) · Discusión (limitaciones como hallazgos) · Conclusiones y propuesta de validación · Referencias (todas verificadas) · Anexos (diccionario, preguntas al Socio Formador, tabla completa de contrastes, plan de análisis).

**Prueba de coherencia:** resumen, última frase de la intro, títulos de figuras y primer párrafo de conclusiones cuentan la misma historia.

## Repositorio (además de lo de la E1)
1. Cada figura y tabla se regenera con un comando o notebook indicado en el README.
2. Plan de análisis documentado (`docs/plan_de_analisis.md`).
3. Tabla completa de contrastes como archivo de salida (carpeta `tablas/`, por crear).

## Clases de contribución
| Clase | Aporta a Ternium | No puede afirmar |
|---|---|---|
| Descriptiva para la decisión | Dónde una receta común absorbe más heterogeneidad | Que respondan distinto a la misma receta |
| Causal con variación natural en MC4 | Rangos candidatos de consigna para validar | Un óptimo |
| Metodológica / auditoría de etiquetas | Qué indicadores sirven y qué instrumentación falta | Efecto de una consigna |
| Predictiva con encuadre honesto | Criterio para señalar rollos difíciles | Que la importancia de variables mida efectos |

## Escalera de afirmaciones
1. Observamos · 2. Se asocia, ajustando por / Permite anticipar · 3. Es consistente con un efecto, bajo supuestos · 4. Proponemos validar.

## Herramientas del módulo
Regresión logística (diferencias en puntos porcentuales) · árboles poco profundos para auditar etiquetas · RF/boosting solo contra línea base y con validación temporal y agrupada · PR-AUC/F1/recall con defectos raros · redes neuronales rara vez.

## Experimento propuesto (operación evolutiva, Box 1957)
Qué se asigna y a qué unidad (bloques: programa, turno, día) · bloqueo por producto y rango de ancho/espesor · resultado primario y criterio de decisión previos · volumen y tiempo de prueba · riesgos y reglas de paro.

## Datos del Skinpass que pide la guía vs lo que ya hay (archivos SKP_PSQ)
| Pide | Estado |
|---|---|
| Identificador que ligue SKP con MC4 | Sí (97%) |
| Historial de recetas con fechas y ajustes del operador | Parcial (PRAM, sin fechas) |
| Consigna y medido de cada palanca | Parcial (fuerza, bending, tensiones; sin velocidad) |
| Lógica de lazos automáticos | No |
| Planeza de salida continua | No (solo defectos) |
| Calidad posterior automática vs inspección | Sí |
| Campaña de rodillos | Sí (ID y diámetro) |

## Seis tentaciones
Exploración de E1 como resultados · importancia de variables como efecto · exactitud con defecto raro o validación aleatoria · ajustar por temperatura real · "llegan distinto" → "necesitan recetas distintas" · "recomendamos" en lugar de "proponemos validar".
