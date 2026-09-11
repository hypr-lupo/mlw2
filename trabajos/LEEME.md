# trabajos/

Componente de salida. Aquí viven los entregables evaluados: los trabajos de cada
asignatura y, más adelante, el trabajo de grado. No es wiki, no es corpus y no es
apunte de clase.

## Tres reglas

1. **El original es el Markdown.** El `.docx` o el `.pdf` son derivados: se generan
   con `_recursos/exportar.py`, se entregan y se descartan. Nunca se editan a mano
   ni se versionan. `_export/` está fuera del control de versiones.

2. **Se cita el documento, nunca la wiki.** Un enlace `[[pagina]]` sirve para
   navegar dentro de Obsidian y desaparece al exportar. La referencia bibliográfica
   va al pie, en APA 7, y apunta a la obra original. La wiki apoya la redacción; no
   la acredita. Citar una página de la wiki en un trabajo evaluado sería citar un
   apunte propio como si fuera literatura.

3. **La dependencia es unidireccional y no se invierte.** Este componente lee
   `wiki/` y `clases/`; ninguno de los dos lo lee a él. `wiki/` en particular debe
   seguir funcionando de forma autónoma, sin conocer la existencia de esta carpeta.

## Estructura

```
trabajos/
├── Trabajos.md         # panel: un botón por ramo y el estado de cada entregable
├── Trabajos.base       # tabla filtrable por ramo, tipo, ponderación y estado
├── _recursos/          # cómo citar, cómo exportar, exportar.py y plantilla.docx
├── _export/            # derivados .docx y .pdf. Lo crea exportar.py; desechable
└── S1.2 - ....md       # un archivo por entregable, el ramo en el nombre
```

## Nomenclatura

`<código de ramo> - <título del trabajo>`. Ejemplo:
`S1.2 - Análisis crítico de una investigación`.

El código de ramo encabeza el nombre y es lo único que agrupa por asignatura: la
carpeta es plana. De ahí depende también el filtro `--ramo` de `exportar.py` y el
cruce con la etiqueta `malla/…` que llevan los apuntes de clase.

## Ciclo de vida

`sin empezar` → `en borrador` → `en revisión` → `entregado` → `calificado`

El campo `estado` del frontmatter lo declara y `Trabajos.base` lo muestra. Al pasar
a `calificado` se agrega `nota:`. Ningún trabajo se borra tras la entrega: la serie
completa es el registro del avance académico.

## Qué no vive aquí

Los apuntes de clase, que van en `clases/`. Las fichas de fuentes, que van en
`wiki/sources/`. Las fichas de cada ramo del programa, que van en `programa/`.
Y la bibliografía, que vive en `raw/` y no se copia: se enlaza.
