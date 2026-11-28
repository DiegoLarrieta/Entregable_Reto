# Plan de análisis

Se fija ANTES de correr los modelos. Cualquier cambio se anota abajo con fecha y motivo.
Base: *Propuesta de Validación Metodológica (MC4–Skinpass)* y diagnóstico del 2026-11-27.

| Elemento | Decisión actual | Estado |
|---|---|---|
| Población A (esfuerzo mecánico) | Piezas del Skinpass 2025 en **modo Elongación** (53,260), ligadas a su rollo de MC4 | Fijo (ver nota 2) |
| Población B (retenciones) | Todas las piezas del Skinpass 2025 ligadas a su rollo de MC4 | Propuesta |
| Unidad de análisis | Pieza del Skinpass; las piezas de un mismo rollo comparten el bloque MC4 → agrupar por rollo | Fijo |
| Resultado A | **ΔBending** y **ΔFuerza** (con su valor Real en paralelo, nota 3). ΔFuerza siempre con efecto fijo de producto (el producto explica 84 % de su varianza). Tensiones como secundarias (casi no se desvían) | Fijo (01) |
| Resultado B | Administrativa = retenida solo por defectos de PESO (D1 y D3 como sensibilidad). **B1** = retención por regla automática o por medición registrada por inspector (ancho, espesor, temperatura), sin usar como predictor la medición que define la regla. **B2** = defecto físico de inspector, por familias: forma, superficie y manejo, enrollado, metalúrgico (bordes sin eventos suficientes) | Fijo (aprobado 2026-11-28) |
| Regla de corona | Relativa al espesor en lugar de 0-300 µm fijo (en lámina de 6-8 mm el 10.6 % de las coronas cae entre 300 y 1,000 µm) | Por fijar en 03 |
| Espesor Final / Taper Teórico | `Espesor Final` es el espesor nominal del producto final (control, no herencia). `Taper Teórico` vale siempre 0: ΔTaper = `Taper Medido` | Fijo (01) |
| Bloque MC4 | Geometría (corona, acuñamiento, taper, ancho, espesor) y térmica (acabado, enrollado, castillos) | Propuesta |
| Bloque SKP | Rodillos (diámetros, coronas, campaña) y operación (modo, medidor, usuario) | Propuesta |
| Controles | Grado Salida, Norma, PRAM, espesor, ancho, Dividido, Es Reproceso | Propuesta |
| Agrupaciones | Programa MC4 (herencia del MC4) y Programa SKP / campaña de rodillo (condiciones del SKP), **cruzados**; Colada como efecto aleatorio solo si captura varianza | Fijo |
| Prohibidas | Dictamen, Resolución, Calidad Sugerida, Defecto*, Causa*, Observaciones*, Muestreado, Empaque Cumple, Siguiente Acción/Proceso, fechas de registro | Fijo |
| Tautologías | No predecir un defecto automático con la medición que lo define (p. ej., ANCHO con el ancho del MC4, PESO con el peso) | Fijo |
| Exclusiones | Corona fuera de 0 a 300 µm (→ faltante); piezas sin llave MC4 | Fijo |
| Validación | GroupKFold por Programa MC4 y por campaña de rodillo SKP; corte temporal por trimestre | Propuesta |
| Comprobaciones | Control negativo, estabilidad por trimestre, robustez a umbrales, sensibilidad a la definición de "administrativa" | Propuesta |

## Decisiones del Notebook 02 (2026-11-28)
- Correlaciones e interpretaciones siempre **dentro de producto**; las crudas no se interpretan.
- Temperaturas de castillo resumidas con T en F1 y caída F1→F7 (F1-F4 redundantes entre sí).
- Desgaste: una sola medida (piezas en campaña) y **siempre con el ancho como control**: la subida de ΔFuerza en la campaña era sobre todo el orden de anchos del programa.
- **PCA no se usa en los modelos** (no comprime ni mejora la asociación con la respuesta).
- Mediador: probar también **fuerza real** (corona → fuerza real → defecto de forma), no solo ΔBending.
- `Días MC4 → SKP` entra como variable de interés para el problema A (ρ = 0.23 con ΔFuerza); no se usa para B1 ni administrativa, donde puede ser consecuencia.
- **Intervención candidata D:** recalibración del preset de fuerza por producto (sesgo de −32 % a +14 %, ligado al espesor). Revisar antes el posible tope en −40 %.

## Decisiones del Notebook 04 (2026-11-28)
- **El preset no es predictor de su propio Δ** (acoplamiento matemático: Δ = real − preset). Solo entra, como bloque "Setup", en los modelos de los valores reales.
- El bloque Skinpass se valida también con **pliegues por campaña**: los diámetros identifican la campaña y sin esa validación su aporte se duplica.
- Respuesta parcial a la tesis A: dentro de producto el MC4 aporta < 1 punto de R² fuera de muestra a ΔBending y ~1-2 a ΔFuerza. El programa y la campaña del Skinpass concentran 21-32 % de la varianza; el operador explica ~12 % de ΔBending y es lo que generaliza.
- El bending real se satura cuando el preset pide más de ~150 kN sobre lo normal del producto: la intervención B tiene techo.
- **Intervención candidata E:** estandarizar la práctica de operación del bending (dos operadores con ΔBending ~140 kN distinto).

## Decisiones del Notebook 05 (2026-11-28)
- **B1 nunca usa como predictor la medición que define su regla** (error de ancho, de espesor, de enrollado, elongación) ni los días de espera. Con ellas la mejora sobre el azar sube de 9× a 16× por tautología.
- Respuesta parcial a la tesis B: dentro de producto y con validación por campaña, el MC4 no mejora la predicción de B1 ni de B2. Forma se asocia con modo Fuerza (OR 3.9), fuerza real (OR 1.3), bending real (OR 0.63) y corona del rodillo (OR 1.35).
- Modo Fuerza: 7.9 veces más defectos de forma de lo esperado por producto; tratar como posible selección.
- Intervención A: ~790 retenciones por PESO (+) y ~19,700 t evitables en enero-octubre (estimación optimista).
- Operador sin patrón claro en defectos: la intervención E no tiene evidencia de calidad.

## Decisiones del Notebook 06 (2026-11-28)
- **Mediación MC4 → fuerza → forma: nula** (+0.003 pp). Pista débil por la vía del bending (+0.013 pp), no confirmable con datos históricos.
- **Controles negativos fallan** para fuerza y bending (efectos imposibles sobre metalúrgico y PESO −): hay confusión no medida. No se hacen afirmaciones causales sobre defectos con datos históricos.
- **Días de espera → ΔFuerza:** +49 kN por DE (IC 40-59), con controles negativos que pasan. Único efecto causal plausible de la herencia del MC4 sobre el esfuerzo.

## Notas sobre el preset (no tenemos respuesta de Ternium; ver `preguntas_socio_formador.md`)
1. **Qué es Δ.** El preset lo fija el control de *setup* antes de procesar la pieza; durante el proceso el control dinámico ajusta la fuerza para alcanzar la elongación. Por eso Δ = Real − Preset se interpreta como **lo que el modelo de setup no anticipó para esa pieza**. Si variables del MC4 explican Δ, el setup no está usando información disponible al llegar el rollo (argumento para el feedforward, intervención B).
2. **Ceros del preset.** El preset de fuerza en 0 corresponde al modo Fuerza (RCO), que se excluye del Resultado A. El preset de bending en 0 es una **consigna neutra válida** (el bending tiene signo y el real no es 0 cuando el preset lo es) y se conserva.
3. **No interpretar el nivel de Δ.** La fuerza real queda ~18% debajo del preset en mediana; puede ser un margen intencional del setup. Se interpreta la **variación de Δ entre piezas dentro de un mismo producto**, no su promedio.
4. **No sabemos qué variables usa el setup.** Si ya usara la corona, su efecto sobre Δ saldría cerca de cero aunque la corona sí mueva la fuerza. Por eso se modelan en paralelo **Δ y el valor Real**, y se comparan:
   - MC4 explica Real y Δ → el setup no captura la herencia del MC4.
   - MC4 explica Real pero no Δ → el setup ya la captura.
   - MC4 no explica ninguno → la herencia del MC4 no mueve el esfuerzo.

## Registro de cambios
- 2026-11-28: Notebook 06 (mediación por g-computación y Double ML propio con ajuste cruzado agrupado y controles negativos).
- 2026-11-28: Notebook 05 (retenciones). Se corrige la tautología de B1; GBDT anidados M1-M5 con validación por campaña; logística de forma; O/E por modo y operador; oportunidad de la intervención A.
- 2026-11-28: Notebook 04 (modelos del esfuerzo). Se corrige el acoplamiento Δ-preset, se agrega validación por campaña y el análisis por operador.
- 2026-11-28: Notebook 03. Base analítica en `data/analitica/base_analitica.parquet`; prueba final = piezas desde el 2025-11-01; 5 pliegues por Programa MC4; recorte p0.5-p99.5 de entrenamiento con bandera; enrollado frío (< −100 °C) como evento; faltantes sin imputar en la base.
- 2026-11-26: se agregan los 12 archivos del Skinpass y se propone usar fuerza/bending del Skinpass como resultado.
- 2026-11-28: se aprueban la definición de administrativa (solo PESO) y la división B1/B2. Con el EDA (Notebook 01): ΔFuerza con efecto de producto obligatorio, ΔBending como respuesta con más variación dentro de producto, tensiones secundarias, regla de corona relativa, reclasificación de Espesor Final.
- 2026-11-27: se adopta la propuesta de validación metodológica. Población A en modo Elongación; Δ y Real en paralelo; Programa MC4 y SKP como agrupaciones cruzadas; notas sobre el preset.
