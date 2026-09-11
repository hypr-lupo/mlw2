---
tags:
  - panel
---

Entregables evaluados. El botón crea la nota, pregunta el tipo, el título, la
ponderación y la fecha, y arma el esqueleto correspondiente.

## Intro Criminología
*Introducción a la criminología y aspectos teóricos de la prevención*
### [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS1.1%20-%20Nuevo)

Sin programa. Evaluaciones desconocidas.

```query
path:"trabajos/S1.1 -"
```

---

## Medición y Análisis
*Metodología para la medición y análisis del delito*
### [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS1.2%20-%20Nuevo)

Dos entregables: análisis crítico (40 %) y diseño de investigación aplicada (60 %).

```query
path:"trabajos/S1.2 -"
```

---

## Sistema Penal
*Sistema penal, política criminal y Estado de derecho*
### [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS1.3%20-%20Nuevo)

Un entregable: trabajo de investigación final.

```query
path:"trabajos/S1.3 -"
```

---

## Violencia Juvenil
*Abordaje de la violencia y delincuencia adolescente y juvenil*
### [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS2.4%20-%20Nuevo)

Reseña audiovisual y prueba de contenidos. Los atrasos descuentan 0,5 por día.

```query
path:"trabajos/S2.4 -"
```

---

## Resto de la malla

Carpeta lista. El botón funciona desde el primer día de cada ramo.

| Código | Ramo | |
|---|---|---|
| S2.1 | Violencia Urbana | [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS2.1%20-%20Nuevo) |
| S2.2 | Victimología | [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS2.2%20-%20Nuevo) |
| S2.3 | Prevención Local | [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS2.3%20-%20Nuevo) |
| S3.1 | Diseño Proyectos | [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS3.1%20-%20Nuevo) |
| S3.2 | Salud Mental | [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS3.2%20-%20Nuevo) |
| S3.3 | Violencia Género | [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS3.3%20-%20Nuevo) |
| S3.E1 | Electivo Cárceles | [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS3.E1%20-%20Nuevo) |
| S3.E2 | Electivo Migración | [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS3.E2%20-%20Nuevo) |
| S3.E3 | Electivo Policía | [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS3.E3%20-%20Nuevo) |
| S3.E4 | Electivo Crimen Organizado | [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS3.E4%20-%20Nuevo) |
| SEM | Seminario | [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FSEM%20-%20Nuevo) |
| S4 | Trabajo Grado | [+ Nuevo trabajo](obsidian://new?vault=MagisterLeo&file=trabajos%2FS4%20-%20Nuevo) |

---

## Si el botón parece muerto

Misma causa que en `clases/`: quedó una nota llamada `<ramo> - Nuevo` sin renombrar. `obsidian://new` crea el archivo si no existe y lo **abre** si ya existe, de modo que una nota `Nuevo` sin renombrar bloquea el botón en silencio. Bórrela y vuelva a pulsar.

```query
path:"trabajos/" -tag:trabajo -path:"_plantillas" -path:"_recursos" -path:"_export" -file:"Trabajos" -file:"LEEME"
```

## Cómo funciona

El botón crea un archivo vacío llamado `<ramo> - Nuevo`. Templater lo detecta por ese prefijo, pregunta
el tipo de trabajo entre siete opciones, lo renombra a `<código> - <título>` y escribe
el frontmatter y el esqueleto de secciones que ese tipo pide. Una sola plantilla sirve
a los dieciséis ramos: el código de asignatura sale del nombre de la carpeta.

**Estado de cada trabajo.** El campo `estado` recorre `sin empezar`, `en borrador`,
`en revisión`, `entregado` y `calificado`. [[Trabajos.base|Trabajos]] los ordena y
filtra. Al calificar se completa `nota:`.

**Entrega.** El Markdown es el original. Para producir el `.docx` o el `.pdf` que se
entrega, `trabajos/_recursos/exportar.md` tiene el procedimiento. Los derivados van a
`_export/`, que no se versiona.

**Citación.** Se cita la obra, nunca la wiki. `trabajos/_recursos/citar.md` explica
por qué y cómo llevar una referencia desde `wiki/referencias.md` hasta el pie de un
trabajo evaluado.
