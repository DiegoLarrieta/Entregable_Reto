# Presentación final (guion, 15 minutos)

Borrador generado a partir de los notebooks 00-09. Versión visual: subpágina «Presentación» del artifact.

## Las tres frases

- Qué es verdad. Comparando piezas del mismo producto, la herencia del MC4 agrega menos de 1.5 puntos de R² a la predicción del bending del Skinpass y nada a la de defectos (43,175 piezas, 581 campañas, validación por campaña, confirmado en noviembre-diciembre). La única herencia con efecto plausible es la espera entre líneas: +49 kN de fuerza por desviación estándar (IC 40-59).
- Qué sigue sin saberse. Si la fuerza, el bending o el modo de operación causan los defectos de forma: no varían de forma independiente (los controles negativos fallan) y no hay planeza medida.
- Qué lo resolvería. Un ensayo por rollo de 4 semanas que valide la regla de peso (~790 retenciones evitables en diez meses), y registrar planeza de salida, criterio del modo Fuerza y correcciones del operador.

## 1 · Portada 0:00
**La herencia del MC4 explica poco del esfuerzo y los defectos del Skinpass; la oportunidad está en el peso**

- Evidencia de un año de producción (2025) y una propuesta de validación por rollo Francisco Vaquera · Armando Calzada · María José Vital · Luis Diego Dominguez · Tec de Monterrey · Socio formador: Ternium Pesquería

*Cómo explicarla:* No leo el título completo: digo la afirmación en una frase y aviso que en 15 minutos vamos a mostrar por qué creerla y qué proponemos probar.

*Fuente:* Título del artículo (sección de título). Guía de la presentación: "el título dice lo que demuestra".

## 2 · El problema y el alcance real 1.5 min
**Ternium pregunta si diferenciar la receta del Skinpass; con datos históricos solo podemos medir cuánto pesa cómo llega el rollo**

- **57,099** piezas del Skinpass ligadas a su rollo (97.1 %)
- **581** campañas de rodillo
- **1,385** programas del MC4
- **12 meses** 2025; nov-dic reservados

*Cómo explicarla:* La pregunta de la planta es de receta. Lo que los datos permiten es medir cuánto de lo que pasa en el Skinpass ya venía del MC4. Doy la muestra efectiva en grupos (campañas, programas), no solo en piezas, porque la evidencia real está en los grupos.

*Fuente:* Notebook 00 (liga y conteos); Notebook 03 (particiones); Notebook 04 (programas y campañas en entrenamiento).

## 3 · La pregunta respondible 1.5 min
**Comparando piezas del mismo producto, ¿cuánto explica la herencia del MC4 frente a la operación del Skinpass?**

- A. Esfuerzo: desviación de bending y de fuerza frente al preset
- B. Retenciones por defecto físico, separadas de las de peso
- Dentro de producto: el producto explica el 84 % de la desviación de fuerza

*Cómo explicarla:* Una línea de población: modo Elongación, 2025. Explico "dentro de producto" con un ejemplo: comparamos una pieza contra otras del mismo producto, no contra todas. Si no, el producto inventa relaciones (de −0.42 a −0.05).

*Fuente:* Propuesta de Validación Metodológica (pregunta); Notebook 01 (84 %); Notebook 02 (−0.42 → −0.05).

## 4 · El hallazgo principal 2 min
**La herencia del MC4 agrega menos de 1.5 puntos de R² a la predicción del bending; la operación del Skinpass, unos 12**

- Figura: `figuras/04_validacion_campana.png`

*Cómo explicarla:* Esta es la diapositiva central. Señalo la barra azul de "+ MC4": casi cero. Digo el número, su unidad (puntos de R² dentro de producto), la validación (por campaña, 581 campañas) y que el periodo reservado lo confirma (−1.2 puntos). Peldaño: "observamos" y "permite anticipar", no "causa".

*Fuente:* Notebook 04 (sección 3.1; resultados/04_validacion_por_campana.csv); Notebook 08 (H2); Notebook 09 (0.6-1.5 puntos con cuatro métodos).

## 5 · El hallazgo principal 1.5 min
**Donde sí está la variación: el bloque de operación y el desgaste del rodillo**

- **24-32 %** de la varianza dentro de producto la comparten las piezas de un mismo programa del Skinpass
- **−78 kN** fuerza en las primeras 10 piezas de una campaña (IC −105 a −51)
- **≈130 kN** que el setup baja el bending a lo largo de la campaña

*Cómo explicarla:* Si no es el MC4, ¿qué es? Lo que comparten las piezas de un mismo bloque del Skinpass, y el rodillo que se asienta en ~20 piezas. Aclaro que el preset no anticipa ese asentamiento: un ajuste fácil.

*Fuente:* Notebook 04 (ICC, sección 2.1); Notebook 07 (experimento natural; resultados/07_posicion_campana.csv).

## 6 · El hallazgo principal 1 min
**La mayor oportunidad no es física: los rollos que exceden el peso de su orden y no se dividen se retienen la mitad de las veces**

- Figura: `figuras/08_intervencion_A.png`

*Cómo explicarla:* Muestro solo el panel izquierdo: 48.7 % en enero-octubre, 60.8 % en noviembre-diciembre, contra 0.3 % si se dividen. Traduzco a volumen: ~790 retenciones y ~19,700 t en diez meses (estimación optimista).

*Fuente:* Notebook 05 (sección 5); Notebook 08 (H1; resultados/08_evaluacion_prueba.csv).

## 7 · Por qué creerlo 1.5 min
**Tres artefactos inflaban los resultados; corregidos, cambian lo que se puede afirmar**

- Una etiqueta de defecto era una regla sobre la medición que la predecía: detección de 16× a 9×
- El Δ contiene al preset: el Skinpass "explicaba" 73 % del bending por aritmética
- El diámetro identificaba la campaña: el aporte del Skinpass bajó de 24 % a 12 %

*Cómo explicarla:* Esto suena a metodología pero es un hallazgo: sin estas correcciones, la conclusión habría sido la contraria (que el MC4 explica las retenciones). Va al frente, como pide la guía.

*Fuente:* Notebook 05 (tautología de B1); Notebook 04 (secciones 1.1 y 3.1).

## 8 · Por qué creerlo 1 min
**Intentamos romper el resultado de cuatro maneras y se sostuvo**

- Figura: `figuras/09_robustez.png`

*Cómo explicarla:* Cuatro métodos (hiperparámetros ajustados, Ridge, Random Forest, residuo) y un periodo reservado con criterios escritos antes: 4 de 5 hallazgos se sostienen. Digo también el que se refutó (el operador) y la excepción (grado C071TM) como exploratoria.

*Fuente:* Notebook 09 (resultados/09_*.csv); Notebook 08 (tabla de evaluación).

## 9 · Qué implica y qué no 2 min
**La fuerza alta acompaña a los defectos de forma, pero con estos datos no se puede saber si los causa**

- Figura: `figuras/06_dml.png`

*Cómo explicarla:* Implica: el feedforward desde el MC4 (intervención B) tiene poco que corregir. No implica: que el MC4 no importe nunca (espera entre líneas: +49 kN por DE, IC 40-59) ni que bajar la fuerza reduzca defectos: los controles negativos fallan, señal de confusión no medida.

*Fuente:* Notebook 06 (resultados/06_dml.csv); Notebook 05 (odds ratios de forma).

## 10 · Qué probar y qué falta medir 2 min
**Proponemos validar la regla de peso con un ensayo por rollo de 4 semanas**

- Unidad: rollo que excede la orden · asignación 1:1 en bloques PRAM × semana
- Potencia 0.84 para −50 % (simulada sobre semanas reales); por PRAM sería 0.11
- Guardrails: retención por peso bajo y días de espera, con regla de paro
- Falta medir: planeza de salida, criterio del modo Fuerza, correcciones del operador, motivo de no dividir

*Cómo explicarla:* Empiezo con "lo que proponemos validar es…". Explico por qué no por familias: un PRAM concentra el 31 % de los eventos. Menciono el segundo cambio (preset al inicio de campaña, 12 semanas monitoreadas) solo si hay tiempo.

*Fuente:* Notebook 08 (secciones 4 a 6; resultados/08_potencia_A_por_rollo.csv).

## 11 · Cierre 1 min
**Lo que es verdad, lo que no sabemos y lo que lo resolvería**

- La herencia del MC4 explica < 1.5 puntos del bending; la espera entre líneas, +49 kN de fuerza por DE
- No sabemos si la fuerza o el modo causan defectos de forma: no hay variación independiente ni planeza medida
- Un ensayo por rollo de 4 semanas y registrar planeza y ajustes del operador lo resolverían

*Cómo explicarla:* Las tres frases, dichas tal cual. Termino en el peldaño 4: proponemos validar.

*Fuente:* Guía de la presentación ("las tres frases"); síntesis de los Notebooks 04 a 09.

## R1 · Respaldo
**El producto explica el 84 % de la desviación de fuerza: es un sesgo del preset por producto (de −32 % a +14 %)**

- Figura: `figuras/02_sesgo_producto.png`

*Cómo explicarla:* Si preguntan por qué la fuerza casi no varía dentro de producto: el preset se equivoca distinto en cada producto, ligado al espesor (ρ = −0.43).

*Fuente:* Notebook 02 (sección 8; resultados/02_sesgo_preset_fuerza_por_producto.csv).

## R2 · Respaldo
**Dentro de producto, la herencia del MC4 y el bending varían; la fuerza, poco**

- Figura: `figuras/01_varianza_grupos.png`

*Cómo explicarla:* Para el diagnóstico de soporte: sí había variación del MC4 que pudiera explicar algo (corona 91 % dentro de producto).

*Fuente:* Notebook 01 (sección 6).

## R3 · Respaldo
**El desgaste dentro de la campaña: asentamiento al inicio y bending programado a la baja**

- Figura: `figuras/07_posicion_esfuerzo.png`

*Cómo explicarla:* Si preguntan por el rodillo: efectos fijos de campaña, producto × ancho y operador; el diámetro (rectificados) no importa.

*Fuente:* Notebook 07.

## R4 · Respaldo
**Evaluación en noviembre-diciembre con criterios escritos antes**

- Peso: 60.8 % vs 0.10 % · se sostiene
- MC4 no mejora el bending: −1.2 pts · se sostiene
- Operador mejora el bending: −6.1 pts · se refuta
- Asentamiento: −156 kN · se sostiene
- Espera → fuerza: +66 kN por DE · se sostiene

*Cómo explicarla:* Declaro que la tasa del peso en el periodo reservado se consultó al diseñar el protocolo.

*Fuente:* Notebook 08 (sección 2).
