# Esquema

Reglas estructurales de la wiki. El propósito —para qué existe— está en
[[purpose]].

## Disposición y divergencias

La wiki se opera con Obsidian y se mantiene compatible con la aplicación LLM Wiki,
cuyos nombres de archivo y de carpeta están comprometidos en su código. De ahí que
los directorios y el campo `type` estén en inglés mientras el contenido se redacta
en español.

```
MagisterLeo/
├── purpose.md          # propósito, preguntas rectoras, alcance
├── schema.md           # este archivo
├── MANIFIESTO.json     # hashes de fuentes ingeridas
├── INVENTARIO.md       # el corpus y sus cúmulos
├── raw/
│   ├── sources/        # fuentes inmutables, plano, sin subcarpetas
│   └── assets/         # figuras extraídas y adjuntos, se crea al necesitarse
├── despliegue/fase1/   # análisis de fase 1 persistidos, se crea al ingerir
└── wiki/
    ├── index.md  log.md  overview.md  pendientes.md  revision.md  referencias.md
    ├── entities/  concepts/  methodology/  sources/
    └── queries/  synthesis/  comparisons/  thesis/
```

Dos divergencias respecto de la disposición por defecto de la skill, ambas
deliberadas:

1. **Las fuentes viven en `raw/sources/`, no en `sources/`.** El vault es anterior
   a la wiki y `raw/` es su componente de entrada.
2. **`raw/sources/` es plano.** No hay subcarpetas y no se admiten. Las figuras
   que se extraigan de una fuente van a `raw/assets/`, fuera del corpus, que es
   además la carpeta de adjuntos configurada en Obsidian. La taxonomía
   del corpus está en `INVENTARIO.md`. Esto invalida la heurística de la skill que
   usa la ruta de carpeta como pista de clasificación: **el cúmulo de
   `INVENTARIO.md` cumple esa función**, y es también el que agrupa el informe de
   `scripts/estado.py`.

El campo `carpeta_bib`, que registraba la carpeta de origen, quedó retirado el
05-09-2026 al aplanarse el corpus. No se vuelve a escribir.

## Tipos de página

| `type` | Carpeta | Qué es |
|---|---|---|
| `source` | `wiki/sources/` | Una ficha por fuente ingerida. Se crea siempre |
| `entity` | `wiki/entities/` | Personas, organismos, políticas, programas, territorios |
| `concept` | `wiki/concepts/` | Ideas, teorías, marcos analíticos |
| `method` | `wiki/methodology/` | Instrumentos y procedimientos de medición y análisis |
| `query` | `wiki/queries/` | Consultas archivadas con su respuesta |
| `synthesis` | `wiki/synthesis/` | Síntesis transversal a varias fuentes |
| `comparison` | `wiki/comparisons/` | Confrontación explícita de dos o más posiciones |
| `thesis` | `wiki/thesis/` | Posición del autor. Prefijo `tesis-`, `procedencia: autor` |

Ocho tipos, uno por carpeta. No se crean tipos nuevos sin pasar por la operación 8.

Las políticas, programas y proyectos no tienen tipo propio: son `entity` con
`subtipo`. Distinguirlos importa porque el anclaje empírico del trabajo de grado
recae sobre uno de ellos.

El perfil de posgrado por asignaturas sugiere tipos propios `norma`, `politica` y
`caso` para dominios de política pública. No se adoptan todavía: con tres páginas
en la wiki, declarar once tipos es sobreajuste. Se reevalúan por la operación 8
cuando se elija el caso de anclaje del trabajo de grado, que es el momento en que
la distinción empieza a hacer trabajo.

`subtipo` admitido en `entity`: `persona`, `organismo`, `politica`, `programa`,
`territorio`.

## Frontmatter

Tres campos son estructurales y no se renombran ni se traducen: `title`, `type`,
`sources`. Alimentan el modelo de relevancia y la ingesta incremental.

```yaml
---
title: Título legible
type: source | entity | concept | method | query | synthesis | comparison | thesis
sources: ["2016 - Weisburd y otros - El lugar importa....pdf"]
cluster: nombre-del-clúster
curso: [s1-1, s2-3]          # o [transversal], o [] si no alimenta ningún ramo
procedencia: fuentes | autor | mixta
estado: borrador | revisado | estable
creado: YYYY-MM-DD
actualizado: YYYY-MM-DD
---
```

`sources` lleva el **nombre de archivo exacto** tal como está en `raw/sources/`,
con extensión. Es la llave contra `MANIFIESTO.json` y contra `INVENTARIO.md`.

Campos adicionales según tipo:

- `entity`: `subtipo`, `alias`.
- `source`: `autor`, `anio`, `titulo_original`, `editorial`, `idioma_fuente`,
  `apa`, `verificacion_bibliografica`, `truncado`.
- `thesis`: `refuta`, `sostenida_por`.

### Vigencia

`vigencia: vigente | superado | incierto` es **obligatorio** en las páginas que
describen política pública chilena o cifras oficiales —`entity` con `subtipo`
`politica` o `programa`, y las fichas de fuentes estadísticas— y no se usa en el
resto. La teoría criminológica no caduca; la ENUSC y las orientaciones técnicas de
la Subsecretaría, sí.

Regla: las afirmaciones no se corrigen sobre sí mismas. La versión anterior se
conserva marcada como superada, con la fecha y la fuente que la superó.

## Nomenclatura

Páginas: slug en minúsculas, sin tildes ni eñes, palabras unidas por guion.
`prevencion-situacional`, `subsecretaria-prevencion-del-delito`. El `title` del
frontmatter lleva la forma legible, con tildes.

Las páginas de tesis llevan prefijo `tesis-`.

Las fichas de fuente toman un slug corto y estable, no el nombre del archivo:
`2016 - Weisburd y otros - El lugar importa, criminología para el siglo XXI.pdf`
produce `weisburd-el-lugar-importa`.

## Clústeres declarados

El clúster agrupa por estructura del problema. La cobertura curricular la mide el
campo `curso`, que es un eje distinto y no se confunde con este.

| Clúster | Qué reúne |
|---|---|
| `marco-institucional` | El programa, su malla, las exigencias del trabajo de grado |
| `explicacion-del-delito` | Teorías criminológicas y etiología del delito |
| `prevencion` | Prevención situacional, social, comunitaria y local |
| `medicion-y-metodo` | Metodología de investigación, medición y análisis delictual |
| `sistema-penal` | Política criminal, garantismo, expansión punitiva |
| `victimizacion-e-inseguridad` | Victimización, miedo al delito, percepción |
| `gobernanza-criminal` | Crimen organizado, control territorial, orden crimilegal |
| `caso-de-grado` | El anclaje empírico del trabajo de grado |

`caso-de-grado` está declarado y vacío a propósito: es el vacío más importante del
proyecto y conviene que se vea.

Un clúster vacío es un vacío visible. Los ramos sin material se detectan por el
campo `curso`, no creando clústeres por asignatura.

## Trazabilidad

Ninguna afirmación sustantiva queda sin marca. Notas al pie nombradas, numeración
local a cada página desde 1:

```markdown
El lugar concentra el delito más que las personas [^ext-1].
Probablemente sea trasladable a comunas chilenas [^inf-1].

[^ext-1]: **Extraído** — [[weisburd-el-lugar-importa]], p. 45.
[^inf-1]: **Inferido** (confianza 0.6) — combinando [[weisburd-el-lugar-importa]] y
    [[guerra-modelo-las-condes]].
```

`ext` extraído · `inf` inferido, con confianza entre 0.0 y 1.0 · `amb` ambiguo.

## Citación

APA 7. Una cita textual por página como máximo, de quince palabras o menos, entre
comillas y con página. `wiki/referencias.md` mantiene la bibliografía completa.

**Divergencias de edición.** Cuando el corpus tiene la obra que el programa pide
pero en otra edición o traducción, la ficha lleva
`verificacion_bibliografica: pendiente` y la divergencia se anota en el cuerpo. No
se resuelve por inferencia: la resuelve el autor contra el documento. Casos
conocidos: Ferrajoli, Baratta, Pavarini y Srur.

**Fuentes en otro idioma.** El corpus está renombrado con títulos en español
aunque muchas obras sean inglesas. En `apa` va el título original; en `title`, el
español.

## Exportación

Las páginas de la wiki no se citan en trabajos evaluados: se cita la obra. Los
wikilinks desaparecen al exportar con Pandoc, y las notas al pie nombradas
sobreviven. Ver `trabajos/_recursos/citar.md`.

Las páginas `procedencia: autor` y `procedencia: mixta` no son bibliografía. Las
segundas son síntesis del LLM sobre resultados de terceros y deben sustituirse por
la fuente original antes de citarse.

## Validación

`python scripts/validar_frontmatter.py wiki/` comprueba estas reglas: campos
estructurales, tipos, clústeres declarados, subtipos, vigencia obligatoria,
prefijo `tesis-`, separación de procedencia y notas de inferencia con confianza
declarada. Con `--estricto` falla además ante `verificacion_bibliografica:
pendiente`.

Este archivo es la autoridad; el validador lo codifica. Si divergen, se corrige el
validador.
