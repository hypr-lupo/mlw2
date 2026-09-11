---
tags:
  - panel
---
## Intro Criminología
*Introducción a la criminología y aspectos teóricos de la prevención*
### [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS1.1%20-%20Nueva)

```query
path:"clases/S1.1 -"
```

---

## Medición y Análisis
*Metodología para la medición y análisis del delito, la inseguridad y la violencia*
### [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS1.2%20-%20Nueva)

```query
path:"clases/S1.2 -"
```

---

## Sistema Penal
*Sistema penal, política criminal y Estado de derecho*
### [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS1.3%20-%20Nueva)

```query
path:"clases/S1.3 -"
```

---

## Violencia Juvenil
*Abordaje de la violencia y delincuencia adolescente y juvenil*
### [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS2.4%20-%20Nueva)

```query
path:"clases/S2.4 -"
```

---

## Resto de la malla

Plantilla ya lista. El botón funciona desde el primer día de cada ramo.

| Código | Ramo | |
|---|---|---|
| S2.1 | Violencia Urbana | [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS2.1%20-%20Nueva) |
| S2.2 | Victimología | [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS2.2%20-%20Nueva) |
| S2.3 | Prevención Local | [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS2.3%20-%20Nueva) |
| S3.1 | Diseño Proyectos | [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS3.1%20-%20Nueva) |
| S3.2 | Salud Mental | [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS3.2%20-%20Nueva) |
| S3.3 | Violencia Género | [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS3.3%20-%20Nueva) |
| S3.E1 | Electivo Cárceles | [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS3.E1%20-%20Nueva) |
| S3.E2 | Electivo Migración | [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS3.E2%20-%20Nueva) |
| S3.E3 | Electivo Policía | [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS3.E3%20-%20Nueva) |
| S3.E4 | Electivo Crimen Organizado | [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS3.E4%20-%20Nueva) |
| SEM | Seminario | [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FSEM%20-%20Nueva) |
| S4 | Trabajo Grado | [+ Nueva clase](obsidian://new?vault=MagisterLeo&file=clases%2FS4%20-%20Nueva) |

---

## Si el botón parece muerto

Tiene una sola causa y se reconoce de inmediato: **quedó una nota llamada `<ramo> - Nueva` sin renombrar.**

El botón usa `obsidian://new`, que crea el archivo si no existe y lo **abre** si ya existe. En marcha normal eso no molesta, porque la plantilla renombra la nota a `AAAA-MM-DD <ramo>` y `Nueva` deja de existir en el mismo instante. Pero si la plantilla no corre —por ejemplo, con el disparador de Templater apagado—, `Nueva` se queda ahí vacía y a partir de entonces cada clic la abre en lugar de crear nada. El botón deja de responder para siempre, sin error.

**Solución:** borrar la nota `Nueva` y volver a pulsar. Si vuelve a aparecer, es que el disparador sigue apagado: ver «Plantillas» en `LEEME.md`, en la raíz.

Estas notas quedaron sin plantilla y no deberían existir:

```query
path:"clases/" -tag:clase -file:"Clases"
```

## Cómo funciona

El botón crea un archivo vacío llamado `<ramo> - Nueva`. Templater lo detecta por el prefijo del ramo, lo renombra a
`AAAA-MM-DD <ramo>` y le escribe `creado`, `ramo` y las etiquetas `clase` y `malla/…`. Nada más:
el cuerpo queda en blanco.

La nota sirve para las dos cosas: preparar la clase y escribir durante la sesión sincrónica. Lo
habitual es abrirla el día que empiezas a preparar y seguir en la misma durante la clase; entonces
`creado` marca la preparación y `modificado` la última vez que la tocaste. Si prefieres separarlas,
basta con pulsar el botón dos veces: la segunda nota del mismo día lleva la hora en el nombre.

**Buscar por contenido.** [[Clases.base|Clases]] no puede: una base sólo ve el nombre, la ruta, las
fechas, el tamaño, las etiquetas y las propiedades de cada archivo, nunca su texto. Para buscar
dentro de las notas, el buscador de Obsidian.

El código de la malla —`S1.1`, `S3.E4`— no desaparece: vive en la etiqueta `malla/…` de cada nota,
que es lo que permite cruzarlas con las fichas de `programa/`, con `INVENTARIO.md` y con el
campo `curso:` de la wiki.

La fecha de última modificación no se guarda como propiedad —se quedaría vieja al primer cambio—.
La lleva el sistema de archivos y se ve en la columna `modificado` de [[Clases.base|Clases]] y
ordenando el explorador por fecha de modificación.

Las plantillas están en `_plantillas/`, en la raíz del vault, una por ramo. Templater ya no las
asocia por carpeta sino por el prefijo del nombre, que es lo que permite que `clases/` sea plana.
Para cambiar qué propiedades se escriben, se edita ahí.

Esta carpeta es apunte propio y queda fuera de `wiki/`, que sólo admite lo que sostiene una fuente
ingerida. Lo que de una clase merezca llegar a la wiki se anota en `wiki/pendientes.md`.
