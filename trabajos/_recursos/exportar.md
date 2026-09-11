# Exportar un trabajo

El Markdown es el original. El `.docx` y el `.pdf` son derivados: se generan, se
entregan y se descartan. `_export/` está fuera del control de versiones por eso.

```
Markdown ──pandoc──▶ .docx (con los estilos de la plantilla) ──soffice──▶ .pdf
```

## Comandos

```bash
# un trabajo a Word, con el formato institucional si hay plantilla
python trabajos/_recursos/exportar.py "trabajos/S1.2 - Medición y Análisis/S1.2 - Análisis crítico de una investigación.md"

# el mismo, a PDF
python trabajos/_recursos/exportar.py "<nota>" --formato pdf

# todos, o sólo los de un ramo
python trabajos/_recursos/exportar.py --todos
python trabajos/_recursos/exportar.py --todos --ramo S1.2

# con otra plantilla, o sin ninguna
python trabajos/_recursos/exportar.py "<nota>" --plantilla "ruta/otra.dotx"
python trabajos/_recursos/exportar.py "<nota>" --sin-plantilla
```

La salida cae en `trabajos/_export/`.

## La plantilla institucional

Deja **`plantilla.dotx`** —o `plantilla.docx`— en `trabajos/_recursos/` y el
exportador la toma sin más argumentos. No hace falta configurar nada.

**Por qué el script convierte el `.dotx`.** Pandoc sólo admite `.docx` como
documento de referencia. Un `.dotx` es el mismo paquete OOXML: sólo declara otro
tipo de contenido para su parte principal. El exportador reescribe esa
declaración sobre una copia en caché —`_export/.plantilla/`— y le entrega esa
copia a Pandoc. **Tu `.dotx` no se modifica nunca.** La caché se regenera sola
cuando la plantilla cambia.

**Por qué el PDF pasa por Word y no por LaTeX.** Con plantilla, el PDF se produce
desde el `.docx` ya maquetado, con LibreOffice, y conserva el formato. Sin
plantilla cae a la vía LaTeX de Pandoc, que ignora por completo los estilos de
Word. Si el formato importa, exporta con plantilla.

## Qué debe definir la plantilla

Pandoc no copia el contenido de la plantilla: **copia sus estilos, por nombre.**
Un estilo que la plantilla no defina sale con el aspecto por defecto de Word. Los
que este proyecto usa de verdad:

| Estilo | Dónde aparece |
|---|---|
| `Title` | El título del trabajo, que sale del campo `titulo` |
| `Heading 1` … `Heading 3` | Las secciones del esqueleto |
| `Normal`, `Body Text`, `First Paragraph` | El cuerpo |
| `Footnote Text`, `Footnote Reference` | Las citas. **Es el estilo que más importa** |
| `Block Text` | Las citas en bloque y los recuadros de exigencias |
| `Hyperlink` | Los enlaces |
| `Compact` | Las listas apretadas |
| `Caption`, `Table Caption` | Pies de tabla y de figura |
| `Source Code`, `Verbatim Char` | Código, que en estos trabajos casi no aparece |

Márgenes, tamaño de página, interlineado, numeración de páginas y encabezados se
heredan de la plantilla, no de los estilos: basta con que estén configurados en
ella.

**Al construirla:** parte de un documento en blanco de Word, ajusta esos estilos,
configura márgenes y encabezado, y guarda como `.dotx`. No hace falta escribir
contenido; lo que se escriba se descarta.

## Qué transforma antes de convertir

- Retira el frontmatter y lo convierte en una portada breve: asignatura, tipo,
  ponderación y fecha de entrega.
- Reduce los enlaces de Obsidian: `[[pagina|texto]]` queda en «texto»,
  `[[pagina]]` en «pagina». Ver `citar.md`.
- Deja intactas las notas al pie, que son Markdown estándar y Pandoc convierte en
  notas reales de Word.

No toca la nota original: lee, transforma en memoria y escribe aparte.

## Requisitos

| Salida | Necesita |
|---|---|
| `.docx`, con o sin plantilla | Pandoc |
| `.pdf` con plantilla | Pandoc y LibreOffice |
| `.pdf` sin plantilla | Pandoc y un motor LaTeX |

Los tres están disponibles en el entorno de la sesión asistida. En Windows hay
que instalarlos aparte para exportar sin asistencia; Word convierte a PDF por su
cuenta, así que basta con el `.docx`.

## Antes de entregar

Abrir el `.docx` y revisar tres cosas: que la portada diga lo que corresponde,
que las notas al pie estén numeradas de corrido, y que no haya quedado el nombre
de una página de la wiki suelto en una oración —eso delata una cita faltante—.
