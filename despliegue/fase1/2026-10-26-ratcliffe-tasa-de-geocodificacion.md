---
fuente: "2004 - Ratcliffe - Geocodificación del delito y una primera estimación de la tasa mínima aceptable de acierto.pdf"
ficha_destino: wiki/sources/ratcliffe-tasa-de-geocodificacion.md
cumulo: Medición e inseguridad (alta del 26-10-2026)
prioridad: sin asignar
tanda: S1.2d, por delante de la 4a
fase: 1
fecha: 2026-10-26
estado: materializado
truncado: false
caracteres_extraidos: 40213
---

# Fase 1 — Ratcliffe (2004), la tasa mínima aceptable de geocodificación

**Fuente:** `2004 - Ratcliffe - Geocodificación del delito y una primera estimación de la tasa mínima aceptable de acierto.pdf`

Análisis de sólo lectura, persistido antes de escribir ninguna página. Llegó como `ratcliffe2004.pdf`
el 26-10-2026 y se renombró a la convención.

## Identificación

Ratcliffe, J. H. (2004). Geocoding crime and a first estimate of a minimum acceptable hit rate.
*International Journal of Geographical Information Science, 18*(1), 61-72.
https://doi.org/10.1080/13658810310001596076

- **Paginación.** La p. 1 del PDF es una portada de Taylor & Francis. Página impresa = página del
  PDF más 59.
- **Lectura completa.** `truncado: false`.
- **Cuál de los dos Ratcliffe.** Es el trabajo sobre la tasa de acierto. No es «The hotspot matrix»,
  que cita Vozmediano y San Juan.

## 1. Entidades

Policía de Nueva Gales del Sur y sus paneles de revisión de operaciones (pp. 62-63).

## 2. Conceptos

- **Geocodificación.** Convertir una dirección en coordenadas (p. 61).
- **Tasa de acierto.** El porcentaje de registros que se geocodifican con éxito (p. 62).
- **Simulación de Monte Carlo.** Repetir muchas veces un proceso aleatorio para estimar una
  distribución (pp. 66-68).
- **Depuración de direcciones.** Una pasada previa que corrige errores comunes (p. 70).

## 3. Afirmaciones (todas extraídas)

- Lograr el 100 % de geocodificación es raro. Pocos analistas lo consiguen (p. 61).
- Errores comunes de dirección: nombre mal escrito, prefijo equivocado, abreviatura desconocida,
  dirección imposible, lugar conocido sin dirección, texto previo («50 m al este de») (p. 65).
- Las calles nuevas que todavía no están en la base de calles tampoco se geocodifican (p. 66).
- Método: se quita al azar el 1 % de los puntos por vez, se agrega a manzanas censales y se compara
  con el mapa completo mediante la prueba U de Mann-Whitney al 0,01. Cada conjunto se repite 250
  veces (pp. 66-69).
- Cinco conjuntos de Nueva Gales del Sur, de 783 a 1.362 registros, en 144 a 261 manzanas (tabla 1,
  p. 68).
- El mínimo aceptable se fija en la media más dos desviaciones estándar. Va de 78 a 85 %. Con 85 %, el
  mapa no difiere del completo en al menos el 95 % de los casos (tabla 2, p. 69).
- Límite: la simulación quita puntos al azar. Pero los errores reales pueden agruparse en un lugar,
  como un conjunto de calles nuevas o un hito sin dirección. En ese caso, el mínimo sube (pp. 69-70).
- Es una primera estimación. El objetivo sigue siendo el 100 %. Con 85 %, de 10.000 delitos quedan
  fuera hasta 1.500 (p. 70).
- El analista debe revisar los registros no geocodificados en busca de un patrón (p. 70).
- Menciona el problema de la unidad espacial modificable al agregar en polígonos (p. 64).

## 4. Vigencia

Método. No caduca, pero es una primera estimación con datos de 2002.

## 5. Conexiones y tensiones

- **Resuelve el `amb-1` de [[vozmediano-criminologia-ambiental]] y de
  [[analisis-espacial-del-delito]].** La tasa de 85 % viene de este trabajo.
- **Con Weisburd (2015) y Chainey y otros (2019).** Ambos usan el 85 % de Ratcliffe como umbral.
- **Unidad de agregación.** El 85 % se estimó con mapas agregados a manzanas censales. No se probó a
  escala de segmento de calle.

## 6. Recomendación

Ficha `ratcliffe-tasa-de-geocodificacion`, clúster `medicion-y-metodo`. Actualizar
[[analisis-espacial-del-delito]]: cerrar el `amb-1`, sumar el método, el umbral y sus dos límites
(azar y unidad).
