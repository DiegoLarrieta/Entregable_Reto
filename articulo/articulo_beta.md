# La herencia del Molino Caliente explica poco del esfuerzo y los defectos del Skinpass: evidencia de un año de producción y una propuesta de validación por rollo

**Versión beta · 28 de noviembre de 2026**
Francisco Vaquera Saavedra · Armando Calzada Delgado · María José Vital Castillo · Luis Diego Dominguez Larrieta
Tecnológico de Monterrey · Socio formador: Ternium Pesquería
Revista objetivo: *Quality Engineering* (Taylor & Francis)

> **Fuente:** el título enuncia la afirmación central (Notebooks 04, 05, 08 y 09) y la propuesta (Notebook 08), como pide la guía del artículo ("que diga el hallazgo, no el tema").

---

## Resumen

Ternium Pesquería quiere saber si conviene diferenciar la receta del Skinpass según cómo llega cada rollo del Molino Caliente 4 (MC4). Ligamos 57,099 piezas del Skinpass de 2025 con su rollo del MC4 (97.1 % del total) y preguntamos en qué medida la geometría y la historia térmica heredadas del MC4, frente a las condiciones del propio Skinpass, explican el esfuerzo mecánico (desviación de fuerza y bending frente al preset) y las retenciones por defecto físico, **comparando solo piezas del mismo producto**.

Antes de estimar, una auditoría encontró tres artefactos que inflaban los resultados: una etiqueta de defecto que es una regla sobre la misma medición que la predice, el acoplamiento aritmético entre la desviación y su preset, y la memorización de campañas de rodillo. Corregidos esos artefactos y validando por campaña, la herencia del MC4 agrega como máximo **1.5 puntos de R²** a la predicción del bending y **0 a 4 puntos** a la de la fuerza, con cuatro métodos distintos. Tampoco mejora la detección de defectos. El resultado se sostiene en un periodo reservado (noviembre-diciembre, 9,638 piezas).

La única herencia con un efecto plausible es la **espera entre líneas**: +49 kN de fuerza por desviación estándar de espera (IC 95 % 40-59), con controles negativos que pasan. Las asociaciones entre esfuerzo y defectos no resisten controles negativos, así que su efecto causal no se puede estimar con estos datos.

La mayor oportunidad medible es de planeación: los rollos que exceden el peso de su orden y no se dividen se retienen en el 49 % de los casos (61 % en el periodo reservado), contra 0.3 % si se dividen. Proponemos validarlo con un **ensayo aleatorizado por rollo de 4 semanas** (potencia 0.84 para una reducción del 50 %).

> **Fuente:** cifras de los Notebooks 00 (liga), 04 y 09 (aportes por bloque), 06 (días de espera y controles negativos), 05 y 08 (peso y potencia), 08 (periodo reservado).

---

## 1. Introducción

En una línea de laminación en caliente, el rollo sale con un perfil (corona, acuñamiento) y una historia térmica que el proceso siguiente hereda. El Skinpass de Ternium Pesquería aplica una pasada en frío ligera (~1.5 % de elongación) con una receta que fija, antes de cada pieza, un *preset* de fuerza, bending y tensiones. La pregunta de la planta es si esa receta debería diferenciarse según cómo llega cada rollo del MC4.

La literatura de laminación en caliente con aprendizaje automático predice bien el espesor, el ancho y el perfil a la salida del molino (Ewen et al., 2026), pero eso no responde si **la variación heredada mueve lo que pasa después**. Para eso hace falta separar la herencia de las condiciones del proceso siguiente, y separar la asociación del efecto.

Nuestra propuesta inicial suponía una cadena: *un rollo que llega con más corona o con otra temperatura obliga al Skinpass a esforzarse más, y ese sobreesfuerzo genera defectos*. Este artículo muestra que, con los datos de un año, **esa cadena no se sostiene**. Lo convertimos en motivación y no en disculpa: saber que la herencia del MC4 explica poco le evita a la planta invertir en un sistema de corrección anticipada (*feedforward*) y apunta a dónde sí está la oportunidad.

**Contribuciones**, cada una verificable en Resultados:
1. Una **auditoría de etiquetas y diseños** que identifica tres artefactos que inflan la importancia aparente de las variables (sección 4.1).
2. La **estimación del aporte de cada bloque** dentro de producto, con validación por campaña, robusta a cuatro métodos y confirmada en un periodo reservado (secciones 4.2 a 4.4).
3. Un **efecto plausible** de la espera entre líneas sobre la fuerza, con controles negativos (sección 4.5).
4. Un **protocolo de validación en planta** con análisis de potencia por simulación sobre datos reales (sección 6).

> **Fuente:** pregunta de investigación de la *Propuesta de Validación Metodológica (MC4–Skinpass)*; la hipótesis del mediador es su ajuste crítico 2; el giro se documenta en los Notebooks 04 a 06.

---

## 2. Revisión de literatura

**Aprendizaje automático en laminación en caliente.** Ewen et al. (2026) revisan sistemáticamente la predicción de espesor, ancho y perfil en trenes de laminación en caliente. Señalan que los errores geométricos del rollo solo se corrigen de forma limitada en los procesos posteriores y que los resultados reportados son difíciles de comparar entre estudios por su dependencia de los datos. Nuestro trabajo atiende justo ese paso posterior: no predecir el perfil, sino medir cuánto de él se transmite al Skinpass.

**Modelos físicos del laminado.** La simulación numérica (Ojeda-López et al., 2024) y los modelos de flujo transversal del metal (Chai et al., 2023) explican cómo cambian el ancho y el perfil durante el laminado. Dan el mecanismo, pero no la magnitud con que esa variación pesa frente a otras fuentes en una planta real. Nuestro análisis complementa esa visión con evidencia observacional.

**Inferencia causal en manufactura.** Vuković y Thalmann (2022) y Paredes y Reis (2025) documentan el paso de modelos predictivos a análisis causales en procesos industriales, y advierten que la importancia predictiva no equivale a una palanca de control. Spirtes y Zhang (2016) presentan los fundamentos del descubrimiento causal. Usamos Double Machine Learning (Chernozhukov et al., 2018) y controles negativos (Lipsitch et al., 2010) para poner a prueba las asociaciones.

**El vacío.** La optimización de parámetros con aprendizaje automático no resuelve por sí sola nuestro problema: un modelo puede predecir bien usando variables que no se pueden mover, o reaprendiendo reglas de tolerancia. Hacen falta tres cosas: comparar dentro de producto, auditar las etiquetas y validar fuera de muestra con agrupación por campaña. Ese es el aporte metodológico de este trabajo.

> **Fuente:** PDFs en `docs/papers/` (autores, revista y año extraídos de sus primeras páginas). Las referencias de métodos son estándar. **Todas deben ser leídas por el equipo antes de la versión final.**

---

## 3. Datos y metodología

### 3.1 Población y periodo
- **MC4:** 149,734 rollos y 280 variables (24 archivos quincenales).
- **Skinpass:** 58,786 piezas y 208 variables (12 archivos mensuales). Todo en 2025.
- **Liga:** `Material Entrada` del Skinpass = `Material Salida` del MC4. Liga el 97.1 % de las piezas (57,099) sin multiplicar filas. 49,557 rollos se convierten en piezas; el 16 % de las piezas comparte rollo con otra, así que las piezas de un rollo se mantienen juntas en toda validación.
- **Producto:** norma, grado de salida y rango de espesor. Los análisis comparan piezas del mismo producto.
- **Particiones:**
  - **Entrenamiento:** enero a octubre (47,461 piezas).
  - **Periodo reservado:** noviembre y diciembre (9,638 piezas), sin uso hasta la evaluación final.

> **Fuente:** Notebook 00 (secciones 1 y 3), Notebook 03 (sección 1); `resultados/00_cifras_propuesta.csv`.

### 3.2 Resultados y variables prohibidas
- **Problema A (esfuerzo):** ΔBending = bending real − preset y ΔFuerza = fuerza real − preset, con los valores reales en paralelo. Población: modo Elongación (51,965 piezas), porque en modo Fuerza el preset de fuerza vale 0.
- **Problema B (retenciones):**
  - **B1:** retención por regla automática.
  - **B2:** defecto físico registrado por un inspector, por familias: forma, enrollado, superficie y metalúrgico.
  - **Administrativa:** retenida solo por peso.
- **Prohibidas como predictor:** dictamen, resolución, calidad sugerida, causa, observaciones y todo lo generado después del dictamen.

> **Fuente:** Notebook 00 (secciones 6 y 7), Notebook 01 (sección 8); definiciones aprobadas el 28 de noviembre de 2026 (`docs/plan_de_analisis.md`).

### 3.3 Diagrama causal y conjunto de ajuste
Ordenamos las variables por el momento en que se conocen:
1. Especificación de la orden.
2. Salida del MC4.
3. Entrada al Skinpass.
4. Durante el Skinpass.
5. Dictamen.

Los **confusores** (producto, dimensiones, condiciones del Skinpass al entrar) se ajustan; los **mediadores** (fuerza y bending reales) no se ajustan cuando se busca un efecto total; lo posterior al dictamen nunca entra.

> **Fuente:** Notebook 03 (sección 5, auditoría de fuga) y Notebook 06 (sección B, diagrama).

### 3.4 Diagnóstico de soporte
Antes de estimar medimos cuánta variación existe **dentro de producto** (figura 1):
- **ΔBending:** el 93 % de su varianza queda dentro de producto.
- **Corona:** el 91 %.
- **ΔFuerza:** solo el 16 %; el 84 % es un sesgo del preset por producto.

Las temperaturas de castillo F1-F3 son casi redundantes (ρ ≈ 0.95) y se resumen con T en F1 y la caída F1→F7. Fuera de eso, solo 2 de 190 pares de predictores superan |ρ| = 0.3.

![Figura 1](FIG:01_varianza_grupos)
**Figura 1.** La herencia geométrica del MC4 y el bending varían casi enteros dentro de producto; la fuerza no. Porcentaje de varianza explicado por cada agrupación (R² ajustado, modo Elongación, 51,965 piezas).

> **Fuente:** Notebook 01 (sección 6), Notebook 02 (sección 3); `resultados/01_varianza_entre_dentro.csv`.

### 3.5 Dependencia y validación
- **Agrupación de las piezas:** las piezas de un mismo programa del MC4 comparten rodillos y horno, y las de una misma campaña de rodillo del Skinpass comparten su desgaste.
- **Validación cruzada:** se agrupa por **campaña** (581 campañas en entrenamiento), la versión estricta, y como sensibilidad por programa del MC4.
- **Intervalos:** por bootstrap de programas o con errores agrupados.
- **Prueba final:** el periodo reservado, con criterios de refutación escritos antes de mirarlo.

> **Fuente:** Notebook 03 (sección 6), Notebook 04 (sección 3.1), Notebook 08 (sección 1).

### 3.6 Métodos
- **Modelos anidados:** controles; + MC4; + Skinpass; completo. El aporte se mide con el R² dentro de producto fuera de muestra:
  - con LightGBM (Ke et al., 2017);
  - con modelos lineales mixtos con efecto aleatorio por programa del Skinpass (R² de Nakagawa y Schielzeth, 2013).
- **Problema B:** clasificadores con PR-AUC expresada como mejora sobre la tasa base y regresión logística.
- **Mediación:** g-computación (Imai et al., 2010).
- **Efectos:** Double Machine Learning con ajuste cruzado agrupado (Chernozhukov et al., 2018), con controles negativos.
- **Experimento natural:** efectos fijos de campaña, producto × ancho y operador para el desgaste del rodillo.
- **Robustez:** hiperparámetros ajustados con validación anidada, Ridge, Random Forest y aprendizaje del residuo.

> **Fuente:** Notebooks 04 a 07 y 09.

---

## 4. Resultados

### 4.1 Tres artefactos que inflaban los resultados

| Artefacto | Cómo se ve | Corregido |
|---|---|---|
| **B1 es una regla sobre la propia medición** | Con el error de ancho y de espesor como predictores, B1 se detecta 16× mejor que el azar y el MC4 parece aportar mucho | Sin esas mediciones: 9×, y el MC4 no agrega nada (9.7× → 9.3×) |
| **El Δ contiene al preset** | Con el preset como predictor, el bloque Skinpass "explica" el 73 % de ΔBending | Sin el preset: 24 % con pliegues por programa MC4 |
| **Los diámetros identifican la campaña** | El diámetro es constante en cada campaña: el modelo memoriza su nivel | Validando por campaña: 12 % |

Estos tres artefactos habrían llevado a conclusiones opuestas: que el MC4 explica las retenciones y que la receta del Skinpass explica casi todo el bending.

> **Fuente:** Notebook 05 (sección 1, tautología de B1; `resultados/05_gbdt_anidados.csv`); Notebook 04 (secciones 1.1 y 3.1; `resultados/04_validacion_por_campana.csv`).

### 4.2 El aporte de cada bloque (problema A)

| Validación por campaña (R² dentro de producto, %) | ΔBending | ΔFuerza |
|---|---|---|
| M1 controles | −1.5 | 27.0 |
| M2 + MC4 | −0.2 | 27.5 |
| M3 + Skinpass | 11.5 | 24.5 |
| M4 completo | 12.2 | 29.5 |

- **El MC4 agrega:** ~1 punto a ΔBending y ~0.5 a ΔFuerza.
- **El Skinpass agrega ~12 puntos a ΔBending,** y lo que generaliza a campañas nuevas es el operador: sin él, el bloque cae a −4.8.
- **Los modelos mixtos coinciden:** el R² marginal pasa de 0.15 % a 0.48 % al agregar el MC4 a ΔBending.
- **Agrupaciones dentro de producto:** el programa del Skinpass concentra el 24 % de la varianza de ΔBending y el 32 % de la de ΔFuerza; la campaña, el 25 % y el 21 %; el programa del MC4, el 9 % y el 19 %.

![Figura 2](FIG:04_validacion_campana)
**Figura 2.** Al validar por campaña, el MC4 no mejora la predicción del esfuerzo y la mitad del aporte aparente del Skinpass desaparece. R² dentro de producto fuera de muestra (43,175 piezas, 581 campañas).

> **Fuente:** Notebook 04 (secciones 2.1, 2.2 y 3.1); `resultados/04_lmm_anidados.csv`, `04_validacion_por_campana.csv`.

### 4.3 Las retenciones (problema B)
- **B2 (defecto de inspector):** el mejor modelo llega a ROC-AUC 0.73 y 6.7× sobre el azar (controles: 5.4×). Agregar el MC4 no cambia la detección (5.36× → 5.35×).
- **Defectos de forma** (136 eventos), dentro de producto, en odds ratio:
  - **Modo Fuerza:** 3.9 (IC 2.4-6.1).
  - **Ancho:** 1.6.
  - **Corona del rodillo:** 1.35.
  - **Fuerza real:** 1.31.
  - **Bending real:** 0.63.
  - **Corona del MC4:** 1.09 (IC 0.94-1.26).
- **Modo Fuerza:** tiene 7.9 veces más defectos de forma de lo esperado por su mezcla de productos, pero no sabemos con qué criterio se elige (posible selección).

> **Fuente:** Notebook 05 (secciones 1 y 2); `resultados/05_gbdt_anidados.csv`, `05_logistica_forma.csv`.

### 4.4 Robustez y periodo reservado
- **Robustez a modelo y algoritmo:** el aporte del MC4 a ΔBending es de 0.6 a 1.5 puntos con cuatro métodos (LightGBM con hiperparámetros ajustados por validación anidada, Ridge, Random Forest y aprendizaje del residuo). Corregir el residuo de un modelo sin MC4 usando el MC4 empeora la predicción (11.5 → 10.1). Para ΔFuerza agrega entre 0 y 4 puntos.
- **Excepción exploratoria:** en los dos productos grandes del grado C071TM, el MC4 agrega ~17 puntos.
- **Periodo reservado:** de cinco hallazgos evaluados con criterios previos, cuatro se sostienen. **Se refuta** que el operador mejore la predicción de ΔBending (−6.1 puntos en noviembre-diciembre).

![Figura 3](FIG:09_robustez)
**Figura 3.** Con ningún método la herencia del MC4 agrega más de 1.5 puntos al bending; solo en un grado aporta a la fuerza. Aporte del MC4 en puntos de R² dentro de producto según la prueba (a) y por producto (b).

| Hallazgo | Criterio fijado antes | Noviembre-diciembre | Veredicto |
|---|---|---|---|
| Peso: excede y no se divide | ≥ 20 % y ≥ 10× el resto | 60.8 % vs 0.10 % | Se sostiene |
| El MC4 no mejora ΔBending | Mejora < 2 pts | −1.2 pts | Se sostiene |
| El operador mejora ΔBending | Mejora ≥ 2 pts | −6.1 pts | **Se refuta** |
| Asentamiento del rodillo | IC < 0 | −156 kN (−224 a −88) | Se sostiene |
| Días de espera → ΔFuerza | IC > 0 | +66 kN por DE (51 a 82) | Se sostiene |

**Tabla 1.** Cuatro de cinco hallazgos se sostienen en el periodo reservado. La tasa del primero se consultó al diseñar el protocolo; los otros cuatro se evaluaron por primera vez.

> **Fuente:** Notebook 09 (`resultados/09_*.csv`) y Notebook 08 (sección 2; `resultados/08_evaluacion_prueba.csv`).

### 4.5 Lo causal: un efecto que resiste y asociaciones que no
- **Mediación:** el efecto de la corona sobre los defectos de forma a través de la fuerza es +0.003 puntos porcentuales (IC −0.000 a 0.007), con riesgo base de 0.24 %. Hay una pista débil a través de un menor bending: +0.013 pp (IC 0.003-0.022).
- **Double ML:** la asociación de la fuerza real con los defectos de forma (+0.28 pp por DE sin ajustar) desaparece al ajustar (−0.015 pp; IC −0.21 a 0.18).
- **Controles negativos de la fuerza: fallan.** Su "efecto" sobre defectos metalúrgicos (z = −2.5) y sobre la retención por peso bajo (z = −2.7), que no puede causar, indica confusión no medida.
- **Días de espera:** +49 kN de ΔFuerza por DE (IC 40-59). Sus controles negativos, resultados que ocurrieron antes de la espera, pasan: 0.007 y 0.019 DE.

![Figura 4](FIG:06_dml)
**Figura 4.** Al ajustar, la fuerza deja de asociarse con los defectos y sus controles negativos fallan; solo los días de espera mantienen un efecto. Estimaciones de Double ML (puntos) frente a las ingenuas (cruces), con IC 95 %.

> **Fuente:** Notebook 06 (secciones 1 y 2); `resultados/06_mediacion.csv`, `06_dml.csv`.

### 4.6 El desgaste del rodillo como experimento natural
Comparando piezas de la misma campaña, producto × ancho y operador:
- **Fuerza real:** es 78 kN menor en las primeras 10 piezas (IC −105 a −51) y el preset no lo anticipa (ΔFuerza −98 kN).
- **Bending:** el setup baja el bending ~130 kN a lo largo de la campaña.
- **Defectos de forma:** se duplican en las piezas 61-80 (+0.24 pp; IC 0.06-0.41).
- **Diámetro del rodillo** (rectificados acumulados): no se asocia con nada.
- **Placebo:** pasa para el enrollado, la caída térmica y la espera. La corona sube ligeramente al final de la campaña.

> **Fuente:** Notebook 07; `resultados/07_*.csv`.

### 4.7 La oportunidad de planeación
| Grupo | Retención por PESO (+) | Retención por PESO (−) |
|---|---|---|
| Cabe en la orden | 0.02 % | 1.6 % |
| Excede y **no** se divide | **48.7 %** | 1.0 % |
| Excede y se divide | 0.3 % | 3.9 % |

Dividir los rollos que exceden la orden habría evitado ~790 retenciones (~19,700 t) en enero-octubre, ~24 % de todas las retenidas. Es una estimación optimista, porque supone que esos rollos se podían dividir.

![Figura 5](FIG:08_intervencion_A)
**Figura 5.** La retención por peso ocurre casi solo en rollos que exceden la orden y no se dividen, también en el periodo reservado (a), y un ensayo por rollo la detecta en 4 semanas (b).

> **Fuente:** Notebook 05 (sección 5), Notebook 08 (secciones 2 y 4); `resultados/08_potencia_A_por_rollo.csv`.

---

## 5. Discusión

**Qué significa.** El Skinpass no está "corrigiendo" una herencia variable del MC4: su esfuerzo depende sobre todo del producto (sesgo del preset), de la operación del bloque (programa y campaña) y del estado del rodillo. Ajustar la receta según la geometría del rollo entrante (*feedforward*) tiene, con estos datos, poco que corregir.

**Las limitaciones son hallazgos.**
- *La fuerza alta acompaña a los defectos de forma, pero los controles negativos fallan*: las piezas que se laminan con más fuerza difieren de las demás en algo que no se registra, y **solo un experimento** puede atribuir causa.
- *El modo Fuerza concentra defectos 7.9 veces más de lo esperado, pero no sabemos con qué criterio se elige*: si se usa cuando el rollo ya llega mal, el modo es consecuencia.
- *La ventaja del operador no se transfiere a noviembre-diciembre*: la práctica de bending no es una palanca estable.
- *El bending real se satura cuando el preset pide más de ~150 kN sobre lo normal*: cambiar la consigna no garantiza cambiar lo aplicado.

**Multiplicidad.** Examinamos muchos contrastes. Por eso:
- la afirmación central se apoya en comparaciones de bloque, no en la variable más llamativa;
- los hallazgos clave se evaluaron con criterios fijados antes en un periodo reservado;
- los resultados por tramo de campaña (18 comparaciones) y por producto (4 productos) se reportan como exploratorios.

**Para Ternium, en el peldaño correcto:**
- *Observamos* que la retención por peso se concentra en rollos que exceden la orden.
- *Se asocia* (ajustando por producto) que la espera entre líneas aumenta la fuerza necesaria.
- *Es consistente con un efecto, bajo supuestos*, que la espera cause más fuerza.
- *Proponemos validar* la regla de peso con un ensayo por rollo.

> **Fuente:** síntesis de los Notebooks 04 a 09; escalera de afirmaciones de la guía del artículo.

---

## 6. Conclusiones y propuesta de validación

**Afirmación central.** Una vez controlado el producto, la herencia geométrica y térmica del MC4 explica muy poco del esfuerzo y de los defectos del Skinpass. La mayor oportunidad medible es la asignación de peso.

**Experimento propuesto (operación evolutiva; Box, 1957):**

| Elemento | Definición |
|---|---|
| Unidad | Rollo que excede el peso máximo de su orden |
| Tratamiento | Dividirlo en piezas dentro de [mínimo, máximo] o reasignarlo |
| Asignación | Aleatoria 1:1 en bloques PRAM × semana |
| Resultado primario | % de piezas retenidas por PESO (+) |
| Guardrails | PESO (−), días de espera, órdenes sin rollo, B1 y B2 |
| Regla de paro | PESO (−) más de 5 pp sobre el control o mediana de espera +1 día, dos semanas seguidas |
| Duración | 4 semanas (potencia 0.84 para −50 %, simulada sobre semanas reales) |
| Por qué no por PRAM | Un PRAM concentra el 31 % de los eventos: potencia ≤ 0.11 |

**Segundo cambio, monitoreado:** corregir el preset de fuerza en las primeras 20 piezas de cada campaña (~100 kN y ~25 kN). Un ensayo aleatorizado requeriría ~500 campañas; el monitoreo contra 2025, ~163 campañas (~12 semanas).

**Datos del Skinpass que cerrarían la brecha:** planeza medida de salida, velocidad de línea, criterio de elección del modo Fuerza, correcciones del operador sobre el preset, lógica del control de bending, rugosidad de rodillos y motivo de no dividir un rollo que excede la orden.

> **Fuente:** Notebook 08 (secciones 3 a 6); `resultados/08_tabla_decision.csv`, `08_potencia_*.csv`.

---

## Referencias
*Formato APA. Las marcadas con (†) están en `docs/papers/`. Todas deben verificarse y leerse antes de la versión final.*

- Box, G. E. P. (1957). Evolutionary operation: A method for increasing industrial productivity. *Applied Statistics, 6*(2), 81–101.
- Chai, X., Li, Y., & Shang, F. (2023). Numerical study on metal transverse flow law and model of rolled strip under variable specification in hot rolling. *Metals, 13*, 1876. (†)
- Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W., & Robins, J. (2018). Double/debiased machine learning for treatment and structural parameters. *The Econometrics Journal, 21*(1), C1–C68.
- Ewen, D., Seitz, J., Siedo, H., Prinz, C., & Kuhlenkötter, B. (2026). Hot strip mill process optimization with machine learning: Systematic review and methodical prediction framework based on open-source data. *International Journal of Material Forming, 19*, 69. https://doi.org/10.1007/s12289-026-02022-w (†)
- Imai, K., Keele, L., & Tingley, D. (2010). A general approach to causal mediation analysis. *Psychological Methods, 15*(4), 309–334.
- Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., & Liu, T.-Y. (2017). LightGBM: A highly efficient gradient boosting decision tree. *Advances in Neural Information Processing Systems, 30*.
- Lipsitch, M., Tchetgen Tchetgen, E., & Cohen, T. (2010). Negative controls: A tool for detecting confounding and bias in observational studies. *Epidemiology, 21*(3), 383–388.
- Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting model predictions. *Advances in Neural Information Processing Systems, 30*.
- Nakagawa, S., & Schielzeth, H. (2013). A general and simple method for obtaining R² from generalized linear mixed-effects models. *Methods in Ecology and Evolution, 4*(2), 133–142.
- Ojeda-López, A., Botana-Galvín, M., González-Rovira, L., & Botana, F. J. (2024). Numerical simulation as a tool for the study, development, and optimization of rolling processes: A review. *Metals, 14*, 737. https://doi.org/10.3390/met14070737 (†)
- Paredes, R., & Reis, M. S. (2025). Causality in process systems engineering: Fundamentals, applications, and emerging trends. *Computers and Chemical Engineering, 203*, 109345. (†)
- Spirtes, P., & Zhang, K. (2016). Causal discovery and inference: Concepts and recent methodological advances. *Applied Informatics, 3*, 3. https://doi.org/10.1186/s40535-016-0018-x (†)
- Vuković, M., & Thalmann, S. (2022). Causal discovery in manufacturing: A structured literature review. *Journal of Manufacturing and Materials Processing, 6*(1), 10. (†)

---

## Anexos
- **A. Diccionario de variables derivadas:** `resultados/03_diccionario_derivadas.csv`.
- **B. Preguntas al socio formador y supuestos de trabajo:** `docs/preguntas_socio_formador.md`.
- **C. Plan de análisis con registro de cambios:** `docs/plan_de_analisis.md`.
- **D. Tablas completas de contrastes:** `resultados/04_*.csv` a `09_*.csv`.
- **E. Reproducibilidad:** cada figura y tabla se regenera ejecutando los notebooks 00 a 09 en orden (README).

## Pendiente para la versión final
- Pasar a la plantilla LaTeX de *Quality Engineering*.
- Que el equipo lea y verifique cada referencia.
- Crear la carpeta `tablas/` con la tabla completa de contrastes.
- Escribir el resumen definitivo al final, verificando la prueba de coherencia: el resumen, la última frase de la introducción, los títulos de las figuras y el primer párrafo de conclusiones deben contar la misma historia.
