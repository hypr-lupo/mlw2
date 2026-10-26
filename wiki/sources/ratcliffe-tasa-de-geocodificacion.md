---
title: La tasa mínima aceptable de geocodificación (Ratcliffe)
type: source
sources: ["2004 - Ratcliffe - Geocodificación del delito y una primera estimación de la tasa mínima aceptable de acierto.pdf"]
autor: [Jerry H. Ratcliffe]
anio: 2004
titulo_original: "Geocoding crime and a first estimate of a minimum acceptable hit rate"
editorial: International Journal of Geographical Information Science, 18(1), 61-72
idioma_fuente: en
apa: "Ratcliffe, J. H. (2004). Geocoding crime and a first estimate of a minimum acceptable hit rate. *International Journal of Geographical Information Science, 18*(1), 61-72. https://doi.org/10.1080/13658810310001596076"
verificacion_bibliografica: verificado
cluster: medicion-y-metodo
curso: [s1-2]
procedencia: fuentes
estado: revisado
truncado: false
creado: 2026-10-26
actualizado: 2026-10-26
---

# La tasa mínima aceptable de geocodificación (Ratcliffe)

**Referencia APA 7.** Ratcliffe, J. H. (2004). Geocoding crime and a first estimate of a minimum acceptable hit rate [La geocodificación del delito y una primera estimación de la tasa mínima aceptable de acierto]. *International Journal of Geographical Information Science, 18*(1), 61-72. https://doi.org/10.1080/13658810310001596076

> [!info] Qué es
> El artículo que propone el 85 % como tasa mínima de geocodificación. Se leyó completo. La p. 1 del PDF es una portada de la editorial, y la página impresa es la del PDF más 59. No es «The hotspot matrix», el otro Ratcliffe de 2004. Análisis de fase 1: `despliegue/fase1/2026-10-26-ratcliffe-tasa-de-geocodificacion.md`.

## Tesis

Pocos analistas logran geocodificar el 100 % de los delitos. La pregunta es qué tasa basta para que el mapa sea confiable [^ext-1]. La respuesta es una primera estimación: 85 % [^ext-1]. Ver [[analisis-espacial-del-delito]].

## Por qué se pierden direcciones

La geocodificación convierte una dirección en coordenadas [^ext-1]. Las bases policiales rara vez verifican las direcciones al registrarlas [^ext-2]. Errores comunes [^ext-3]:

- nombre de calle mal escrito o abreviatura que el sistema no reconoce
- prefijo o tipo de calle equivocado
- dirección imposible o vacía
- un lugar conocido sin dirección, como un cine
- texto previo, como «50 metros al este de»

Las calles nuevas que todavía no están en la base de calles tampoco se geocodifican [^ext-4].

## El método

Una simulación de Monte Carlo. Se parte de un mapa completo, agregado a manzanas censales. Se quita al azar el 1 % de los puntos por vez y se compara con el mapa completo [^ext-5]. La prueba es la U de Mann-Whitney al nivel 0,01. Cada conjunto se repite 250 veces [^ext-6].

Usa cinco conjuntos de Nueva Gales del Sur, de 783 a 1.362 registros, en 144 a 261 manzanas. Mezclan todo el delito, robo de vehículos, daños y robo en viviendas [^ext-7].

## El resultado

El mínimo aceptable es la media más dos desviaciones estándar, redondeada hacia arriba. Va de 78 a 85 % según el conjunto [^ext-8]. Con 85 %, el mapa no difiere del completo en al menos el 95 % de los casos [^ext-8].

## Cita

> "85% as a first estimate of a minimum reliable geocoding rate" [85 % como primera estimación de una tasa mínima confiable de geocodificación]
> — Ratcliffe (2004, p. 61)

## Alcance y límites

**Pérdidas al azar.** La simulación quita puntos al azar. Pero los errores reales pueden agruparse, por ejemplo, en un conjunto de calles nuevas o alrededor de un hito sin dirección. En ese caso, el mínimo sube [^ext-9].

**Manzanas censales.** El 85 % se estimó con mapas agregados a manzanas. No se probó a escala de segmento de calle ni de dirección [^inf-1].

**Una primera estimación.** El objetivo sigue siendo el 100 %. Con 85 %, de 10.000 delitos quedan fuera hasta 1.500 [^ext-10]. El analista debe revisar los registros perdidos en busca de un patrón y depurar las direcciones [^ext-10].

**Unidad modificable.** Agregar en polígonos trae el problema de la unidad espacial modificable [^ext-11].

## Conceptos tratados

- [[analisis-espacial-del-delito]] — geocodificación y tasa de acierto

## Conexiones con otras fuentes

- [[weisburd-ley-de-concentracion]] — usa este umbral para sus ocho ciudades
- [[chainey-concentracion-america-latina]] — usa este umbral para sus 42 ciudades
- [[vozmediano-criminologia-ambiental]] — cita el otro Ratcliffe de 2004

## Encuadre curricular

Capa posterior y reversible. Vaciarla no cambia nada de lo anterior.

Entró el 26-10-2026 en la tanda S1.2d, por decisión del autor, porque el diseño de investigación aplicada de S1.2 la cita. Verificación contra el borrador de esa fecha:

- La referencia coincide con el original.
- La sección 9 fija una tasa mínima de 85 % con esta cita. La cifra está en el original (pp. 61 y 69).
- Dos condiciones del original pesan para el diseño. El 85 % se estimó con manzanas censales, no con segmentos. Y supone pérdidas al azar: si las direcciones fallidas se agrupan en un lugar, hace falta más (pp. 69-70).

---

[^ext-1]: **Extraído** — p. 61.
[^ext-2]: **Extraído** — p. 65.
[^ext-3]: **Extraído** — pp. 65-66, adaptado de Harries (1999).
[^ext-4]: **Extraído** — p. 66.
[^ext-5]: **Extraído** — pp. 66-67.
[^ext-6]: **Extraído** — pp. 68-69.
[^ext-7]: **Extraído** — p. 68, tabla 1.
[^ext-8]: **Extraído** — p. 69, tabla 2.
[^ext-9]: **Extraído** — pp. 69-70.
[^ext-10]: **Extraído** — p. 70.
[^ext-11]: **Extraído** — p. 64, sobre Openshaw (1984).
[^inf-1]: **Inferido** (confianza 0.85) — el método agrega a manzanas censales (pp. 66-69) y no prueba otras unidades. Con unidades más pequeñas, cada pérdida pesa más en el conteo de cada unidad.
