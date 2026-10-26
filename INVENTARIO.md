# INVENTARIO — corpus de fuentes

**Fecha:** 26-10-2026 · **Total:** 143 documentos · **767 MB**

> **Nomenclatura normalizada el 12-09-2026.** Los 114 documentos siguen ya el
> patrón `año - autor - título`; no queda ninguno fuera de convención. Sin año
> verificable se usa `s.f.`.
>
> **13 documentos ingresaron el 12-09-2026 sin clasificar.** Están al final de
> este archivo, en el cúmulo `Ingreso sin clasificar`, que es una cuarentena y no
> una categoría temática. Ninguno entra al orden de ingesta hasta que se resuelva
> el ítem correspondiente de `wiki/revision.md`.

`raw/sources/` es plano y no admite subcarpetas. La única taxonomía del corpus es
esta tabla: el agrupamiento vive aquí, en metadatos, no en el árbol de archivos.
Los encabezados de esta tabla son los **cúmulos** con que `scripts/estado.py`
agrupa el avance del despliegue; renombrarlos cambia ese informe.

Nomenclatura: `año - autor - título en español.ext`. Sin año verificable, `s.f.`;
sin autor verificable, `Autor por identificar`.

Carpeta inmutable: aquí no se edita, no se anota y no se convierte nada. La wiki
se escribe en `wiki/`; las fichas de cada ramo, en `programa/`.


## Núcleo ancla S1.1 · 4 doc.


Alimenta: S1.1. **Prioridad 0 de ingesta.**

Las cuatro lecturas marcadas como obligatorias en el programa del curso ancla, y las
únicas marcadas como obligatorias en todo el material de programas recibido. Llegaron
el 11-09-2026 y se ingieren antes que cualquier otro cúmulo.

| Documento | MB | MD5 |
|---|---:|---|
| 2006 - Sampson - Vecindario y comunidad, eficacia colectiva y seguridad ciudadana.pdf | 0.1 | `19868e43b1c3` |
| 2017 - Adams - La violencia crónica y su reproducción, tendencias perversas en las relaciones sociales, la ciudadanía y la democracia en América Latina.pdf | 1.9 | `5e6657144c64` |
| 2017 - Wikström - Por qué se delinque, una teoría de la acción situacional.pdf | 0.3 | `17556ae80696` |
| 2023 - Albarracín - Crimen organizado en América Latina.pdf | 0.2 | `2bc01a9cad32` |

**Duplicados del 09-10-2026.** Ese día llegaron dos copias de este cúmulo con nombres
opacos. `ADAMS_La_Violencia_Cronica_su_reproduccion_WWilson_IntCenter.pdf.pdf` tiene el
mismo MD5 que Adams (2017). `sampson_vecindario_ycomunidad_ef_colectiva.pdf` tiene otro
MD5, pero su texto coincide en un 99,9 % con el de Sampson (2006). Ninguno se cuenta como
documento ni se ingiere. El autor los retiró de `raw/sources/` antes del 24-10-2026.

## Bibliografía S1.1, consulta y complementaria · 12 doc.


Alimenta: S1.1. Blanco alimenta además S2.4.

Resto de lo integrado el 11-09-2026 desde el programa ancla: tres obras marcadas en rojo
—consulta— y dos de la bibliografía sin marca.

| Documento | MB | MD5 |
|---|---:|---|
| 2002 - Romero Mendoza y Aguilera Guzmán - ¿Por qué delinquen las mujeres, perspectivas teóricas tradicionales, parte I.pdf | 0.4 | `a09e7199c243` |
| 2003 - García-Pablos de Molina - Tratado de criminología (extracto, pp. 688-1372).pdf | 113.7 | `5b9c9bd35b03` |
| 2007 - Alda y Beliz (eds.) - ¿Cuál es la salida, la agenda inconclusa de la seguridad ciudadana.pdf | 1.9 | `9f6d3488e0c4` |
| 2011 - Blanco - El enfoque del curso de vida, orígenes y desarrollo.pdf | 0.3 | `b5757d527a87` |
| 2020 - ONU-Hábitat y Gobierno Municipal de Guadalajara - Guía en seguridad y prevención de barrios.pdf | 1.8 | `c2dba1f1eac9` |

**Ocho documentos integrados el 12-09-2026, siete en el corpus.** Todos son
bibliografía oficial de S1.1 que faltaba. El octavo, el manual de Blokland y van der
Geest, se retiró el 26-09-2026 (ver la advertencia 2). Llegaron con nombres opacos y
se identificaron por su página de imprenta.

| Documento | MB | MD5 |
|---|---:|---|
| 2004 - Kessler - Sociología del delito amateur.pdf | 9.6 | `d9e3a1fc5d5c` |
| 2004 - Wacquant - Las cárceles de la miseria.pdf | 8.3 | `cff7d0ca14e5` |
| 2005 - Garland - La cultura del control, crimen y orden social en la sociedad contemporánea (traducción Gedisa de Sozzo).pdf | 24.7 | `7bb6c6e443a0` |
| 2016 - Bergman - Drogas, narcotráfico y poder en América Latina.pdf | 2.0 | `590e0855895a` |
| 2023 - Bergman - El negocio del crimen, el crecimiento del delito, los mercados ilegales y la violencia en América Latina.pdf | 2.5 | `f6ac444b1af0` |
| 2024 - Zeballos - Un virus entre sombras, la expansión del crimen organizado y el narcotráfico en Chile.epub | 1.5 | `3c3c8d82540a` |
| 2026 - Zeballos - Cuando el crimen reza.epub | 3.0 | `4778ad29b5d4` |

Tres advertencias sobre este bloque:

1. **Garland: queda solo la traducción.** El archivo fechado en 2001 resultó ser **el
   original en inglés** (University of Chicago Press y Oxford, ISBN 0-226-28383-6),
   aunque tenía título en español. El que llegó el 12-09-2026 es la traducción de
   Máximo Sozzo, Gedisa, primera edición de abril de 2005, ISBN 84-9784-040-2: la
   edición que pide `programa/S1.1`. **El 26-09-2026 se retiró el original en inglés.**
   El autor lo declaró un error de integración, porque ya tiene la traducción. Se
   borró su fila del cúmulo `Sistema penal y Estado de derecho`, que era donde estaba
   registrado.
2. **Blokland y van der Geest no sustituía a Gibson y Krahn, y se retiró.** S1.1 pide
   el *Handbook of life course criminology* de Gibson y Krahn (2013, Springer). Lo que
   llegó fue el *Routledge International Handbook of Life-Course Criminology* de
   Blokland y van der Geest (2017, Taylor & Francis): otra obra, otros editores y otra
   editorial. Es el mismo patrón que Romero Mendoza frente a Alvarado y que Zaffaroni.
   **El 26-09-2026 se retiró del corpus:** el autor lo declaró un error de integración
   que no corresponde al curso. Gibson y Krahn sigue faltando.
3. **Dos divergencias de año.** Wacquant: el programa pide la edición de 2000 y el
   corpus tiene la primera edición, segunda reimpresión, de Manantial 2004. Zeballos:
   el programa pide *Cuando el crimen reza* de 2025 y los metadatos del archivo dan
   2026.

**Duplicados del 09-10 y del 17-10-2026.** `GU_A_DE_BARRIOS_ESPA_OL.pdf` llegó el 09-10
con otro MD5, pero su texto coincide en un 99,7 % con el de la guía de ONU-Hábitat y
Guadalajara (2020). `annas-arch-d9e3a1fc5d5c.pdf` llegó el 17-10 con el mismo MD5 que
Kessler (2004). Ninguno se cuenta como documento ni se ingiere. El autor los retiró de
`raw/sources/` antes del 24-10-2026.

## Bibliografía obligatoria S2.4 · 3 doc.


Alimenta: S2.4. Brizuela alimenta además S1.1, por el libro que reseña.

Las tres son lecturas obligatorias del programa vigente de S2.4. Llegaron el 17-10-2026
con nombres opacos y se identificaron el 23-10-2026 por su página de imprenta. Con ellas,
el ramo pasa de una a cuatro de sus nueve obligatorias en el corpus.

| Documento | MB | MD5 |
|---|---:|---|
| 2002 - Bourdieu - La juventud no es más que una palabra.pdf | 1.1 | `4fc96fc7d998` |
| 2012 - Duarte Quapper - Sociedades adultocéntricas, sobre sus orígenes y reproducción.pdf | 0.3 | `e2ac0bb916b8` |
| 2014 - Brizuela - Reseña de Sociología del delito amateur, de Gabriel Kessler.pdf | 0.1 | `3632c52660ae` |

- **Bourdieu.** Es el capítulo de *Sociología y cultura* (Grijalbo y Conaculta), pp.
  163-173. El nombre de origen decía 1990. Se usa 2002, el año que dan el pie del propio
  archivo y el programa.
- **Duarte Quapper.** *Última Década*, n.º 36, CIDPA Valparaíso, julio de 2012, pp.
  99-125. Coincide con la cita del programa.
- **Brizuela.** *Revista Cátedra Paralela*, n.º 11, 2014, pp. 313-317. Reseña la edición
  de Paidós de 2010, y el corpus tiene la de 2004.

## Juventudes, módulo I de S2.4 · 9 doc.


Alimenta: S2.4, módulo I. Ninguna es obligatoria del programa vigente.

Llegaron el 24-10-2026 con nombres opacos y se identificaron el mismo día por su
portada o su página de imprenta. Cinco son complementarias del programa vigente de
S2.4. Las otras cuatro no están en él: Brito y Romero se citan en la presentación de la
clase 1, Souto y Brito estaban en el programa de 2023, y Lozano no figura en ningún
programa recibido.

| Documento | MB | MD5 |
|---|---:|---|
| 1999 - Feixa - De jóvenes, bandas y tribus, antropología de la juventud.pdf | 8.0 | `1a9f77e09234` |
| 2000 - Duarte Quapper - Juventud o juventudes, acerca de cómo mirar y remirar a las juventudes de nuestro continente.pdf | 0.1 | `d7ae49e71469` |
| 2000 - Sennett - La corrosión del carácter, las consecuencias personales del trabajo en el nuevo capitalismo.pdf | 6.9 | `4b2814d3a22f` |
| 2010 - Krauskopf - La condición juvenil contemporánea en la constitución identitaria.pdf | 0.1 | `1ac385828cd5` |
| 2012 - Rubio Gil y San Martín Pascal - Subculturas juveniles, identidad, idolatrías y nuevas tendencias.pdf | 0.5 | `04dfc48f97ca` |
| 1998 - Brito Lemus - Hacia una sociología de la juventud, algunos elementos para la deconstrucción de un nuevo paradigma de la juventud.pdf | 0.1 | `d87efb3e4ac2` |
| 2003 - Lozano Urbieta - Nociones de juventud.pdf | 0.0 | `aa8233b0a47c` |
| 2007 - Souto Kustrín - Juventud, teoría e historia, la formación de un sujeto social y de un objeto de análisis.pdf | 0.3 | `912e221cfade` |
| 2015 - Romero Miranda - La edad sociológica, una mirada de la infancia desde el adelantamiento y la acumulación de experiencia.pdf | 0.8 | `c4c4dce4f9ed` |

- **Feixa.** Ariel, Barcelona. Primera edición de marzo de 1998 y segunda de marzo de
  1999. Se usa 1999, la edición que cita el programa. El escaneo tiene capa de texto
  con errores de OCR.
- **Duarte Quapper (2000).** *Última Década*, n.º 13, CIDPA Viña del Mar, septiembre de
  2000, pp. 59-77. Firma «Klaudio». En el artículo de 2012 firma «Claudio»: es el mismo
  autor, y las dos iniciales del programa no son un error.
- **Sennett.** Anagrama, primera edición de enero de 2000. El ejemplar es la octava
  impresión, de 2005. **Es un escaneo sin capa de texto** y necesita OCR antes de
  ingerirse.
- **Krauskopf.** *Última Década*, n.º 33, CIDPA Valparaíso, diciembre de 2010, pp.
  27-42. El nombre de origen decía «Krauskopp».
- **Rubio Gil y San Martín Pascal.** *Revista de Estudios de Juventud* (Injuve), n.º 96.
  El programa no da año. Se usa 2012, por el número de la revista y la fecha del PDF.
  Falta confirmarlo contra el índice del número.
- **Brito Lemus.** *Última Década*, n.º 9, CIDPA Valparaíso, 1998. Es la definición de
  juventud con que abre la clase 1 de S2.4.
- **Lozano Urbieta.** *Última Década*, n.º 18, CIDPA Viña del Mar, abril de 2003, pp.
  11-19.
- **Souto Kustrín.** *Historia Actual Online*, n.º 13, 2007, pp. 171-192.
- **Romero Miranda.** Año 9, n.º 14, diciembre de 2015, desde la p. 46. El PDF no
  nombra la revista. Es la fuente de la cirposición y la edad sociológica de la clase 1.

**Duplicados del 24-10-2026.** Dos archivos llegaron junto a estos y no se cuentan
como documentos ni se ingieren:
`2017 - Arias - empresas criminales y gobernanza en amlat.pdf` tiene el mismo MD5 que
Arias (2017), y `bourdieu_la_juventud_no_es_m_s_que_una_palabra.pdf` tiene otro MD5,
pero su texto y sus seis páginas coinciden con Bourdieu (2002). Siguen en
`raw/sources/` hasta que el autor los retire.

## Explicación del delito · 11 doc.


Alimenta: S1.3 —Baratta, Pavarini y, por contenido, Felson y Eckert— y S1.1 —Gottfredson
y Hirschi—. La atribución anterior daba los cuatro a S1.1; el programa ancla, recibido el
11-09-2026, sólo confirma uno. Ver `programa/S1.1`.

**Alta del 02-10-2026: Bourgois (2010).** Llegó como `bourgois-en-busca-del-respeto
-Violencia como lenguaje.pdf` y se renombró a la convención. Es la traducción de 2010 de la
2.ª edición en inglés (2003) de una obra de 1995. «Violencia como lenguaje» no está en el
libro: es un añadido de quien nombró el archivo, y queda como pregunta en
`wiki/revision.md`. Ningún programa recibido lo nombra. Ingerido el mismo día, fuera del
orden por calendario, por decisión del autor.

**Alta del 26-10-2026: Vozmediano y San Juan (2010).** Sale de la cuarentena de `Ingreso sin
clasificar` por decisión del autor, que verificó su pertinencia. Es un manual de criminología
ambiental: teorías de la oportunidad, mapas del delito y hot spots. Se ingirieron sólo los caps.
III y IV, para el diseño de investigación aplicada de S1.2. Ningún programa recibido lo pide.

**Alta del 26-10-2026: ocho artículos citados por el diseño de S1.2.** El autor los agregó a
`raw/sources/` con nombres sin convención, y se renombraron el mismo día: `Cohen and Felson 1979
Routine Activities.pdf`, `opportunity_makes_the_thief.pdf`, `ssrn-2632683.pdf`, `weisburd2015.pdf`,
`chainey2019.pdf`, `guerette2009.pdf`, `ratcliffe2004.pdf` y `s10940-016-9324-7.pdf`. Cinco van a este
cúmulo. Guerette y Bowers (2009) va a `Prevención e intervención`, y Ratcliffe (2004) y Bernasco y
Steenbeek (2017), a `Medición e inseguridad`. Ningún programa recibido los pide. Ingeridos el mismo
día en la tanda S1.2d, por decisión del autor.


| Documento | MB | MD5 |
|---|---:|---|
| 1979 - Cohen y Felson - Cambio social y tendencias del delito, un enfoque de las actividades rutinarias.pdf | 3.3 | `d862220e808f` |
| 1990 - Gottfredson y Hirschi - Una teoría general del delito.pdf | 31.3 | `a9c9341311ce` |
| 1998 - Felson y Clarke - La oportunidad hace al ladrón, teoría práctica para la prevención del delito.pdf | 0.4 | `fbc28033f7df` |
| 2002 - Pavarini - Control y dominación, teorías criminológicas burguesas y proyecto hegemónico.pdf | 9.3 | `96cfa9d34aa2` |
| 2004 - Baratta - Criminología crítica y crítica del derecho penal, introducción a la sociología jurídico-penal.pdf | 9.5 | `4ff1f2891d1d` |
| 2004 - Weisburd, Bushway, Lum y Yang - Trayectorias del delito en los lugares, un estudio longitudinal de segmentos de calle en Seattle.pdf | 2.3 | `09198d84abba` |
| 2010 - Bourgois - En busca de respeto, vendiendo crack en Harlem.pdf | 16.8 | `7e154c5a74d5` |
| 2010 - Vozmediano y San Juan - Criminología ambiental, ecología del delito y de la seguridad.pdf | 2.2 | `83da5982df7d` |
| 2015 - Weisburd - La ley de concentración del delito y la criminología del lugar.pdf | 0.5 | `97a6dff65ea6` |
| 2016 - Felson y Eckert - El delito y la vida cotidiana.pdf | 11.6 | `0b35231846f5` |
| 2019 - Chainey y otros - Concentración del delito en microlugares en América Latina.pdf | 0.8 | `bdad2144ecf4` |

## Vínculo Estado-crimen · 18 doc.


Alimenta: S3.E4.


| Documento | MB | MD5 |
|---|---:|---|
| 1985 - Tilly - La guerra y la construcción del Estado como crimen organizado.pdf | 1.6 | `db1216d29913` |
| 1988 - Chambliss - Crimen organizado de Estado.pdf | 1.4 | `cf44b0614b88` |
| 1990 - Tilly - Coerción, capital y los Estados europeos.pdf | 15.7 | `3732734188cd` |
| 1996 - Gambetta - La mafia siciliana, el negocio de la protección privada.pdf | 25.6 | `782ac72332c0` |
| 2003 - Hill - La mafia japonesa, yakuza, ley y Estado.pdf | 1.0 | `3fc80bf529dc` |
| 2003 - McCoy - La política de la heroína, la complicidad de la CIA en el tráfico global de drogas.pdf | 47.2 | `1abfed552382` |
| 2004 - Williams - El crimen organizado transnacional y el Estado.pdf | 0.1 | `28b7b304324e` |
| 2008 - Xia - Formaciones organizacionales del crimen organizado en China.pdf | 0.2 | `05bf6c37c50a` |
| 2009 - Greenhill - Interdependencia cleptocrática, tráfico, corrupción y el vínculo entre política y ganancias ilícitas.pdf | 1.7 | `585e2817439c` |
| 2010 - Chabat - El Estado y el crimen organizado transnacional.pdf | 0.1 | `8f36f7835842` |
| 2014 - Duncan - Más que plata o plomo, el poder político del narcotráfico.pdf | 11.9 | `d582e3047575` |
| 2016 - Gómez-Hecht - Interdependencia cleptocrática, el caso de El Salvador.pdf | 0.5 | `fc0aa8624bef` |
| 2016 - Schultze-Kraft - Órdenes crimilegales, repensando el poder político del crimen organizado.pdf | 0.2 | `5d71e4003646` |
| 2017 - Farah y Babineau - Surinam, el nuevo paradigma de un Estado criminalizado.pdf | 3.9 | `012e6b5a557f` |
| 2018 - Grabosky - Simpatía por el diablo, la vinculación del Estado con organizaciones criminales.pdf | 1.3 | `f9b348237995` |
| 2019 - Caballero - Del crimen organizado a la crimilegalidad.pdf | 0.6 | `1cde6e7ba789` |
| 2023 - Hill - El Estado como organización criminal transnacional, el caso de Corea del Norte.pdf | 0.2 | `f0e1d86651ed` |
| 2023 - Lavorgna - El nexo político-criminal en los ciberdelitos de Estado.pdf | 0.7 | `8864e9d39499` |

## Gobernanza criminal y territorio · 6 doc.


Alimenta: S2.1, S3.E4.

**Duplicado del 02-10-2026.** `2017 - Arias - empresas criminales y gobernanza en
amlat.pdf` apareció ese día con el mismo tamaño y el mismo MD5 que el Arias (2017) de esta
tabla. No se cuenta como documento ni se ingiere. Retirarlo le corresponde al autor; mientras
siga en la carpeta, `scripts/estado.py` lo reportará fuera de inventario.


| Documento | MB | MD5 |
|---|---:|---|
| 2006 - Arias - Las dinámicas de la gobernanza criminal.pdf | 3.7 | `e26f1fb9b3c4` |
| 2012 - Garzón Vergara - La rebelión de las redes criminales, el crimen organizado en América Latina.pdf | 0.3 | `c2b00a2617d6` |
| 2015 - Salinero - El crimen organizado en Chile, aproximación criminológica al perfil del delincuente.pdf | 0.8 | `adbe5e650bff` |
| 2016 - Weisburd y otros - El lugar importa, criminología para el siglo XXI.pdf | 7.0 | `58efa2121eb5` |
| 2017 - Arias - Empresas criminales y gobernanza en América Latina.pdf | 2.0 | `2726230a32fc` |
| 2024 - Campana y Meneghini - El desplazamiento del crimen organizado en comunidades locales.pdf | 1.9 | `81e8c4889dec` |

**Duplicado del 26-10-2026.** `annas-arch-cb4897d86908.pdf` llegó a `raw/sources/` con los artículos de
la tanda S1.2d. Es otra copia de Weisburd y otros (2016): el texto extraído es idéntico y el archivo
difiere en 148 bytes. No se ingiere ni se cuenta. Borrarlo de `raw/sources/` es decisión del autor. Ver
`wiki/revision.md`.

## Prevención e intervención · 7 doc.


Alimenta: S1.1, S2.3, S3.1.


| Documento | MB | MD5 |
|---|---:|---|
| 1997 - Clarke - Prevención situacional del delito, casos de éxito.pdf | 0.3 | `9d9427605858` |
| 2009 - Guerette y Bowers - El alcance del desplazamiento del delito y de la difusión de beneficios, una revisión de evaluaciones de prevención situacional.pdf | 0.4 | `8eae90a409cb` |
| 2011 - UNODC - Manual sobre la aplicación eficaz de las directrices para la prevención del delito.pdf | 2.0 | `06ae0a1b418b` |
| 2015 - Vanderschueren - Guía para la prevención en barrios.pdf | 2.8 | `06b1d0fa4eea` |
| 2019 - Schroeder y Coello-Torres - Placemaking, transformación de un lugar en el asentamiento humano Santa Julia, Piura, Perú.pdf | 1.4 | `ae86d2118c19` |
| 2024 - Guerra Araya - Orquestando el ecosistema de seguridad local, el modelo Las Condes.pdf | 11.9 | `5c580cd0b7ff` |
| s.f. - Gobierno de Santiago - Guía para la gestión local de la seguridad desde los barrios.pdf | 15.1 | `27b8260d7fab` |

**Dos documentos sumados el 23-10-2026**, ambos sobre barrio y espacio público. Sirven a
los módulos 3 y 4 de S1.1 y a su prueba final, cuya pauta admite como objeto «un espacio
público significativo».

- **Gobierno de Santiago (s.f.).** Llegó el 09-10-2026 como `Guia_de_barrios_WEB.pdf`. Es
  otra obra que la guía de ONU-Hábitat (2020), aunque comparte autores con ella: entre
  ellos Germán Díaz Urrutia y Franz Vanderschueren, docentes de S2.4 y S1.1. Aplica el
  método Rotterdam a barrios de la Región Metropolitana en 2023. No imprime año: su cita
  más reciente es de 2023 y el PDF se generó el 23-04-2025. El año se resuelve contra la
  publicación del Gobierno de Santiago.
- **Schroeder y Coello-Torres (2019).** Llegó el 23-10-2026 como `PLACEMAKING.pdf`.
  *Revista Hábitat Sustentable, 9*(1), 6-19. La presentación del módulo 4 de S1.1 trata el
  placemaking y no cita este artículo.

## Institucionalidad y política de prevención en Chile · 8 doc.


Alimenta: S1.1 (clase 0, Leitao) y S2.3. Ingresaron el 26-09-2026 como la bibliografía
de la presentación de Carolina Leitao, «Prevención en Chile: de la teoría a la práctica,
desde lo nacional a lo local». Tres son normas descargadas de LeyChile (BCN). El autor
que figura en el nombre es el ministerio de origen que registra la BCN, y el año es el
de publicación en el Diario Oficial.

- **Ley 21.730**: promulgada el 27-01-2025 y publicada el 05-02-2025. Es la versión única, vigente desde el 01-04-2025.
- **Decreto 96**: promulgado el 22-10-2025 y publicado el 30-01-2026. Aprueba la Política Nacional de Seguridad Pública 2025-2031. La BCN lo rotula «(2025)» por el año de promulgación.
- **Ley 21.802**: promulgada el 03-02-2026 y publicada el 11-02-2026. La versión descargada rige desde el 12-08-2026.
- **Comunicado de la ACOT**: se sumó el 26-09-2026. Es el comunicado oficial de
  prensa.presidencia.cl del 05-08-2026, guardado como recorte web en Markdown. En él, el
  presidente Kast anuncia en cadena nacional la Agenda contra el Crimen Organizado y el
  Terrorismo (ACOT), sigla que la presentación de Leitao usa sin explicar (diap. 35). Es
  una fuente de gobierno, no académica: registra el anuncio, no sus resultados. La fecha
  de publicación figura en el cuerpo del texto; el campo `published` del recorte quedó
  vacío.
- **Ley 21.675**: se sumó el 27-09-2026 por decisión del autor, y no viene de la
  presentación de Leitao. Actualiza el estado legal que describe Valdivia-Peralta y otros
  (2019), lectura de la clase 4 de S1.2. Promulgada el 03-06-2024 y publicada el
  14-06-2024. Es el texto consolidado de la BCN, con la última modificación de la Ley
  21.829 del 22-07-2026, generado el 27-09-2026. Llegó como `Ley-21675_14-JUN-2024.pdf` y
  se renombró a la convención sin tocar el contenido. Estatuye medidas contra la violencia
  hacia las mujeres en razón de su género; no es una norma de seguridad pública, aunque
  obliga a las policías y al Ministerio del Interior.


| Documento | MB | MD5 |
|---|---:|---|
| 2023 - Luneke y Trebilcock - Prevención del delito, la construcción de la seguridad ciudadana y los cambios en la política criminal en Chile, 1990-2017.pdf | 0.3 | `fc0823159263` |
| 2024 - Ministerio de la Mujer y la Equidad de Género - Ley 21.675, estatuye medidas para prevenir, sancionar y erradicar la violencia en contra de las mujeres en razón de su género.pdf | 0.2 | `525120bde6d8` |
| 2025 - Ministerio del Interior y Seguridad Pública - Ley 21.730, crea el Ministerio de Seguridad Pública.pdf | 0.1 | `2c2c9d2625e7` |
| 2026 - Ministerio de Seguridad Pública - Decreto 96, aprueba la Política Nacional de Seguridad Pública.pdf | 0.3 | `2037255cc177` |
| 2026 - Ministerio de Seguridad Pública - Ley 21.802, fortalece la institucionalidad municipal en materia de seguridad pública y prevención del delito.pdf | 0.1 | `5c546f131941` |
| 2026 - Presidencia de la República - Presidente Kast anuncia la Agenda contra el Crimen Organizado y el Terrorismo (ACOT) en cadena nacional.md | 0.0 | `dfa27aa6cb6e` |
| 2016 - Ministerio del Interior y Seguridad Pública - Ley 20.965, permite la creación de consejos y planes comunales de seguridad pública.pdf | 0.1 | `33a8f68f4be2` |
| 2026 - Municipalidad de Las Condes - Decreto 2098, aprueba el Plan Comunal de Seguridad Pública 2026-2029.pdf | 19.6 | `7aba63774c90` |

**Dos normas sumadas el 24-10-2026** por decisión del autor, por delante de la cola: el
diseño de investigación de S1.2 se ancla en ellas.

- **Ley 20.965**: promulgada el 24-10-2016 y publicada el 04-11-2016. Es la versión
  única de la BCN, generada el 24-10-2026. Es una ley modificatoria: su contenido vive en
  la Ley 18.695, y la Ley 21.802 de 2026 reformó buena parte de él. Llegó como
  `Ley-20965_04-NOV-2016.pdf`.
- **Decreto 2098**: decreto alcaldicio de la Municipalidad de Las Condes, Sección 1.ª,
  del 18-06-2026. Aprueba el Plan Comunal de Seguridad Pública 2026-2029, acordado por el
  concejo el 02-04-2026. Es un escaneo de 63 páginas sin capa de texto: el cuerpo del
  decreto ocupa las pp. 1-30 y el plan se repite como anexo con paginación propia en las
  pp. 31-62. Llegó como `decreto.2098.18jun2026.pdf`.

## Medición e inseguridad · 8 doc.


Alimenta: S1.2.


| Documento | MB | MD5 |
|---|---:|---|
| 2004 - Ratcliffe - Geocodificación del delito y una primera estimación de la tasa mínima aceptable de acierto.pdf | 0.1 | `0261ed59cb3d` |
| 2012 - Dammert - Miedo y delito en América Latina.pdf | 12.0 | `a642681572c4` |
| 2014 - Srur (ed.) - ¿Qué observan los que observan el delito, observatorios del crimen y la violencia en América Latina.pdf | 7.6 | `02a3f693cb3e` |
| 2016 - Cámara Arroyo - Principales instrumentos de medición de la peligrosidad criminal.md | 0.0 | `c8f25592bfde` |
| 2017 - Bernasco y Steenbeek - Más lugares que delitos, implicancias para evaluar la ley de concentración del delito en el lugar.pdf | 0.8 | `ce71781dccd5` |
| 2022 - Luna Pla - El análisis de redes complejas aplicado a grupos de crimen y corrupción.pdf | 0.2 | `1dc04dc73d0f` |
| 2023 - INE - Actualización metodológica de la medición de victimización y percepción de inseguridad, informe metodológico.pdf | 1.4 | `bc447d5662f3` |
| 2023 - González-Guarda y Salazar-Tobar - Una panorámica de la criminología en Chile, una comunidad científica transitando hacia la profesionalización.pdf | 0.5 | `0d1906a5b2bd` |

## Sistema penal y Estado de derecho · 8 doc.


Alimenta: S1.3. El Garland original en inglés (2001), que S1.3 pide en esa edición, se
retiró el 26-09-2026. La obra queda cubierta por la traducción Gedisa (2005), que está en
el cúmulo `Bibliografía S1.1, consulta y complementaria`.

Zúñiga Núñez (2013) entró el 26-09-2026 con su nombre de descarga
(`annas-arch-870bab747f1a.pdf`) y se renombró a la convención. No es bibliografía de
ningún programa: es un proyecto de tesis de pregrado en Derecho, inédito. Se ingirió el
mismo día, fuera del orden por calendario, por decisión del autor.


| Documento | MB | MD5 |
|---|---:|---|
| 1995 - Ferrajoli - Derecho y razón, teoría del garantismo penal.pdf | 43.7 | `6b5014fd43f7` |
| 1997 - Rose-Ackerman - Corrupción y competencia.pdf | 0.4 | `b659e8ed96df` |
| 2001 - Silva Sánchez - La expansión del derecho penal, aspectos de la política criminal en las sociedades postindustriales.pdf | 8.8 | `623cd19b343a` |
| 2007 - Gardner - La prohibición de las inmoralidades.pdf | 0.1 | `9b15f07d8d21` |
| 2013 - Tanguay-Renaud - Criminalizar al Estado.pdf | 0.3 | `4f8139e435a3` |
| 2013 - Zúñiga Núñez - Civilización y derechos humanos, hacia una radicalización de los derechos fundamentales.pdf | 1.5 | `870bab747f1a` |
| 2016 - Pérez - La economía informal y las finanzas públicas, de piratas a corsarios contemporáneos.pdf | 0.1 | `4d759b0da956` |
| 2023 - Stamouli, Gasparinatou y Kouroutzas - Corrupción y delito corporativo en el sistema de salud griego.pdf | 1.4 | `6b22f382a621` |

## Amenaza y securitización · 24 doc.


Alimenta: S3.E4.


| Documento | MB | MD5 |
|---|---:|---|
| 1995 - Shelley - El crimen organizado transnacional como amenaza inminente al Estado-nación.pdf | 2.1 | `81e02a725ef3` |
| 1995 - Williams - Alianzas estratégicas del crimen organizado transnacional.pdf | 1.2 | `03982a1c2286` |
| 2002 - Löwenheim - Argumentos contra la inflación de la amenaza del crimen organizado transnacional.pdf | 2.3 | `70ffb0e3b1a3` |
| 2003 - Allum y Siebert - Crimen organizado y el desafío a la democracia.pdf | 1.8 | `90b4c14cbfb7` |
| 2007 - Friedrichs - Crimen transnacional y criminología global.pdf | 1.4 | `90914a33bfc0` |
| 2007 - Wonders - Globalización, reconstrucción de fronteras y crimen transnacional.pdf | 1.3 | `fea954bf544e` |
| 2008 - Jones y Libicki - Cómo terminan los grupos terroristas.pdf | 0.6 | `cf7512047a3a` |
| 2009 - Dordevic - El crimen organizado transnacional como amenaza a la seguridad y sus teorías.pdf | 0.2 | `f4a25f3c6326` |
| 2009 - Zabyelina - El crimen organizado transnacional en las relaciones internacionales.pdf | 0.7 | `2c859871624d` |
| 2010 - UNODC - La globalización del delito, evaluación de la amenaza del crimen organizado transnacional.pdf | 10.6 | `aea1aff97cbf` |
| 2011 - Casa Blanca (EE.UU.) - Estrategia contra el crimen organizado transnacional.pdf | 0.8 | `30f0658f6ac8` |
| 2012 - Beare - Enciclopedia del crimen y la justicia transnacional.pdf | 57.7 | `918614ef487c` |
| 2016 - Abadinsky - Crimen organizado (11a edición).pdf | 11.4 | `8834a9690c4e` |
| 2017 - Pulido Gragera - Nuevos retos para la inteligencia estratégica ante el desarrollo de las amenazas híbridas (extracto).pdf | 3.1 | `2e11822d62dc` |
| 2018 - Schmid - Revisión de la relación entre terrorismo internacional y crimen organizado transnacional.pdf | 0.5 | `f2aaf7251453` |
| 2019 - Goertz y Streitparth - El nuevo terrorismo.pdf | 2.2 | `c1c8a38ff93b` |
| 2019 - Leukfeldt y Holt - Cibercriminales en los Países Bajos.pdf | 0.1 | `f99847e8cd92` |
| 2020 - UNODC - Veinte años de la Convención de Palermo.pdf | 1.1 | `1234cb41f30c` |
| 2021 - EUROPOL - Evaluación de la amenaza del crimen grave y organizado (SOCTA).pdf | 38.0 | `dbca2d5101df` |
| 2021 - Rivera Vélez y Sansó-Rubert - Crimen organizado y seguridad multidimensional.pdf | 20.8 | `c85e43c7b097` |
| 2022 - Di Nicola - El crimen organizado digital.pdf | 0.5 | `2e6a3c8082c1` |
| 2022 - Sulistyo, Wiranata y Lestari - Teorías, conceptos y métodos de relaciones internacionales para investigar el crimen organizado transnacional.pdf | 0.6 | `b61cf358c026` |
| 2023 - Sullivan - La era de la información, crimen organizado transnacional, redes y mercados.pdf | 2.1 | `b7cf0c4da95b` |
| 2023 - Ucko y Marks - El crimen organizado como guerra irregular.pdf | 1.8 | `a48fbdf8904a` |

## Integrados desde el programa del curso (05-09-2026) · 9 doc.


| Documento | MB | MD5 |
|---|---:|---|
| 2010 - Tudela (ed.) - Análisis delictual, enfoque y metodología para la reducción del delito.pdf | 4.7 | `2122b7b71125` |
| 2011 - Batthyány y Cabrera - Metodología de la investigación en ciencias sociales.pdf | 2.6 | `d901c0da698e` |
| 2015 - CIPC - Experiencias exitosas en prevención de la criminalidad en América Latina, una perspectiva territorial.pdf | 3.1 | `ee9fddfb9da2` |
| 2015 - Tudela - Análisis criminal, proactividad y desarrollo de estrategias policiales basadas en la evidencia.pdf | 0.6 | `733ace2a0d92` |
| 2019 - Valdivia, Fonseca, González y Paino - Invisibilización de la violencia en el noviazgo en Chile.pdf | 0.3 | `1d101363c343` |
| 2021 - Vanderschueren, Díaz y Guajardo (eds.) - Prevención del delito y la violencia, reflexiones desde la academia y los territorios.pdf | 1.9 | `787e80e312f8` |
| 2021 - Vives Varela y Hamui Sutton - La codificación y categorización en la teoría fundamentada.pdf | 0.5 | `dcd50eb9f829` |
| 2022 - Subsecretaría de Prevención del Delito - Orientaciones técnicas, prevención comunitaria del delito y la violencia.pdf | 0.7 | `c87e377d5d6e` |
| 2023 - Minayo, Deslandes y Gomes - Investigación social, teoría, método y creatividad.pdf | 7.8 | `28cc6ea65da8` |

## Programas oficiales y malla · 7 doc.

El programa de S2.4 de la promoción 2023 quedó reemplazado el 17-10-2026 por el vigente, de 2026. Se conserva para comparar las dos versiones. Ver `programa/S2.4`.


| Documento | MB | MD5 |
|---|---:|---|
| 2023 - Universidad Alberto Hurtado - Programa del curso, Abordaje de la violencia y delincuencia adolescente y juvenil.pdf | 0.2 | `2795c5f78693` |
| 2025 - Universidad Alberto Hurtado - Programa del curso, Metodología para la medición y análisis del delito.pdf | 0.3 | `543db059c1b8` |
| 2025 - Universidad Alberto Hurtado - Programa del curso, Sistema penal, política criminal y Estado de derecho.pdf | 0.1 | `1c31c6bed0ea` |
| 2026 - Universidad Alberto Hurtado - Horario, cohorte 2026, segundo semestre.pdf | 0.2 | `d682a5d2d7d9` |
| 2026 - Universidad Alberto Hurtado - Programa del curso, Abordaje de la violencia y delincuencia adolescente y juvenil.pdf | 0.3 | `eccfe14e7da3` |
| 2026 - Universidad Alberto Hurtado - Programa del curso, Introducción a la criminología y aspectos teóricos de la prevención del delito y la violencia (síntesis).md | 0.0 | `f6258904c24f` |
| 2026 - Universidad Alberto Hurtado - Programa del Magíster, presentación y malla.md | 0.0 | `65150a2e467f` |

## Ingreso sin clasificar · 9 doc.


**Cuarentena, no cúmulo temático.** Trece archivos aparecieron en `raw/sources/` el
12-09-2026, sin nomenclatura del corpus y sin pasar por decisión de alcance. Se listan
aquí para que `scripts/estado.py` deje de reportarlos como anomalía y para que la
situación quede visible, **no** para incorporarlos al orden de ingesta.

Tres constataciones de la verificación del 12-09-2026:

1. **Trece archivos, diez obras.** Hay duplicados exactos por MD5: `Criminología
   Preventiva .pdf` y `Criminología Preventiva. Estrategias-1.pdf` son el mismo
   archivo, y `Criminología mediatica.pdf` y `Criminología y victimología.pdf` también.
   `Criminología Preventiva II.pdf` tiene otro hash pero las mismas 161 páginas y la
   misma portada que las dos primeras: es una reexportación, no un segundo volumen.
2. **Ninguna está en la bibliografía oficial** de los cuatro programas de curso
   recibidos. Zaffaroni aparece en S1.3, pero por *En busca de las penas perdidas*
   (2006), que **no** es la obra que llegó. Es el mismo patrón de sustitución falsa
   que `programa/S1.1` ya registró con Romero Mendoza frente a Alvarado.
3. **Ninguna cubre los vacíos declarados** en `purpose.md`: siguen faltando Merton,
   los dos Sutherland y Lamnek para el módulo 5 de S1.1, Renzetti para criminología
   feminista, y toda la bibliografía oficial de S2.4.

**Depurado el 26-09-2026.** Se retiraron los tres archivos sobrantes que señala la
constatación 1: el duplicado exacto y la reexportación de *Criminología preventiva*, y
el duplicado exacto de Gaibor. Quedan diez archivos, uno por obra.

Renombrados a la convención del corpus el 12-09-2026. Estar en convención no
significa estar admitido: siguen en cuarentena.

**Salida del 26-10-2026.** El autor admitió a Vozmediano y San Juan (2010), que pasó a
`Explicación del delito`. Quedan nueve.

| Documento | MB | MD5 |
|---|---:|---|
| 2012 - Vélez Salas - Delincuencia, criminología y sociedad.pdf | 7.7 | `3fd71b116699` |
| 2013 - Hikal - Criminología psicológica.pdf | 8.3 | `b232e82520a1` |
| 2013 - Hikal - Introducción al estudio de la criminología (2a edición).pdf | 8.7 | `f152edbad675` |
| 2015 - Bernaola Ponce - Criminología ambiental orientada a la delincuencia juvenil (trabajo de fin de grado).pdf | 2.9 | `2d80f9d89df2` |
| 2017 - Zaffaroni, Bailone y Mavila León - Dogmática penal y criminología cautelar.pdf | 0.8 | `57dbd80b8388` |
| 2017 - Zapata - Criminología empresarial, manual de intervención criminológica en las empresas.pdf | 0.8 | `8208f9d5caa7` |
| 2022 - Ríos Patio y Hikal (dirs.) - Criminología preventiva, estrategias basadas en casos reales.pdf | 5.6 | `84bb567b9b71` |
| s.f. - Gaibor - Criminología mediática y victimología del miedo.pdf | 1.8 | `19a51b9488fa` |
| s.f. - Velasco de la Fuente - Criminal-mente, la criminología como ciencia.pdf | 2.2 | `35570db4be57` |

### Identificación

Datos tomados de las páginas de imprenta de cada archivo, no de la portada. Se
registran para que, si alguna se admite, pueda renombrarse a la nomenclatura del
corpus sin volver a abrirla.

| Archivo | Obra identificada | Imprenta | Tipo |
|---|---|---|---|
| Criminología ambiental.pdf · **admitida el 26-10-2026** | Vozmediano Sanz, L. y San Juan Guillén, C. *Criminología ambiental: ecología del delito y de la seguridad* | Editorial UOC, 1.ª ed. castellana mayo 2010 · ISBN 978-84-9788-847-5 | Manual académico |
| Criminología mediatica.pdf · Criminología y victimología.pdf | Gaibor, P. C. *Criminología mediática y victimología del miedo* | Universidad Andina Simón Bolívar, Quito · Serie Magíster 285 · ISBN 978-9942-837-08-0 · **año por confirmar** | Tesis de magíster publicada |
| DOGMÁTICA PENAL y CRIMINOLOGÍA CAUTELAR.pdf | Zaffaroni, E. R., Bailone, M. y Mavila León, R. *Dogmática penal y criminología cautelar* | Lima, 1.ª ed. octubre 2017 · Depósito Legal BNP 2017-13237 | Ensayo académico |
| Criminología Preventiva (3 archivos) | Ríos Patio, G. y Hikal, W. (dirs.); Riega Cayetano, R. y Pérez Arroyo, M. (coords.). *Criminología preventiva*. Colección de criminologías específicas, libro 12 | Universidad de San Martín de Porres, Fondo Editorial · 1.ª ed. electrónica mayo 2022, 161 pp. · ISBN 978-612-4460-43-2 | Obra colectiva |
| Criminología Psicológica.pdf | Hikal Carreón, W. S. *Criminología psicológica* | México, 1.ª ed. 2011 · © 2013 · ISBN 978-607-09-1403-4 | Manual |
| Introduccion-al-Estudio-de-la-Criminologia.pdf | Hikal Carreón, W. S. *Introducción al estudio de la criminología* | México, 2.ª ed. · 1.ª ed. 2009 · © 2013 · ISBN 978-607-09-1475-1 | Manual |
| Delincuencia_Criminologia_y_Sociedad.pdf | Vélez Salas, A. *Delincuencia, criminología y sociedad* | FUOC, © 2012 | Módulo docente |
| Criminología Empresarial.pdf | Zapata, A. *Criminología empresarial: manual de intervención criminológica en las empresas* | 2017 | Manual profesional |
| Criminologia ambiental Bernaola Ponce Nagore.pdf | Bernaola Ponce, N. *Criminología ambiental orientada a la delincuencia juvenil* (dir. L. Vozmediano Sanz y E. Ocáriz Passevant) | Universidad del País Vasco, curso 2014-2015 | **Trabajo de fin de grado** |
| Criminal-mente. La criminología como ciencia.pdf | Velasco de la Fuente, P. *Criminal-mente: la criminología como ciencia* | Grupo Planeta · **año por confirmar**, no anterior a 2016 | Divulgación de gran público |

Dos obras quedan con año por confirmar y ninguna con autor sin identificar.

**Sin duplicados con el corpus preexistente.** Se cruzaron los MD5 de los 106 archivos
de `raw/sources/`: hay 104 contenidos distintos, y los dos únicos grupos de duplicados
son los dos pares internos de este ingreso. Ninguno de los trece repite un documento
que ya estuviera en el corpus.

La decisión de alcance y la recomendación están en `wiki/revision.md`. Si se admite
alguna, se renombra a la nomenclatura del corpus, se traslada al cúmulo que
corresponda y se elimina esta sección de cuarentena.
