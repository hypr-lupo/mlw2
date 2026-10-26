---
fuente: "2017 - Bernasco y Steenbeek - Más lugares que delitos, implicancias para evaluar la ley de concentración del delito en el lugar.pdf"
ficha_destino: wiki/sources/bernasco-steenbeek-mas-lugares-que-delitos.md
cumulo: Medición e inseguridad (alta del 26-10-2026)
prioridad: sin asignar
tanda: S1.2d, por delante de la 4a
fase: 1
fecha: 2026-10-26
estado: materializado
truncado: false
caracteres_extraidos: 45751
---

# Fase 1 — Bernasco y Steenbeek (2017), más lugares que delitos

**Fuente:** `2017 - Bernasco y Steenbeek - Más lugares que delitos, implicancias para evaluar la ley de concentración del delito en el lugar.pdf`

Análisis de sólo lectura, persistido antes de escribir ninguna página. Llegó como
`s10940-016-9324-7.pdf` el 26-10-2026 y se renombró a la convención.

## Identificación

Bernasco, W. y Steenbeek, W. (2017). More places than crimes: Implications for evaluating the law of
crime concentration at place. *Journal of Quantitative Criminology, 33*(3), 451-467.
https://doi.org/10.1007/s10940-016-9324-7. Publicado en línea el 20-09-2016, en acceso abierto con
licencia CC BY 4.0.

- **Paginación.** Página impresa = página del PDF más 450.
- **Fórmulas.** Las ecuaciones salen dañadas en la extracción. Se reconstruyen desde el texto y el
  ejemplo numérico (pp. 456-459).
- **Lectura completa.** `truncado: false`.

## 1. Entidades

La Haya, con 14.375 segmentos de calle (p. 461).

## 2. Conceptos

- **Curva de Lorenz.** Relaciona el porcentaje acumulado de delitos con el porcentaje acumulado de
  lugares, ordenados de más a menos delito. Cada punto es un enunciado «el Y % del delito ocurre en
  el X % de los lugares» (p. 454). → [[analisis-espacial-del-delito]].
- **Coeficiente de Gini.** Resume la concentración entre 0 y 1 (p. 456).
- **Datos escasos.** Hay menos delitos que lugares (c < n). Es común con segmentos y más aún con
  direcciones (p. 452).
- **Línea de máxima igualdad.** Con c < n, la igualdad perfecta es imposible, porque un delito no se
  divide. La referencia pasa a ser la máxima dispersión posible (pp. 457-458).
- **Gini generalizado (G').** G' = máx(n/c, 1) · (G − 1) + 1. Corrige hacia abajo cuando c < n e
  iguala al original cuando c ≥ n (pp. 458-459).

## 3. Afirmaciones (todas extraídas)

- La literatura no tiene un estándar para medir y reportar la concentración (pp. 451-452).
- Con datos escasos, la curva de Lorenz y el Gini sobrestiman la concentración (p. 452).
- Weisburd (2015) no tenía ese problema: todas sus ciudades tenían más delitos que segmentos. Los
  estudios futuros, con unidades pequeñas, periodos cortos y delitos específicos, sí lo tendrán
  (p. 453).
- Ejemplo: 10 lugares y 10 delitos dan G = 0. Si se quita al azar la mitad, G = 0,50 sin que cambie
  el proceso de fondo (p. 457).
- Sherman y otros (1989) ya lo notaron: los robos estaban en el 2,2 % de las direcciones, frente a un
  máximo posible de 3,6 % (p. 457).
- La Haya, 2007-2009: 37.121 robos con fuerza y 7.135 agresiones. El 50 % cae en el 8,84 % y el 4,70 %
  de los segmentos (p. 461). Con un solo año, aun los robos con fuerza serían menos que los segmentos
  (nota 7, p. 461).
- Gini original: 0,73 y 0,86. Gini generalizado: 0,73 y 0,72. La agresión parecía más concentrada,
  pero era un efecto de su rareza (pp. 462-463).
- El problema afecta también los enunciados de porcentaje acumulado, no sólo la curva y el Gini
  (p. 463).
- La varianza del Gini puede estimarse con jackknife (p. 460).
- A los usuarios operativos les importa más el volumen que la concentración relativa (p. 463).
- Proponen reformular la ley respecto de la concentración bajo la máxima dispersión posible
  (pp. 463-464).

## 4. Vigencia

Método. No caduca.

## 5. Conexiones y tensiones

- **Con Weisburd (2015).** Lo critican en la medición, no en el fondo.
- **Con Chainey y otros (2019).** Chainey los cita, pero usa las bandas de Weisburd sin corregir, y
  en varias combinaciones de ciudad y delito hay menos delitos que segmentos. → tensión: parte de la
  mayor concentración latinoamericana podría deberse a datos escasos.

## 6. Recomendación

Ficha `bernasco-steenbeek-mas-lugares-que-delitos`, clúster `medicion-y-metodo`. Actualizar
[[analisis-espacial-del-delito]] (curva de Lorenz, Gini y Gini generalizado) y [[puntos-calientes]]
(la reformulación de la ley).
