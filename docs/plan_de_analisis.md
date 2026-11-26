# Plan de análisis (borrador)

Se fija ANTES de correr el modelo principal. Cualquier cambio se anota abajo con fecha y motivo.

| Elemento | Decisión actual | Estado |
|---|---|---|
| Población | Rollos que pasaron por el Skinpass de Pesquería en 2025, modo SKP, sin reprocesos, primera pieza | Propuesta |
| Unidad de análisis | Rollo; agrupamiento por Programa de MC4 | Propuesta |
| Resultado | Fuerza real del Skinpass (alternativa: Fuerza real − Preset) | Por confirmar con profesor |
| Exposición / predictores | Corona relativa, acuñamiento, temperaturas de MC4 | Propuesta |
| Conjunto de ajuste | Elongación, espesor, ancho, grado | Propuesta |
| Prohibidas | Dictamen, Resolución, Calidad Sugerida, Defecto*, Causa*, Observaciones*, fechas de registro (`src/ternium.py`) | Fijo |
| Exclusiones | Corona fuera de 0 a 300 µm; filas sin llave MC4 | Fijo |
| Validación | GroupKFold por Programa MC4; también corte temporal por trimestre | Propuesta |
| Comprobaciones | Control negativo, estabilidad por trimestre, robustez a umbrales de depuración | Propuesta |

## Registro de cambios
- 2026-11-26: se agregan los 12 archivos del Skinpass y se propone usar fuerza/bending del Skinpass como resultado.
