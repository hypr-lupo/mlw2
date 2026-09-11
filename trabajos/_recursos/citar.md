# Citar en un trabajo evaluado

## La regla

**Se cita la obra, nunca la wiki.**

Una página de `wiki/` es un apunte propio, por trazable que sea. Citarla en un trabajo
evaluado equivale a citarse a uno mismo como si fuera literatura, y ante un evaluador es
indefendible. La wiki sirve para encontrar la afirmación, recordar dónde estaba y
reconstruir el argumento. La referencia va siempre al documento original.

## El recorrido

1. **Localizar en la wiki.** La página lleva la afirmación con su marca de procedencia:
   `[^ext-N]` extraído, `[^inf-N]` inferido, `[^amb-N]` ambiguo. Sólo las `ext-` se citan
   sin más trabajo; las `inf-` son elaboración propia y hay que sostenerlas de otro modo.

2. **Sacar la referencia.** Está en `wiki/referencias.md`, en APA 7, junto al enlace a su
   ficha. Si la entrada arrastra `verificacion_bibliografica: pendiente`, **no se cita
   todavía**: hay que cotejarla contra el documento. Ese estado significa que la
   referencia se estableció por metadatos y no por portada.

3. **Verificar la página.** La wiki registra afirmaciones, no siempre el número de página
   exacto. Una cita textual exige abrir el documento en `raw/sources/` y anotar la página.

4. **Escribir la nota al pie.** Markdown estándar, `[^1]`. Pandoc la convierte a nota real
   en el `.docx` o el `.pdf`.

## Enlaces internos

`[[pagina]]` sirve para navegar mientras se redacta. `exportar.py` los reduce a texto
plano al exportar, de modo que no llegan al archivo entregado. Es deliberado: un enlace de
bóveda no significa nada fuera de ella.

Si al exportar aparece el nombre de una página de la wiki en medio de una oración, es
señal de que ahí faltaba una cita.

## Divergencias de edición

La ficha del ramo en `programa/` registra los casos en que el corpus tiene la obra que el
programa pide, pero en otra edición o traducción. Ferrajoli es el ejemplo: el programa
pide la de 2008 y el corpus tiene la de 1995. **Se cita la edición que se leyó**, no la
que pide el programa, y si el número de página importa se declara cuál se usó.
