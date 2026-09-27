---
operacion: auditoria
fecha: 2026-09-27
paginas: 51
fuentes_ingeridas: 14
corpus: 117
commit_base: 220fb7d
---

# Auditoría de la wiki — 27-09-2026

Operación 7 de la skill, ejecutada a pedido del autor al cerrar la tanda 1. Con 51 páginas
la revisión es cualitativa, apoyada en `scripts/grafo.py`, `scripts/validar_frontmatter.py`
y un cotejo propio de índice, fichas, referencias, citas y procedencia. La skill pide
reportar como lista priorizada y corregir sólo con aprobación. Lo que se corrigió en esta
misma pasada son errores mecánicos o de mantenimiento, sin decisión de contenido; está
marcado **[corregido]**. Todo lo demás queda propuesto.

## Estado general

| Medida | Valor |
|---|---|
| Páginas | 51: 32 conceptos, 4 métodos, 1 entidad, 14 fichas |
| Fuentes ingeridas | 14 de 117 documentos; 98 pendientes de un universo de 111 |
| Estado | 42 revisadas, 9 en borrador |
| Procedencia | 51 `fuentes`; ninguna `autor` ni `mixta` |
| Grado medio | 10,4 |
| Páginas aisladas | 0 |
| Enlaces rotos | 0 |
| Páginas sin fuente | 0 |
| Frontmatter | 0 errores, 0 avisos |
| Notas al pie | todas definidas y usadas, sin huecos de numeración |
| Índice | 51 de 51 catalogadas, sin entradas huérfanas ni conteos de fuentes desfasados; seis entradas fuera de orden alfabético [corregido] |
| Fichas, manifiesto y referencias | 14 = 14 = 14 |
| Fuentes citadas | todas en disco y en el manifiesto |
| Verificación bibliográfica pendiente | 7 de 14 fichas |

## Hallazgos, por prioridad

### Alta

1. **La topología no confirma los clústeres.** La detección de comunidades devuelve una sola
   comunidad con las 51 páginas; con otra semilla, 48 más un grupo de 3 —la violencia en el
   noviazgo, su ficha y la ley—. 40 de 51 páginas son nodos puente. Los siete clústeres
   tienen cohesión interna aceptable (0,46 a 1,0), pero ninguno se distingue por su
   conectividad. Dos causas probables:
   - la señal de fuente compartida la dominan unas pocas obras: el libro colectivo de 2021
     está en 16 páginas, Weisburd y otros en 12, la guía de 2010 en 11, y la de 2020 y Adams
     en 9 cada una;
   - las secciones «Relacionado» enlazan con generosidad.

   No es urgente con 51 páginas de un solo campo, pero es la condición del ítem de esquema
   sobre obras colectivas. **Propuesta:** enmienda a ese ítem de [[revision]] y repetir el
   diagnóstico con 100 páginas. [enmienda aplicada en la cola]

2. **Candidatos con peso acumulado y sin página.**

   | Tema | Páginas que lo mencionan | Situación |
   |---|---:|---|
   | Prevención situacional | 13 | En cola como «teorías de la oportunidad»; espera a Clarke y Felson, tanda 4 |
   | Cohesión social | 12 | Sin página; se usa suelto entre [[capital-social]] y [[eficacia-colectiva]] |
   | Control social informal | 10 | En cola; espera a Gottfredson y Hirschi, tanda 4 |
   | Carabineros de Chile | 8 | Sin ítem. Se propone sumarlo al del Plan Cuadrante [enmienda aplicada] |
   | Fundación Paz Ciudadana | 7 | Sin página. Importa como afiliación: es la institución de autores de dos fuentes, Tudela (2015) y el cap. IV del libro de 2021 |
   | Seguridad ciudadana y seguridad humana | 5 | Sin ítem. La guía de 2010 define la seguridad ciudadana frente a la pública; la de 2020 y el libro de 2021 adoptan la humana. Son del mismo círculo de autores. Se propone `crear-pagina` con una fuente de fuera [ítem nuevo] |
   | Plan Cuadrante; Peñalolén | 6; 5 | En cola |

   La cohesión social no se propone como página: el problema es de uso. Tres fuentes la
   usan sin distinguirla de otros constructos, y la wiki ya lo registra. Paz Ciudadana
   tampoco: basta con que las fichas digan quién escribe, y lo dicen.

3. **Síntesis propias sin marca `inf`.** Un barrido de párrafos largos sin nota encontró 17
   páginas con tres o más. Casi todos son listas cuya frase de entrada sí lleva nota, o
   análisis que la página declara como de la wiki. Pero hay síntesis sustantivas sin marca,
   sobre todo en páginas del 12-09-2026:
   - [[crimen-organizado]]: «Juntos dejan al concepto sin sus dos anclas tradicionales…»;
   - [[gobernanzas-paralelas]]: «Las dos miradas son complementarias y juntas explican…»;
   - [[eficacia-colectiva]]: «Qué hacer con esto» y «Lo que se pierde en la traducción»;
   - [[zona-gris]]: el párrafo sobre el rendimiento del concepto;
   - [[policia-comunitaria]]: el patrón de reversión de las UPP.

   Son lecturas defendibles, pero la regla de procedencia pide marcarlas. **Propuesta:** una
   pasada de marcado, sin cambiar el contenido. Queda en [[pendientes]] como mantenimiento.

### Media

4. **Procedencia incompleta en dos páginas.** [corregido]
   - [[coproduccion-de-seguridad]] cita el folleto del programa en su nota ext-1 sin tenerlo
     en `sources`.
   - [[moralismo-legal]] cita a Zúñiga Núñez en su nota ext-14 sin tenerlo en `sources`.

   Se agregaron los archivos.
5. **Frases desactualizadas.** [corregido]
   - [[diagnostico-barrial]] se presentaba como la primera página de `methodology/`, con
     «hasta ahora» nada sobre producción de evidencia; hoy hay cuatro.
   - [[programa-magister-uah]] decía que Vanderschueren es autor de una fuente «aún no
     ingerida»; hoy lo es de dos, ingeridas.
   - El índice decía que la tanda 1 estaba en curso; se cerró.
6. **Campo `curso` fuera de formato.** [corregido] [[trabajo-de-grado-profesionalizante]]
   usaba `[s4/trabajo-de-grado, sem/seminario]`; se normalizó a `[s4, sem]`, como los demás.
7. **Cuatro páginas sin cita textual.** [[moralismo-legal]], [[trabajo-de-grado-profesionalizante]],
   [[magister-prevencion-uah]] y [[gardner-prohibir-inmoralidades]]. No infringe nada: la
   regla es un máximo. En la ficha de Gardner es deliberado, porque la versión de autor pide
   no citar. Sin acción.
8. **La cola de revisión creció sin orden.** 26 ítems abiertos, en orden de llegada.
   [corregido] Se añadió al inicio de [[revision]] un resumen que los agrupa por lo que los
   destraba. No se cerró ni se borró ninguno: la cola no se vacía por antigüedad.
9. **`pendientes.md` acumuló crónica de sesiones.** [corregido] Se reescribió como
   artefacto para retomar, con la estructura de la operación 9. La crónica ya estaba en
   [[log]].

### Baja

10. **Las «referencias cruzadas faltantes» son efecto de fuentes compartidas.** Las 16 pares
    que marca `grafo.py` comparten las guías o el libro de 2021 y no tienen relación
    sustantiva, salvo la ya enlazada entre [[evaluacion-de-programas]] y
    [[policia-comunitaria]]. Sin acción.
11. **Una sola entidad.** `wiki/entities/` tiene sólo [[magister-prevencion-uah]]. Los
    candidatos —Plan Cuadrante, Peñalolén, Quiero mi Barrio, Vanderschueren— esperan en la
    cola. Es coherente con la regla de la segunda fuente, pero deja la pregunta rectora 6 sin
    material propio.

## Cobertura frente a las preguntas rectoras

| Pregunta | Estado | Lo que falta, y dónde está |
|---|---|---|
| 1. Qué exige el trabajo de grado | Una página desde el folleto | Los programas de S4 y del Seminario, no recibidos |
| 2. Qué explica el delito y qué es operable | **Fuerte.** Sampson, TAS, Weisburd, desorganización, curso de vida, Adams, prevención, análisis criminal | Oportunidad (tanda 4), control (tanda 4), criminología crítica (tanda 3); tensión y cuello blanco, y criminología feminista, sin fuente en el corpus |
| 3. Qué se mide y qué queda fuera | **Débil.** Análisis espacial y criminal, evaluación, la medición por etiqueta o por conducta | INE (2023), Srur, Boba, Batthyány y Cabrera: toda la tanda 2 |
| 4. Qué tiene evidencia y cómo se transfiere | Media. Evaluación, puntos calientes, desplazamiento, la portabilidad de la eficacia colectiva | CIPC (2015), tanda 2; ninguna evaluación chilena en el corpus |
| 5. Gobernanza criminal y Estado local | Media en lo regional, nula en lo chileno | Zeballos (2024), tanda 6; Ley 21.802, tanda 5 |
| 6. Anclaje chileno | Tres candidatos en cola, ninguno con página | Es decisión del autor; `caso-de-grado` sigue vacío a propósito |

## Lo que la wiki ya responde de forma propia

Preguntas que ninguna fuente responde sola y que la wiki sí:

- **Por qué dos guías que parecen independientes son una.** La guía de 2020 reedita sin citarla la
  de 2010, y el libro de 2021 comparte autores con las dos.
- **Qué parte de la tipología barrial descansa en un supuesto discutido.** La lista de
  elementos físicos precede a la teoría de las ventanas rotas; su justificación, no.
- **Cuánto cambia una prevalencia según se pregunte.** Con datos chilenos, y con una ley que ya
  define la violencia por conductas.
- **Por qué «desplazamiento» significa cosas distintas en el libro de 2021 y en Weisburd.**
- **Qué evidencia sobre la policía se repite de fuente en fuente.** Tudela y Weisburd.
- **Qué quedó superado del estado legal del pololeo y qué no.**

## Correcciones aplicadas en esta pasada

1. `sources` de [[coproduccion-de-seguridad]] y [[moralismo-legal]].
2. Frases desactualizadas en [[diagnostico-barrial]], [[programa-magister-uah]] e [[index]].
   En el índice, además, dos conteos de fuentes que cambiaron con la corrección 1, y el
   orden alfabético de seis entradas, desordenado desde ingestas anteriores.
3. `curso` de [[trabajo-de-grado-profesionalizante]].
4. Resumen consolidado al inicio de [[revision]]; un ítem nuevo —seguridad ciudadana y humana— y dos
   enmiendas: Carabineros en el ítem del Plan Cuadrante, y la topología en el de las obras
   colectivas.
5. [[pendientes]] reescrito.
6. Entrada en [[log]].

## Pendiente de aprobación

- La pasada de marcado `inf` del hallazgo 3.
- Las decisiones de la cola que son sólo del autor: ver el grupo A del resumen de
  [[revision]].
