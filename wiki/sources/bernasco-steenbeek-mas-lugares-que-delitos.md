---
title: Más lugares que delitos (Bernasco y Steenbeek)
type: source
sources: ["2017 - Bernasco y Steenbeek - Más lugares que delitos, implicancias para evaluar la ley de concentración del delito en el lugar.pdf"]
autor: [Wim Bernasco, Wouter Steenbeek]
anio: 2017
titulo_original: "More places than crimes: Implications for evaluating the law of crime concentration at place"
editorial: Journal of Quantitative Criminology, 33(3), 451-467
idioma_fuente: en
apa: "Bernasco, W. y Steenbeek, W. (2017). More places than crimes: Implications for evaluating the law of crime concentration at place. *Journal of Quantitative Criminology, 33*(3), 451-467. https://doi.org/10.1007/s10940-016-9324-7"
verificacion_bibliografica: verificado
cluster: medicion-y-metodo
curso: [s1-2]
procedencia: fuentes
estado: revisado
truncado: false
creado: 2026-10-26
actualizado: 2026-10-26
---

# Más lugares que delitos (Bernasco y Steenbeek)

**Referencia APA 7.** Bernasco, W. y Steenbeek, W. (2017). More places than crimes: Implications for evaluating the law of crime concentration at place [Más lugares que delitos: implicancias para evaluar la ley de concentración del delito en el lugar]. *Journal of Quantitative Criminology, 33*(3), 451-467. https://doi.org/10.1007/s10940-016-9324-7

> [!info] Qué es
> Un artículo de método sobre cómo medir la concentración del delito. Se leyó completo. La página impresa es la del PDF más 450. Publicado en línea en 2016, en acceso abierto. Las fórmulas salen dañadas en la extracción y se reconstruyeron desde el texto. Análisis de fase 1: `despliegue/fase1/2026-10-26-bernasco-steenbeek-mas-lugares-que-delitos.md`.

## Tesis

La concentración del delito debe reportarse con la curva de Lorenz y resumirse con el coeficiente de Gini [^ext-1]. Cuando hay menos delitos que lugares, las dos medidas sobrestiman la concentración. Los autores proponen versiones generalizadas que corrigen ese sesgo [^ext-1]. Ver [[analisis-espacial-del-delito]].

## El problema

**Sin estándar.** Los estudios reportan enunciados como «el Y % del delito ocurre en el X % de los lugares», con cortes elegidos a voluntad. Eso dificulta comparar y probar la ley de concentración [^ext-2].

**Datos escasos.** Con segmentos de calle, y más aún con direcciones, suele haber menos delitos que lugares [^ext-3]. Un delito no se divide entre dos lugares. Entonces la igualdad perfecta es imposible, y algunos lugares quedan sin delito por pura aritmética [^ext-4].

**Un ejemplo.** Diez lugares con diez delitos, uno en cada uno, dan un Gini de 0. Si se quita al azar la mitad de los delitos, el Gini sube a 0,50, sin que cambie nada en el proceso de fondo [^ext-4].

**No es nuevo.** Sherman y otros (1989) ya lo notaron. Los robos estaban en el 2,2 % de las direcciones, pero el máximo posible, con un robo por dirección, era 3,6 % [^ext-5].

## La corrección

La curva de Lorenz no cambia. Cambia la línea de referencia: ya no es la igualdad perfecta, sino la máxima igualdad posible con esos datos [^ext-6]. El **Gini generalizado** se calcula así [^ext-7]:

G' = máx(n/c, 1) · (G − 1) + 1

donde n es el número de lugares, c el de delitos y G el Gini original. Cuando c ≥ n, G' es igual a G. Cuando c < n, corrige hacia abajo [^ext-7]. La varianza puede estimarse con jackknife [^ext-8].

## La Haya

La Haya tiene 14.375 segmentos [^ext-9]. En 2007-2009 hubo 37.121 robos con fuerza y 7.135 agresiones. El 50 % de cada uno cae en el 8,84 % y el 4,70 % de los segmentos [^ext-9]. Con un solo año, aun los robos con fuerza serían menos que los segmentos [^ext-10].

El Gini original da 0,73 para los robos y 0,86 para las agresiones. El generalizado da 0,73 y 0,72 [^ext-11]. La agresión parecía más concentrada, pero era un efecto de su rareza [^ext-12].

## Implicancias

**También los porcentajes.** El sesgo afecta los enunciados de porcentaje acumulado, no sólo la curva y el Gini [^ext-13].

**Volumen y concentración.** A la policía le importa más el volumen que la concentración relativa. Las medidas relativas ocultan diferencias de volumen [^ext-14].

**Reformular la ley.** La concentración observada, relativa a la que habría con la máxima dispersión posible, caería en una banda estrecha [^ext-15].

## Cita

> "the rareness of the crime makes assault seem to be more concentrated" [la rareza del delito hace que la agresión parezca más concentrada]
> — Bernasco y Steenbeek (2017, p. 463)

## Alcance y límites

**Weisburd no tenía el problema.** Sus ciudades tenían más delitos que segmentos [^ext-16]. Lo tendrán los estudios con unidades pequeñas, periodos cortos o delitos específicos [^ext-16].

**Poca imagen con datos muy escasos.** Si los lugares son veinte veces los delitos, la curva generalizada casi no se ve. El Gini generalizado sigue sirviendo [^ext-17].

## Conceptos tratados

- [[analisis-espacial-del-delito]] — curva de Lorenz, Gini y Gini generalizado
- [[puntos-calientes]] — la reformulación de la ley de concentración

## Conexiones con otras fuentes

- [[weisburd-ley-de-concentracion]] — la ley que el artículo propone medir mejor
- [[chainey-concentracion-america-latina]] — cita este artículo, pero no aplica la corrección

## Encuadre curricular

Capa posterior y reversible. Vaciarla no cambia nada de lo anterior.

Entró el 26-10-2026 en la tanda S1.2d, por decisión del autor, porque el diseño de investigación aplicada de S1.2 la cita. Verificación contra el borrador de esa fecha:

- La referencia coincide con el original.
- La sección 9 dice que el Gini generalizado corrige el sesgo cuando hay más segmentos que registros. Es correcto (pp. 451 y 458-459).
- El artículo agrega algo que el diseño no recoge. El mismo sesgo afecta el porcentaje de segmentos que acumula el 50 % (p. 463). Es el indicador del criterio a de la decisión 14, calculado por año y por tipo de delito.

---

[^ext-1]: **Extraído** — p. 451.
[^ext-2]: **Extraído** — p. 452.
[^ext-3]: **Extraído** — pp. 452-453.
[^ext-4]: **Extraído** — p. 457, figura 2.
[^ext-5]: **Extraído** — p. 457, sobre Sherman y otros (1989).
[^ext-6]: **Extraído** — p. 458.
[^ext-7]: **Extraído** — pp. 458-459, ecuación 4.
[^ext-8]: **Extraído** — p. 460.
[^ext-9]: **Extraído** — p. 461.
[^ext-10]: **Extraído** — p. 461, nota 7.
[^ext-11]: **Extraído** — p. 462.
[^ext-12]: **Extraído** — pp. 462-463.
[^ext-13]: **Extraído** — p. 463.
[^ext-14]: **Extraído** — p. 463.
[^ext-15]: **Extraído** — pp. 463-464.
[^ext-16]: **Extraído** — p. 453.
[^ext-17]: **Extraído** — p. 463.
