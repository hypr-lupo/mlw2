---
title: Revisión
type: revision
sources: []
---

# Revisión

Cola asincrónica de decisiones que corresponden al autor. Existe para no detener la
ingesta. Acciones admitidas, conjunto cerrado: `crear-pagina`, `investigar`,
`fusionar`, `omitir`, `preguntar`.

## Abiertos

- [ ] **[tesis]** «Anclaje empírico frente a marco conceptual heredado» — el
      programa exige que el trabajo de grado se ancle en una política, programa o
      proyecto identificable; el marco conceptual del proyecto anterior no lo hace.
      Confrontarlos es una posición del autor, no de ninguna fuente.
      Acción propuesta: `crear-pagina` · Origen: ingesta 2026-08-29
      Destino: `wiki/thesis/tesis-anclaje-empirico.md`, `procedencia: autor`

- [ ] **[entidad]** «Franz Vanderschueren» — director del programa y autor de dos
      fuentes del corpus todavía sin ingerir. Decidir si merece página propia o si
      basta mencionarlo en [[magister-prevencion-uah]].
      Acción propuesta: `preguntar` · Origen: inicialización 2026-09-05
      Criterio: si al ingerir sus dos obras resulta que sostienen afirmaciones
      distintas de las del folleto, merece página.
      **Enmienda 12-09-2026:** el criterio se cumple. Vanderschueren aparece ahora como
      **coautor** de [[onu-habitat-guia-barrios]], no sólo como director del programa, y
      esa guía sostiene bastante más que el folleto: la tipología barrial, el ciclo de
      política y el contenido de la coproducción de seguridad. Falta aún su segunda obra
      del corpus, Vanderschueren, Díaz y Guajardo (2021), sin ingerir.
      **Enmienda 26-09-2026** (ingesta de [[vanderschueren-guia-prevencion-barrios]]):
      entra una segunda obra suya, como primer autor y editor, y resulta ser la versión
      anterior de la guía de 2020, que la reedita sin citarla. El núcleo operativo que la
      wiki atribuía a la guía de 2020 —ciclo de política, diagnóstico diferenciado,
      coproducción— es obra de su equipo del Centro de Seguridad Ciudadana de la UAH
      desde hacia 2010. Refuerza el criterio ya cumplido. La decisión sigue siendo del
      autor; Vanderschueren, Díaz y Guajardo (2021) es la ingesta siguiente.

- [ ] **[concepto]** «Control social informal» — Sampson lo usa como el mecanismo
      causal de la eficacia colectiva sin definirlo, y es contenido del módulo 6 de
      S1.1 junto con el control social de Gottfredson y Hirschi, que es otra cosa
      —autocontrol individual—.
      Acción propuesta: `crear-pagina` · Origen: ingesta 2026-09-12
      Criterio: crearla al ingerir Gottfredson y Hirschi (1990), no antes, para que
      la página nazca distinguiendo ambos sentidos en lugar de fusionarlos.
      **Enmienda 12-09-2026** (ingesta de Wikström): la distinción ya tiene fuente
      que la nombra. Wikström y Trieber (2007) se titula «más allá de la teoría
      general del delito de Gottfredson y Hirschi», y [[autocontrol-y-disuasion]]
      deja escrito por qué la disuasión situacional de la TAS y el control social
      informal de Sampson no son el mismo concepto. Lo que sigue faltando es la voz
      de Gottfredson y Hirschi.
      **Enmienda 26-09-2026** (ingesta de Weisburd y otros): el concepto ya tiene una
      definición en el corpus. [[weisburd-el-lugar-importa]] lo define como la
      autorregulación de la conducta de residentes y visitantes por una comunidad
      local, para lograr un objetivo común (p. 58), y lo distingue de la gestión de
      lugares, que es intencional como el control formal pero no es función estatal
      (p. 49). El criterio sigue igual: la página nace con Gottfredson y Hirschi
      (tanda 4), para que distinga los dos sentidos desde el inicio.

- [ ] **[fuente]** Año de edición de Sampson — el corpus y el programa la fechan en
      2006; el texto declara un original de 2004 en *New Economy* y no consigna el
      año de la traducción; su bibliografía interna cita Sampson y Morenoff (2006)
      mientras el cuerpo cita esa misma obra como 2004.
      Acción propuesta: `preguntar` · Origen: ingesta 2026-09-12
      Consulta sugerida: ISBN 978-84-612-3131-7, «Claves del Gobierno Local» n.º 6,
      Fundación Democracia y Gobierno Local — año de publicación del volumen.
      Hasta resolverlo, la ficha queda con `verificacion_bibliografica: pendiente` y
      la obra no se cita en trabajos evaluados.

- [ ] **[entidad]** «Coalición de Diez Puntos» (Boston) — hoy es el único caso
      concreto con evaluación citada en toda la wiki, y sostiene la noción de
      institución mediadora. Vive dentro de [[legitimidad-policial]].
      Acción propuesta: `crear-pagina` · Origen: ingesta 2026-09-12
      Criterio: crearla si una segunda fuente la retoma. Con una sola mención y
      siendo un caso de Boston de los noventa, no hay peso analítico para página
      propia y sí riesgo de poblar el grafo con casos no chilenos.

- [ ] **[método]** PADS+, estudio del desarrollo de adolescentes y jóvenes adultos
      de Peterborough — 716 jóvenes seguidos desde los 12 años, retención del 97 %,
      diario espacio-temporal, escenarios aleatorios y dos encuestas de comunidad
      pequeña. Es el primer diseño de investigación completo que entra al corpus y
      `wiki/methodology/` sigue vacía.
      Acción propuesta: `crear-pagina` · Origen: ingesta 2026-09-12
      Criterio: crearla cuando entre la primera fuente metodológica de S1.2 —Tudela,
      Batthyány y Cabrera, Minayo— con la que contrastarlo. Escribirla ahora
      produciría una ficha de estudio, no una página de método. Nota: el diseño
      completo está en Wikström y otros (2012), *Breaking Rules*, que no está en el
      corpus.

- [ ] **[esquema]** Los grupos criminales no tienen dónde caber — un grupo como el
      PCC, las milícias de Rio o un cartel no encaja en ninguno de los cinco
      `subtipo` admitidos para `entity`: `persona`, `organismo`, `politica`,
      `programa`, `territorio`. Forzarlos a `organismo` pondría una milicia y una
      comisión internacional en la misma categoría.
      Acción propuesta: `preguntar` · Origen: ingesta 2026-09-12
      Criterio: es material de la operación 8, no de una ingesta. `schema.md` ya
      prevé reevaluar los tipos cuando se elija el caso de anclaje; conviene
      resolverlo en la misma pasada y no antes, para no declarar un subtipo por cada
      fuente nueva. Mientras tanto, los grupos viven dentro de
      [[gobernanza-criminal]] y [[crimen-organizado]].

- [ ] **[entidad]** «Milícias de Rio de Janeiro» — hoy el caso más desarrollado de
      toda la wiki sobre actores estatales que constituyen crimen organizado: cerca
      de 1,7 millones de personas bajo su dominio. Vive dentro de
      [[gobernanza-criminal]].
      Acción propuesta: `crear-pagina` · Origen: ingesta 2026-09-12
      Criterio: crearla si una segunda fuente las retoma. El cúmulo `Vínculo
      Estado-crimen` tiene candidatas —Arias, Duncan, Schultze-Kraft—, todas sin
      ingerir. Depende además de resolver el ítem de esquema anterior.

- [ ] **[entidad]** CICIG, Comisión Internacional Contra la Impunidad en Guatemala —
      único ejemplo positivo que ofrece [[albarracin-crimen-organizado-america-latina]]
      para la recomendación de política contra la impunidad estatal, y descansa en un
      solo estudio (Trejo y Nieto-Matiz, 2022).
      Acción propuesta: `crear-pagina` · Origen: ingesta 2026-09-12
      Criterio: crearla sólo con una segunda fuente. Una página de caso construida
      sobre un estudio citado de segunda mano es exactamente el tipo de respaldo
      aparente que [[purpose]] declara como el error más costoso del proyecto.

- [ ] **[fuente]** Fecha de publicación de Adams — el corpus y `programa/S1.1`
      coinciden en 2017, de modo que entre ellos no hay discrepancia. Pero el
      documento no consigna fecha en ninguna parte y su aparato bibliográfico no
      contiene ninguna obra posterior a 2011: 136 menciones de 2010, 55 de 2011,
      ninguna de 2012 en adelante. La autora menciona además como reciente el Informe
      Global sobre Homicidios de la ONU, de 2011.
      Acción propuesta: `preguntar` · Origen: ingesta 2026-09-12
      Consulta sugerida: wilsoncenter.org/ChronicViolence — año del original en
      inglés y año de la traducción al español de Megan Thomas.
      Importa por dos cosas: se citará en un trabajo evaluado, y cambia cómo se lee
      su vigencia. Un diagnóstico regional redactado hacia 2011 antecede a la
      escalada centroamericana posterior y a todo lo ocurrido en Chile.

- [ ] **[contradicción]** ¿Pesa el legado del conflicto armado sobre la violencia
      actual? [[adams-violencia-cronica]] se contradice consigo misma en dos párrafos
      consecutivos: sostiene que la traumatización política extrema explica respuestas
      desproporcionadas al riesgo —con su propio trabajo de campo en Guatemala como
      apoyo— y acto seguido cita al Banco Mundial concluyendo que la evidencia amplia
      no sugiere que la violencia centroamericana resulte principalmente de ese
      legado, sin relación significativa entre las localidades más golpeadas por la
      guerra y la violencia contemporánea.
      Acción propuesta: `preguntar` · Origen: ingesta 2026-09-12
      Criterio: la resolución depende de qué se acepte como indicador. La autora
      señala que el estudio del Banco define violencia estrechamente, por tasas de
      homicidio —y la tesis de ella es justamente que la violencia crónica se mide mal
      si sólo se cuentan homicidios—. Queda registrada en [[miedo-social]] y en la
      ficha, sin resolver. El corpus tiene material que podría dirimirlo en el cúmulo
      `Medición e inseguridad`, sin ingerir.

- [ ] **[fuente]** La Guía ONU-Hábitat es un borrador — la portada de
      [[onu-habitat-guia-barrios]] dice «Borrador avanzado». No es una publicación
      cerrada y la wiki ya construyó cuatro páginas sobre ella.
      Acción propuesta: `preguntar` · Origen: ingesta 2026-09-12
      Consulta sugerida: sitio de ONU-Hábitat, programa Ciudades más Seguras — ¿existe
      versión final de la *Guía en seguridad y prevención de barrios*? Si existe, hay
      que cotejar la tipología y el ciclo de política, que son lo que la wiki registra.
      Importa más de lo habitual: es la obra que operacionaliza el trabajo evaluado de
      S1.1 y su coautor es el docente del ramo.
      **Enmienda 26-09-2026** (ingesta de [[vanderschueren-guia-prevencion-barrios]]):
      el riesgo baja a la mitad. El ciclo de política y el diagnóstico diferenciado por
      tipo de barrio tienen **versión publicada**: la guía que ONU-Hábitat y la UAH
      editaron hacia 2010, que la de 2020 reproduce casi textualmente sin citarla. Lo
      que sigue dependiendo sólo del borrador es lo propio de 2020: la tipología de
      cinco categorías, la proyección de resultados por tipología con la metodología de
      Rotterdam, el caso Guadalajara y la adopción de la violencia crónica. Pero la guía
      anterior tiene su propio problema de año y autoría; ver el ítem siguiente.

- [ ] **[concepto]** Teorías de la oportunidad —elección racional, patrón
      delictivo, actividades rutinarias y prevención situacional—.
      [[weisburd-el-lugar-importa]] las expone como una de las dos familias que
      explican la concentración del delito, y hoy cinco páginas las mencionan sin
      tener adónde enlazar: [[puntos-calientes]], [[gestion-de-lugares]],
      [[desplazamiento-y-difusion]], [[analisis-espacial-del-delito]] y
      [[desorganizacion-social]].
      Acción propuesta: `crear-pagina` · Origen: ingesta 2026-09-26
      Criterio: crearla con Clarke (1997) y Felson y Eckert (2016), que están en el
      corpus y entran en la tanda 4. Escribirla desde Weisburd sería escribirla
      desde el resumen de quien las usa, no desde sus autores.

- [ ] **[investigar]** ¿Vale la ley de concentración del delito en una comuna
      chilena? [[weisburd-el-lugar-importa]] no reporta ningún estudio de
      concentración en América Latina, y sus autores advierten que la ley no se ha
      probado en países de ingresos bajos ni en ciudades en crisis social o económica
      (p. 143). Es el supuesto de cualquier política de focalización territorial, y la
      wiki lo usa en [[puntos-calientes]], [[policia-de-puntos-calientes]] y
      [[diagnostico-barrial]].
      Acción propuesta: `investigar` · Origen: ingesta 2026-09-26
      Criterio: buscar primero en el corpus —las metodológicas de S1.2 y el cúmulo
      `Institucionalidad y política de prevención en Chile`, sin ingerir— y sólo
      después afuera. Una página hecha desde búsqueda web iría a `wiki/synthesis/`
      con `procedencia: mixta`, y no se citaría en un trabajo evaluado sin sustituirla
      por los estudios originales.

- [ ] **[alcance]** Zúñiga Núñez (2013) es, sobre todo, teoría del Estado.
      [[zuniga-civilizacion-y-derechos-humanos]] entró el 26-09-2026 por decisión
      expresa del autor, fuera del orden por calendario. Su veta criminológica
      —criminalización, castigo, selectividad— ocupa pocas páginas. El grueso es sistema
      mundo, imperio, civilización e iusnaturalismo. Toca dos reglas de [[purpose]]: el
      apartado «Diferido» manda que la ampliación temática por interés propio entre como
      capa nueva, con clúster propio; y «Fuera» excluye la teoría del Estado que sostenía
      la memoria previa.
      Acción propuesta: `preguntar` · Origen: ingesta 2026-09-26
      Lo que se hizo mientras tanto: la ficha va al clúster `sistema-penal`, que es donde
      cae su veta criminológica. Sólo se tocaron tres páginas, y únicamente con esa veta.
      La teoría del Estado no tiene páginas. Si el autor prefiere la capa nueva, basta
      cambiar el `cluster` de la ficha. Si prefiere retirarla, el retiro en cascada deja
      las tres páginas con sus demás fuentes y sólo les quita esta.

- [ ] **[fuente]** Institución y estado de Zúñiga Núñez (2013) — el documento es un
      proyecto de tesis de pregrado en Derecho, firmado en Maipú el 4 de marzo de 2013,
      con Patricia Albornoz como profesora guía. No nombra la escuela. Varias notas
      remiten a la Universidad Central de Chile, lo que la sugiere sin confirmarla. Tampoco
      dice si el proyecto se aprobó ni si existe una versión final.
      Acción propuesta: `preguntar` · Origen: ingesta 2026-09-26
      Consulta sugerida: repositorio de tesis de la Universidad Central de Chile, autor
      «Zúñiga Núñez, Ariel», 2013. Hasta resolverlo, la ficha queda con
      `verificacion_bibliografica: pendiente` y la obra no se cita en trabajos evaluados.

- [ ] **[concepto]** Criminalización y selectividad penal — criminalización primaria y
      secundaria, selectividad del sistema penal, derecho penal simbólico. Hoy sólo
      aparecen resumidos de segunda mano en [[zuniga-civilizacion-y-derechos-humanos]],
      junto con su tesis propia: la criminalización como castigo más legitimación.
      Acción propuesta: `crear-pagina` · Origen: ingesta 2026-09-26
      Criterio: crearla con Baratta (2004), caps. I-II, IV, VII y VIII, que entra en la
      tanda 3, y sumar a Zúñiga como segunda voz. Hacerla nacer desde un proyecto de tesis
      inédito fijaría el encuadre desde la fuente más débil del cúmulo.

- [ ] **[fuente]** Año y autoría de la *Guía para la prevención en barrios* — tres
      fechas y ninguna coincide. Los créditos de [[vanderschueren-guia-prevencion-barrios]]
      dicen «© 2010», con el código HS/116/10S. El prólogo la presenta como complemento
      de una guía sobre jóvenes fechada en 2011, mientras la introducción habla de esos
      materiales en futuro. El corpus la fecha en 2015. Tampoco coincide la autoría: son
      seis autores —Vanderschueren, Olave, Ruiz, Mosciatti, del Canto y Díaz— y el
      nombre del archivo lleva sólo el primero.
      Acción propuesta: `preguntar` · Origen: ingesta 2026-09-26
      Consulta sugerida: catálogo de publicaciones de ONU-Hábitat o del Centro de
      Seguridad Ciudadana de la UAH, ISBN 978-92-1-132226-2 — año de publicación, y si
      existe una reimpresión o segunda edición de 2015 que explique la fecha del corpus.
      Hasta resolverlo la ficha usa el año de los créditos, queda con
      `verificacion_bibliografica: pendiente` y la obra no se cita en trabajos evaluados.
      El nombre del archivo en `raw/sources/` no se toca: renombrarlo es decisión del
      autor.

- [ ] **[entidad]** «Quiero mi Barrio» — el primer programa chileno que entra a la
      wiki. [[vanderschueren-guia-prevencion-barrios]] lo describe en la población Santa
      Elena de El Bosque, desde 2007: un consejo vecinal de desarrollo que prioriza obras
      físicas y un plan de gestión social (p. 62). Es exactamente el tipo de programa
      identificable sobre el que puede anclarse el trabajo evaluado de S1.1 o el de
      grado.
      Acción propuesta: `crear-pagina` · Origen: ingesta 2026-09-26
      Criterio: crearla cuando una segunda fuente lo trate, y con `vigencia` declarada.
      Una sola descripción de hace más de quince años no sostiene una página de
      programa. Candidatas en el corpus: SPD (2022), orientaciones técnicas, en la tanda
      5, y Luneke y Trebilcock (2023), en la tanda 6. Mientras tanto la guía trae otros
      territorios chilenos —La Legua, Herminda de la Victoria, La Ermita— y el Programa
      24 Horas de Carabineros, todos dentro de la ficha.

- [ ] **[concepto]** Mediación comunitaria — [[vanderschueren-guia-prevencion-barrios]]
      le dedica un tratamiento propio: la experiencia del Balcón de Derechos en las
      favelas de Rio, las características del mediador, y cómo instalarla paso a paso
      como cultura de resolución pacífica de conflictos (pp. 72-74). La propone como
      acción de largo plazo en los barrios críticos.
      Acción propuesta: `crear-pagina` · Origen: ingesta 2026-09-26
      Criterio: crearla si una segunda fuente la desarrolla. Vanderschueren, Díaz y
      Guajardo (2021), la ingesta siguiente, es la candidata más cercana.

- [ ] **[fuente]** Gardner (2007) está en el corpus como versión de autor — el archivo
      de [[gardner-prohibir-inmoralidades]] es el mecanografiado que Gardner publicó en su
      página, y su portada pide no citar ni transcribir desde él y usar siempre la
      versión definitiva. Las páginas que registra la wiki son las del mecanografiado, y
      a la referencia le falta el rango de páginas de la revista.
      Acción propuesta: `preguntar` · Origen: ingesta 2026-09-26
      Consulta sugerida: *Cardozo Law Review*, vol. 28, 2007, p. 2613 en adelante —
      conseguir el artículo publicado, completar la referencia y cotejar las páginas.
      Hasta entonces la ficha queda con `verificacion_bibliografica: pendiente`, sin cita
      textual, y la obra no se cita en trabajos evaluados.

- [ ] **[concepto]** Principio de daño y Estado de derecho — [[gardner-prohibir-inmoralidades]]
      los pone como dos de las tres condiciones para prohibir una conducta inmoral, y
      como las restricciones especiales que pesan sobre el Estado. No los define ni los
      defiende: los da por aceptados. Hoy viven sólo dentro de [[moralismo-legal]].
      Acción propuesta: `crear-pagina` · Origen: ingesta 2026-09-26
      Criterio: crearlas con Ferrajoli (1995), *Derecho y razón*, en la tanda 6: el
      principio de lesividad y las garantías penales son su tema. Escribirlas desde
      Gardner sería escribirlas desde quien las da por supuestas.

## Resueltos

- [x] **[concepto]** Puntos calientes (concentraciones espacio-temporales del
      delito) — mencionado por [[sampson-vecindario-y-comunidad]] y explicado por
      [[wikstrom-por-que-se-delinque]] como convergencia de personas propensas y
      entornos criminógenos. Dos fuentes lo tocan de paso y ninguna lo desarrolla.
      Acción propuesta: `crear-pagina` · Origen: ingesta 2026-09-12
      Criterio: la página nace con Weisburd y otros (2016), *El lugar importa*, que
      está en el corpus y es la obra dedicada al asunto. Crearla antes sería
      escribirla desde dos notas al margen.
      **Resuelto el 26-09-2026 — `crear-pagina`.** Se cumplió el criterio: nace
      [[puntos-calientes]] con [[weisburd-el-lugar-importa]], la obra dedicada al
      asunto, y registra desde el primer día la tensión con la explicación de la TAS.
      De ella salen además [[policia-de-puntos-calientes]] y
      [[desplazamiento-y-difusion]].

- [x] **[concepto]** «Desorganización social» — el módulo 3 de `programa/S1.1`
      enmarca a Sampson dentro de esta teoría, y Sampson no la nombra en ningún
      momento. Ninguna fuente del corpus la define: García-Pablos de Molina la
      cubriría, pero el extracto disponible parte en la página 688.
      Acción propuesta: `preguntar` · Origen: ingesta 2026-09-12
      Criterio: decidir si se cubre con [[eficacia-colectiva]] como heredera, si se
      escribe desde García-Pablos cuando se ingiera, o si es un vacío que se declara.
      No se resuelve escribiéndola desde Sampson: sería atribuirle un marco que no
      enuncia.
      **Resuelto el 26-09-2026 — `crear-pagina`, por la ingesta.** Ninguna de las tres
      salidas previstas hizo falta: entró al corpus una fuente que sí la define y que
      sí ubica ahí a Sampson. [[weisburd-el-lugar-importa]] expone la teoría desde Shaw
      y McKay, sitúa la eficacia colectiva dentro de ella y la lleva a escala de calle.
      Nace [[desorganizacion-social]], escrita desde esa obra y no desde Sampson, como
      pedía el criterio. Queda en `borrador`: es una exposición de segunda mano, hecha
      por autores que la usan para su propio argumento. García-Pablos, cuando llegue
      completo, sirve de contraste. Si el autor prefería otra de las salidas, se
      reabre este ítem.

- [x] **[corpus]** Dos documentos registrados en `INVENTARIO.md` no estan en
      `raw/sources/` — detectado el 13-09-2026 al cotejar el inventario contra el disco,
      archivo por archivo. Los dos llevan MD5 registrado, de modo que existieron cuando
      se levanto el inventario y desaparecieron despues.
      Accion propuesta: `investigar` · Origen: agnosticacion 2026-09-13

      · **`2017 - Blokland y van der Geest (eds.) - Manual internacional Routledge de
        criminologia del curso de vida.epub`** (5,1 MB, `b26e9da7f080`). Figura entre
        los ocho titulos integrados el 12-09-2026 y [[pendientes]] lo cuenta como
        recibido.
      · **`2001 - Garland - La cultura del control... (original en ingles).pdf`**. El
        inventario dice «se conservan ambos» al registrar la llegada de la traduccion
        Gedisa; en disco solo esta la Gedisa.

      Ninguno de los dos aparece tampoco en `ESTADO.md`, que cuenta sobre el disco y no
      sobre el inventario: o nunca se copiaron a `raw/sources/`, o se borraron antes del
      12-09-2026.

      **Las cifras, al 13-09-2026.** `raw/sources/` tiene **111 archivos**, de los cuales
      6 son programas oficiales: el universo que mide `estado.py` son **105 documentos**,
      no 106. La diferencia es una copia de Gaibor —`s.f. - Gaibor - Criminologia
      mediatica y victimologia del miedo (duplicado exacto).pdf`— que figura en
      `ESTADO.md` y ya no esta en disco. Eso es **higiene de duplicados ya hecha**, no
      una perdida: baja el corpus sin bajar la cobertura. `ESTADO.md` se pone al dia
      solo, en la proxima corrida de `python scripts/estado.py`.

      **Consecuencia inmediata: ninguna.** Ninguno de los tres archivos esta ingerido y
      ninguno bloquea el orden vigente. Lo que importa resolver es si el Blokland se
      borro por error: es, junto con Blanco, el unico material de curso de vida del
      corpus, y Blanco es la siguiente ingesta.

      **Resuelto el 26-09-2026 — `omitir`.** Decisión del autor: los dos archivos
      fueron errores de integración y no se reponen. El manual de Blokland y van der
      Geest no corresponde al curso, y del Garland basta la traducción Gedisa (2005),
      que está en el corpus. Se borraron sus dos filas de `INVENTARIO.md`, y las fichas
      de S1.1 y S1.3 lo registran. Con esto el inventario coincide con el disco: 115
      filas para 115 archivos. El único material de curso de vida que queda en el
      corpus es Blanco (2011); Gibson y Krahn (2013), que pide S1.1, sigue faltando.

- [x] **[alcance]** Trece documentos ingresaron sin clasificar el 12-09-2026 — es la
      decisión más urgente de la cola, porque hasta resolverla el corpus declara 106
      documentos de los que trece no tienen estatus. Están en cuarentena en
      `INVENTARIO.md`, cúmulo `Ingreso sin clasificar`, con su identificación completa.
      Acción propuesta: `preguntar` · Origen: verificación de corpus 2026-09-12

      **Lo verificado.** Trece archivos son diez obras: `Criminología Preventiva .pdf`
      y `Criminología Preventiva. Estrategias-1.pdf` comparten MD5; `Criminología
      mediatica.pdf` y `Criminología y victimología.pdf` también; y `Criminología
      Preventiva II.pdf`, pese a otro hash, tiene las mismas 161 páginas y la misma
      portada. Ninguna de las diez está en la bibliografía oficial de los cuatro
      programas recibidos, y ninguna cubre los vacíos declarados en [[purpose]].

      **Zaffaroni es una falsa coincidencia.** S1.3 pide *En busca de las penas
      perdidas* (2006) y lo que llegó es *Dogmática penal y criminología cautelar*.
      Mismo patrón que `programa/S1.1` ya registró con Romero Mendoza frente a
      Alvarado: título y autor cercanos, obra distinta.

      **Recomendación, en tres grupos.**
      · **Admitir como P3, material de apoyo (2).** *Criminología ambiental* de
        Vozmediano y San Juan es un manual académico consolidado, y la criminología
        ambiental es precisamente el marco teórico del enfoque territorial del módulo 3
        y de la prevención situacional del módulo 6; es además la casa teórica de
        Clarke (1997) y Weisburd y otros (2016), ambos en el corpus. *Criminología
        mediática y victimología del miedo* de Gaibor ancla a [[miedo-social]] y al
        cúmulo `Medición e inseguridad`. Ninguna es bibliografía obligatoria: entrarían
        detrás de todo lo oficial, nunca por delante.
      · **Decidir con criterio propio (1).** Zaffaroni es autor central de S1.3 y esta
        obra no es la pedida. Admitirla es defendible como lectura de apoyo; usarla
        como sustituto de *En busca de las penas perdidas* no lo es.
      · **Dejar fuera (7).** El resto —la colección de criminologías específicas, el
        manual introductorio, el módulo docente de la UOC, *Criminología empresarial*,
        el libro de divulgación de Planeta y el trabajo de fin de grado de la
        Universidad del País Vasco— cae en lo que [[purpose]] declara expresamente
        fuera: ampliación temática que no se ancla a un ramo de la malla ni al trabajo
        de grado. Dos de ellos no son citables en un trabajo evaluado bajo ningún
        criterio: un TFG de pregrado y un libro de gran público.

      **Higiene, independientemente de lo anterior.** Las tres copias de *Criminología
      preventiva* y las dos de Gaibor deberían quedar en una sola cada una. Mientras no
      se resuelva, el corpus cuenta cinco documentos donde hay dos, y `ESTADO.md`
      reportará avances sobre archivos duplicados. El cruce de MD5 sobre los 106
      archivos confirma que no hay ningún otro duplicado en el corpus y que ninguno de
      los trece repite un documento preexistente.

      **Lo que añade la identificación por página de imprenta** (12-09-2026, segunda
      pasada). Refuerza el primer grupo y matiza el tercero:
      · *Criminología ambiental* queda plenamente identificada —Editorial UOC, primera
        edición castellana de mayo de 2010, ISBN 978-84-9788-847-5—. Es manual de
        editorial universitaria, no material suelto, y eso sostiene la recomendación de
        admitirla.
      · *Criminología preventiva* resultó más institucional de lo que parecía:
        Universidad de San Martín de Porres, Fondo Editorial, 2022, ISBN peruano. Sigue
        sin estar en ningún programa, pero la razón para dejarla fuera es de alcance, no
        de calidad editorial.
      · **Tres de las diez obras salen de la misma órbita de autor:** Hikal firma
        *Criminología psicológica* e *Introducción al estudio de la criminología*, y
        codirige la colección donde aparece *Criminología preventiva*. Con el libro de
        divulgación y el trabajo de fin de grado, el conjunto se parece más a una
        adquisición en bloque que a una bibliografía curada, que es justamente lo que
        [[purpose]] describe como ampliación temática por interés propio.
      **Resuelto el 13-09-2026 — `preguntar`, respondido.** Decision del autor: la cuarentena se
      mantiene **sin plazo**. Son en su mayoria manuales genericos y la pertinencia se
      verifica obra por obra, contra el documento y no contra su ficha. Deja de
      bloquear: el corpus sigue declarando trece documentos sin estatus y eso es
      aceptado a sabiendas. La higiene de duplicados sigue pendiente y viaja con este
      item. La recomendacion en tres grupos queda intacta arriba, para cuando se
      retome.

- [x] **[ingesta]** Bibliografía de consulta de S1.1 como ancla teórica — el autor
      plantea que las obras de consulta del programa ancla sirven de ancla teórica
      de todo el corpus, y duda de levantar la ingesta con ellas por su extensión.
      La duda está bien fundada y son tres casos distintos, no uno.
      Acción propuesta: `preguntar` · Origen: sesión 2026-09-12
      Recomendación registrada:
      · **García-Pablos de Molina (2003)**, 113,7 MB y extracto desde la p. 688, es
        el caso problemático. No conviene ingerirlo como fuente única: un tratado
        que recorre el arco teórico completo fijaría el encuadre de todo lo
        posterior, que es exactamente el riesgo que [[purpose]] declara al ordenar
        la ingesta en orden inverso al volumen. Tratarlo como obra de referencia y
        ingerirlo por capítulos atados a un módulo concreto, no entero.
      · **Guía ONU-Hábitat y Guadalajara (2020)**, 1,8 MB, operacionaliza el trabajo
        evaluado de S1.1. Barata y de rendimiento inmediato: entra sin reparos.
      · **Garland (2001)** es la bisagra —única obra en dos programas oficiales— y
        merece ingesta completa, pero después del núcleo ancla, no antes.
      Criterio: lo anterior es una recomendación de orden, no una decisión. La toma
      el autor.
      **Resuelto el 13-09-2026 — `omitir` parcialmente.** Decision del autor sobre los
      tres casos: la Guia ONU-Habitat ya entro (12-09-2026) y la recomendacion se
      cumplio; Garland completo sigue en el orden; y **Garcia-Pablos cambia de
      tratamiento**. No se ingiere por capitulos como recomendaba este item, porque el
      documento esta incompleto —extracto desde la p. 688—: queda en espera hasta que
      el autor consiga el resto de la bibliografia de consulta, y entonces entra
      completo y como base fundamental. Registrado en [[purpose]].
