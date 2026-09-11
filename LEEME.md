# MagisterLeo

Vault de Obsidian del Magíster en Prevención del Delito y la Violencia, Universidad
Alberto Hurtado, cohorte 2026. Cuatro componentes con una dependencia que no se
invierte: `raw/` alimenta a `wiki/`, y `wiki/` y `clases/` alimentan a `trabajos/`.

## Estructura

```
MagisterLeo/
├── purpose.md          # para qué existe la wiki: preguntas rectoras y alcance
├── schema.md           # cómo funciona: tipos, frontmatter, clústeres, citación
├── INVENTARIO.md       # el corpus: 83 documentos, cúmulos y MD5
├── MANIFIESTO.json     # qué se ingirió y con qué hash
├── ESTADO.md           # vista derivada del avance. La escribe scripts/estado.py
├── LEEME.md            # este archivo
├── _plantillas/        # 17 plantillas de Templater: 16 de clase y una de trabajo
├── clases/             # apunte propio, plano. Panel: Clases.md
├── programa/           # una ficha por ramo: programa oficial, bibliografía, brecha
├── raw/sources/        # corpus de fuentes, plano e inmutable
├── scripts/            # manifiesto, estado, grafo y validación de frontmatter
├── trabajos/           # entregables evaluados, planos. Panel: Trabajos.md
└── wiki/               # conocimiento con procedencia; sólo lo que sostiene una fuente
```

**Todo es plano.** Ninguna carpeta por ramo, en ningún componente. El código de
asignatura —`S1.1`, `S3.E4`— vive en el prefijo del nombre del archivo y en la
etiqueta `malla/…` del frontmatter, que es lo que cruza apuntes, trabajos y fichas.
Agrupar por carpeta obligaba a mantener treinta y dos directorios que casi siempre
estaban vacíos.

## raw/sources

Carpeta inmutable y sin subcarpetas: aquí no se edita, no se anota y no se convierte
nada. La taxonomía del corpus vive en `INVENTARIO.md`, no en el árbol de archivos.

Nomenclatura: `año - autor - título en español.ext`. Sin año verificable, `s.f.`; sin
autor verificable, `Autor por identificar`. El título va en español aunque la obra
esté en otro idioma, y los dos puntos del subtítulo se sustituyen por coma.

## programa/

Una ficha por ramo, con el mismo nombre que la asignatura. Declara el programa oficial
—`programa_recibido: sí|no`—, la bibliografía obligatoria cotejada contra el corpus y
la ponderación P1/P2/P3 de cada documento. Mientras una ficha siga en
`programa_recibido: no`, su bibliografía no puede ponderarse: no hay contra qué
contrastarla.

Los programas oficiales en PDF no viven aquí sino en `raw/sources`, como cualquier
otra fuente.

## Plantillas

Templater se dispara por **patrón de nombre**, no por carpeta: la regla
`^clases/S1.1 ` aplica la plantilla de Introducción a la criminología a cualquier nota
que nazca con ese prefijo. Las reglas están en
`.obsidian/plugins/templater-obsidian/data.json`, campo `file_templates`.

En un equipo nuevo, si los botones «+ Nueva clase» crean notas vacías, es que el
disparador está apagado: Ajustes → Templater → *Trigger Templater on new file
creation*, y el modo debe quedar en *File regex templates*.

## Exportar trabajos

```bash
python trabajos/_recursos/exportar.py --todos --ramo S1.2
```

Requiere Pandoc, y LibreOffice para PDF con plantilla. El original es siempre el
Markdown; `trabajos/_export/` es desechable y se regenera.

## La wiki

`wiki/` compila el corpus en conocimiento con procedencia. Se opera con la skill
`llm-wiki` y se mantiene compatible con la aplicación LLM Wiki, de ahí que las
carpetas y el campo `type` estén en inglés y el contenido en español.

Dos archivos la gobiernan y conviene no confundirlos: `purpose.md` dice **para
qué** existe —qué merece página y qué no— y `schema.md` dice **cómo** funciona.
Leer el primero antes de cada ingesta.

```bash
python scripts/manifiesto.py raw/sources --manifiesto MANIFIESTO.json   # qué falta ingerir
python scripts/estado.py                                                # avance por cúmulo
python scripts/validar_frontmatter.py wiki                              # invariantes del esquema
python scripts/grafo.py wiki                                            # diagnóstico del grafo
```

El corpus está desbalanceado —42 de 83 documentos vienen de un taller electivo de
doce horas— y por eso el orden de ingesta es inverso al volumen. Está fijado en
`purpose.md` y no conviene alterarlo: empezar por el bloque grande sesgaría la
clasificación de todo lo demás.
