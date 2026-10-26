---
title: Análisis espacial del delito
type: method
sources: ["2016 - Weisburd y otros - El lugar importa, criminología para el siglo XXI.pdf", "2011 - Batthyány y Cabrera - Metodología de la investigación en ciencias sociales.pdf", "2014 - Srur (ed.) - ¿Qué observan los que observan el delito, observatorios del crimen y la violencia en América Latina.pdf", "2010 - Tudela (ed.) - Análisis delictual, enfoque y metodología para la reducción del delito.pdf", "2010 - Vozmediano y San Juan - Criminología ambiental, ecología del delito y de la seguridad.pdf", "2004 - Ratcliffe - Geocodificación del delito y una primera estimación de la tasa mínima aceptable de acierto.pdf", "2015 - Weisburd - La ley de concentración del delito y la criminología del lugar.pdf", "2004 - Weisburd, Bushway, Lum y Yang - Trayectorias del delito en los lugares, un estudio longitudinal de segmentos de calle en Seattle.pdf", "2017 - Bernasco y Steenbeek - Más lugares que delitos, implicancias para evaluar la ley de concentración del delito en el lugar.pdf", "2019 - Chainey y otros - Concentración del delito en microlugares en América Latina.pdf"]
cluster: medicion-y-metodo
curso: [s1-1]
procedencia: fuentes
estado: revisado
creado: 2026-09-26
actualizado: 2026-10-26
---

# Análisis espacial del delito

Conjunto de técnicas para estudiar dónde ocurre el delito y por qué, cuando la unidad de análisis es un lugar y no una persona. Su premisa es que **lo que pasa en un lugar no es independiente de lo que pasa en los lugares vecinos**. Tratar los lugares como observaciones independientes lleva a errores de inferencia [^ext-1].

**Segunda página de `wiki/methodology/`**, y la primera que viene de un texto metodológico. La otra, [[diagnostico-barrial]], viene de una guía operativa.

## Primero la teoría

Los autores insisten en que el método sin teoría deja a las instituciones en el papel de simples respondedoras: saben dónde ocurre algo, pero no por qué ni qué papel juega el lugar [^ext-2]. Las teorías de la oportunidad y de la desorganización social son las que dicen qué medir [^ext-2]. Ver [[puntos-calientes]].

## Cuatro problemas que hay que resolver

**1. Autocorrelación espacial.** Ocurre cuando el delito en un área hace más o menos probable el delito en el área contigua. Con datos de delito es casi siempre positiva: los lugares cercanos se parecen [^ext-3]. Para la estadística clásica es un problema, porque viola el supuesto de independencia. Para el mapeo es la base, porque la interpolación que produce un mapa de calor depende de ella [^ext-4]. Un modelo con un término espacial mostró que el robo de autos en una cuadra depende de las características de esa cuadra y también de las de las cuadras que la rodean [^ext-4].

**2. Falacia ecológica.** Robinson (1950) mostró que una correlación entre áreas no dice nada seguro sobre los individuos. A nivel de estados de EE. UU., la relación entre inmigración y alfabetización era fuerte y positiva; a nivel individual, era pequeña y negativa [^ext-5]. La crítica vale también para los estudios de microlugar si intentan concluir algo sobre personas y no sobre lugares [^ext-5].

Añadido el 16-10-2026. [[batthyany-metodologia-investigacion]] la define con Galtung (1966): concluir que una relación entre variables de un colectivo vale para sus miembros [^ext-25]. Su ejemplo es escolar. Que las escuelas con más niños pobres tengan más ausentismo no prueba que los niños pobres falten más [^ext-25]. Agrega un error vecino, el de confundir unidades de evento con unidades de persona: contar faltas no es contar niños que faltan [^ext-26]. Con datos policiales pasa lo mismo, porque contar delitos no es contar víctimas ni lugares [^inf-1]. Ver [[diseno-de-investigacion]].

**3. Problema de la unidad espacial modificable.** Los resultados cambian según la unidad en que se agregan los datos: por la escala —manzanas contra comunas— y por cómo se trazan los límites [^ext-6]. Los límites administrativos, pensados para otros fines, casi nunca separan lo que el delito separa [^ext-6]. En Vancouver, cuanto más pequeña la unidad, más estable resultó la concentración del delito en cinco años (Andresen y Malleson, 2011) [^ext-7]. La recomendación es recolectar los datos en la unidad más pequeña posible: después se pueden agregar, pero no al revés [^ext-8].

**4. Efecto de borde.** Un análisis cambia si se agregan datos de las áreas vecinas. En un mapa de calor de Filadelfia, recortar los datos a un solo distrito policial cambió la intensidad de los puntos calientes en su límite [^ext-9].

**El riesgo del promedio.** Agregar a unidades grandes no sólo pierde información: la distorsiona. Un área con unos pocos lugares muy activos parece peligrosa en su conjunto, y un área con muchos lugares tranquilos puede ocultar sus puntos calientes [^ext-10].

## Sitio y situación

Para interpretar un lugar hay que separar dos cosas [^ext-11]:

- **Sitio**: sus características internas, como el tipo de edificio o sus medidas de seguridad.
- **Situación**: qué tiene cerca, como una salida de autopista.

Confundirlas produce errores. En un suburbio, las casas con rejas tenían más robos, pero no por las rejas: estaban junto a salidas de autopista [^ext-11]. En Filadelfia, un aparente punto caliente de robo de autos se explicaba entero por un estacionamiento de varios pisos [^ext-12]. Y los centros de tratamiento de drogas no degradaban su entorno: estaban ubicados donde ya había consumo [^ext-13].

## Técnicas para identificar y predecir

| Técnica | Qué hace | Estado de la evidencia |
|---|---|---|
| **Pruebas de permutación** | Comparan el patrón observado con el esperado si el delito se repartiera según los blancos que realmente existen | Muestran que el robo en viviendas se agrupa más de lo esperable [^ext-14] |
| **Análisis aorístico** | Estima a qué hora ocurrió un delito cuya hora exacta se desconoce | Permite combinar dónde y cuándo [^ext-15] |
| **Repetición cercana** (prueba de Knox) | Detecta si, tras un delito, aumenta el riesgo en el mismo lugar y los cercanos durante un tiempo | Confirmada para robo en viviendas, robo desde vehículos, balaceras y asaltos [^ext-16] |
| **Estimación de densidad (KDE)** | Mapa de calor suavizado a partir de los delitos pasados | Supone que lo riesgoso seguirá siéndolo [^ext-17] |
| **Modelado de terreno de riesgo** | Suma capas de factores de riesgo —bares, botillerías, paraderos— aunque aún no haya delitos | Supera al KDE en predicciones de largo plazo, pero sus ventajas rara vez se han verificado de forma independiente [^ext-18] |
| **Mapeo prospectivo** y modelos de proceso autoexcitado | Incorporan la dinámica de repetición cercana y los factores fijos del entorno | Los que combinan ambas cosas son los más precisos [^ext-19] |
| **Simulación basada en agentes** | Prueba «qué pasaría si» antes de intervenir | Útil para anticipar la intensidad necesaria de una intervención [^ext-20] |

Una aplicación distinta: el **campo de visión de las cámaras**. Para evaluar una cámara no basta con su ubicación: hay que modelar qué puede ver, porque un infractor no se disuade si cree que la cámara no lo ve [^ext-21].

**Otra clasificación.** Añadido el 26-10-2026 al ingerir [[vozmediano-criminologia-ambiental]]. Un manual de 2010 ordena las técnicas de otro modo. Primero los mapas descriptivos: de puntos, de coropletas y de densidad [^ext-30]. Después los estadísticos que contrastan la concentración contra el azar: la función K y el STAC para puntos, y el I de Moran y LISA para áreas [^ext-31]. Dos reglas previas: las direcciones se geocodifican a coordenadas precisas, y se mapea un solo tipo de delito, porque los patrones difieren [^ext-32]. Los mapas muestran dónde, no por qué [^ext-33].

## Geocodificación y unidad

Añadido el 26-10-2026 al ingerir [[ratcliffe-tasa-de-geocodificacion]], [[weisburd-ley-de-concentracion]] y [[weisburd-trayectorias-seattle]].

**La tasa de acierto.** Casi nunca se geocodifica el 100 % de los registros [^ext-34]. Ratcliffe estimó con una simulación cuánto se puede perder sin que el mapa cambie: 85 %, como primera estimación [^ext-35]. El umbral tiene dos condiciones. Se calculó con mapas agregados a manzanas censales [^ext-36]. Y supone pérdidas al azar: si los registros fallidos se agrupan, por ejemplo en calles nuevas o en hitos sin dirección, hace falta una tasa mayor [^ext-37]. Recomienda revisar los registros perdidos en busca de un patrón [^ext-37]. Weisburd (2015) y Chainey y otros (2019) usan el 85 % como umbral [^ext-38].

**El segmento y las intersecciones.** El segmento reduce el error de geocodificación: una dirección mal registrada rara vez saca el delito de su segmento [^ext-39]. Las intersecciones se excluyen porque pertenecen a varios segmentos. No es un detalle: en Seattle eran el 19 % de los registros, y allí el 44 % de los reportes era de tránsito [^ext-40]. En las ocho ciudades de Weisburd, la proporción de delitos en intersecciones fue de 0 a 33 % [^ext-41].

## Medir la concentración

Añadido el 26-10-2026 al ingerir [[bernasco-steenbeek-mas-lugares-que-delitos]]. Los estudios reportan enunciados como «el Y % del delito en el X % de los lugares», con cortes a voluntad [^ext-42]. La **curva de Lorenz** reúne todos esos enunciados en un gráfico, y el **coeficiente de Gini** los resume entre 0 y 1 [^ext-43].

**Datos escasos.** Cuando hay menos delitos que lugares, las dos medidas sobrestiman la concentración, porque un delito no se divide [^ext-44]. Pasa con frecuencia con segmentos y direcciones, con periodos cortos y con delitos específicos [^ext-45]. El sesgo afecta también los porcentajes acumulados [^ext-46]. La corrección es el **Gini generalizado**, G' = máx(n/c, 1) · (G − 1) + 1, que compara con la máxima igualdad posible [^ext-47]. En La Haya, la agresión parecía más concentrada que el robo con fuerza, 0,86 contra 0,73. El Gini generalizado los iguala: 0,72 y 0,73 [^ext-48].

## Límites

- **Los datos van atrás de los métodos.** La calidad de los datos policiales era suficiente hace una década y hoy las técnicas nuevas la superan [^ext-22]. En América Latina el atraso es mayor. En 2014, el 45 % de los observatorios de la región no podía determinar la hora de los hechos, el 40 % no registraba el lugar, y el 31,5 % no tenía software para georreferenciar [^ext-27]. Ver [[observatorios-del-delito]].
- **Faltan evaluaciones de las técnicas.** Muchos las adoptan sin conocer sus ventajas y límites [^ext-22].
- **Los datos sociales llegan en unidades grandes.** Los datos del censo suelen publicarse en unidades mayores que la calle, lo que empuja a agregar hacia arriba [^ext-23].
- **La visión cualitativa también cuenta.** Reducir situaciones complejas a puntos en un mapa pierde información. Hay propuestas de SIG cualitativo y de métodos mixtos [^ext-24].
- **Dos Ratcliffe de 2004.** Añadido el 26-10-2026. El manual de Vozmediano y San Juan cita a Ratcliffe (2004), «The hotspot matrix», sobre mapas de densidad. Hay otro trabajo del mismo autor y año sobre la tasa mínima aceptable de geocodificación. El corpus no tenía ninguno de los dos [^amb-1]. Desde el 26-10-2026 tiene el segundo, [[ratcliffe-tasa-de-geocodificacion]]: la tasa de 85 % viene de allí.

## Cita

> "spatial autocorrelation is not a problem, but the basis of a solution" [la autocorrelación espacial no es un problema, sino la base de una solución]
> — Goodchild (2009, p. 414), citado en Weisburd y otros (2016, p. 92)

## Relacionado

- [[weisburd-el-lugar-importa]] — fuente
- [[puntos-calientes]] — lo que estas técnicas identifican
- [[diagnostico-barrial]] — un método que agrega por barrio; el riesgo del promedio se aplica a él
- [[policia-de-puntos-calientes]] — la práctica que más usa estas técnicas
- [[batthyany-metodologia-investigacion]] — segunda fuente sobre la falacia ecológica
- [[observatorios-del-delito]] — los datos de lugar y hora que faltan en la región
- [[estadisticas-delictuales]] — las dos fechas de un delito y la tasa por blanco
- [[diseno-de-investigacion]] — unidades de análisis, eventos y personas, y la falacia ecológica en general
- [[vozmediano-criminologia-ambiental]] — mapas, geocodificación y estadísticos de hot spot
- [[ratcliffe-tasa-de-geocodificacion]] — la tasa mínima de geocodificación y sus condiciones
- [[bernasco-steenbeek-mas-lugares-que-delitos]] — curva de Lorenz y Gini generalizado
- [[weisburd-ley-de-concentracion]] — el segmento como unidad y las intersecciones

**Contraste del 16-10-2026.** Batthyány y Cabrera (2011) toca la falacia ecológica. El capítulo de Boba en [[tudela-ed-analisis-delictual]] aporta dos insumos de estas técnicas. Todo delito tiene una fecha de denuncia y una de ocurrencia, y en los delitos sin testigos la segunda es un intervalo entre la primera y la última hora posibles [^ext-28]. Ese intervalo es lo que el análisis aorístico necesita [^inf-2]. Y la tasa debe dividir por el blanco, no por la población: robos al comercio por tienda, robos en casas por vivienda [^ext-29]. Es la misma lógica de las pruebas de permutación, que comparan con los blancos que realmente existen [^inf-2]. Ver [[estadisticas-delictuales]].

---

[^ext-1]: **Extraído** — [[weisburd-el-lugar-importa]], pp. 88-89.
[^ext-2]: **Extraído** — [[weisburd-el-lugar-importa]], pp. 86-88.
[^ext-3]: **Extraído** — [[weisburd-el-lugar-importa]], p. 91.
[^ext-4]: **Extraído** — [[weisburd-el-lugar-importa]], p. 92, sobre Goodchild (2009) y Rice y Smith (2002).
[^ext-5]: **Extraído** — [[weisburd-el-lugar-importa]], p. 12, sobre Robinson (1950).
[^ext-6]: **Extraído** — [[weisburd-el-lugar-importa]], pp. 93-94, sobre Rengert y Lockwood (2009).
[^ext-7]: **Extraído** — [[weisburd-el-lugar-importa]], pp. 94-95.
[^ext-8]: **Extraído** — [[weisburd-el-lugar-importa]], p. 8.
[^ext-9]: **Extraído** — [[weisburd-el-lugar-importa]], p. 94 y figura 5.1.
[^ext-10]: **Extraído** — [[weisburd-el-lugar-importa]], p. 13.
[^ext-11]: **Extraído** — [[weisburd-el-lugar-importa]], p. 36, sobre Rengert y Groff (2011).
[^ext-12]: **Extraído** — [[weisburd-el-lugar-importa]], pp. 36-37, sobre Rengert (1997).
[^ext-13]: **Extraído** — [[weisburd-el-lugar-importa]], pp. 39-40 y tabla 2.4, sobre Taniguchi y otros (2009).
[^ext-14]: **Extraído** — [[weisburd-el-lugar-importa]], p. 102.
[^ext-15]: **Extraído** — [[weisburd-el-lugar-importa]], p. 103, sobre Ratcliffe y McCullagh (1998).
[^ext-16]: **Extraído** — [[weisburd-el-lugar-importa]], p. 104.
[^ext-17]: **Extraído** — [[weisburd-el-lugar-importa]], pp. 104-105.
[^ext-18]: **Extraído** — [[weisburd-el-lugar-importa]], pp. 105 y 111, sobre Caplan, Kennedy y Miller (2011).
[^ext-19]: **Extraído** — [[weisburd-el-lugar-importa]], pp. 105-108.
[^ext-20]: **Extraído** — [[weisburd-el-lugar-importa]], pp. 108-110.
[^ext-21]: **Extraído** — [[weisburd-el-lugar-importa]], pp. 100-101.
[^ext-22]: **Extraído** — [[weisburd-el-lugar-importa]], p. 111.
[^ext-23]: **Extraído** — [[weisburd-el-lugar-importa]], pp. 9 y 152.
[^ext-24]: **Extraído** — [[weisburd-el-lugar-importa]], pp. 97-98.
[^ext-25]: **Extraído** — [[batthyany-metodologia-investigacion]], pp. 70-71, sobre Galtung (1966).
[^ext-26]: **Extraído** — [[batthyany-metodologia-investigacion]], p. 70.
[^ext-27]: **Extraído** — [[srur-observatorios-del-delito]], p. 37, y resumen ejecutivo, p. 6.
[^ext-28]: **Extraído** — [[tudela-ed-analisis-delictual]], p. 84.
[^ext-29]: **Extraído** — [[tudela-ed-analisis-delictual]], p. 92.
[^inf-1]: **Inferido** (confianza 0.8) — aplicación propia del ejemplo escolar del manual a los registros policiales. El manual no habla de delito.
[^inf-2]: **Inferido** (confianza 0.7) — Boba no nombra el análisis aorístico ni las pruebas de permutación. La correspondencia es de esta wiki.
[^ext-30]: **Extraído** — [[vozmediano-criminologia-ambiental]], pp. 92-98.
[^ext-31]: **Extraído** — [[vozmediano-criminologia-ambiental]], pp. 99-101, sobre Anselin, Griffiths y Tita (2008).
[^ext-32]: **Extraído** — [[vozmediano-criminologia-ambiental]], p. 91.
[^ext-33]: **Extraído** — [[vozmediano-criminologia-ambiental]], p. 101.
[^amb-1]: **Ambiguo** — [[vozmediano-criminologia-ambiental]], pp. 98 y 110. Quien cite una tasa de acierto de geocodificación atribuida a Ratcliffe (2004) debe verificar cuál de los dos trabajos la trae.
[^ext-34]: **Extraído** — [[ratcliffe-tasa-de-geocodificacion]], p. 61.
[^ext-35]: **Extraído** — [[ratcliffe-tasa-de-geocodificacion]], pp. 61 y 69.
[^ext-36]: **Extraído** — [[ratcliffe-tasa-de-geocodificacion]], pp. 66-69.
[^ext-37]: **Extraído** — [[ratcliffe-tasa-de-geocodificacion]], pp. 69-70.
[^ext-38]: **Extraído** — [[weisburd-ley-de-concentracion]], p. 142, y [[chainey-concentracion-america-latina]], p. 1.
[^ext-39]: **Extraído** — [[weisburd-ley-de-concentracion]], p. 142, y [[weisburd-trayectorias-seattle]], pp. 290-291.
[^ext-40]: **Extraído** — [[weisburd-trayectorias-seattle]], p. 291.
[^ext-41]: **Extraído** — [[weisburd-ley-de-concentracion]], pp. 140 y 143.
[^ext-42]: **Extraído** — [[bernasco-steenbeek-mas-lugares-que-delitos]], p. 452.
[^ext-43]: **Extraído** — [[bernasco-steenbeek-mas-lugares-que-delitos]], pp. 454 y 456.
[^ext-44]: **Extraído** — [[bernasco-steenbeek-mas-lugares-que-delitos]], pp. 452 y 457.
[^ext-45]: **Extraído** — [[bernasco-steenbeek-mas-lugares-que-delitos]], p. 453.
[^ext-46]: **Extraído** — [[bernasco-steenbeek-mas-lugares-que-delitos]], p. 463.
[^ext-47]: **Extraído** — [[bernasco-steenbeek-mas-lugares-que-delitos]], pp. 458-459.
[^ext-48]: **Extraído** — [[bernasco-steenbeek-mas-lugares-que-delitos]], pp. 462-463.
