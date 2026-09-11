<%*
// Nombra la nota y la deja en clases/, que es plana: el ramo va en el
// prefijo del nombre, no en una carpeta.
//
// Funciona por dos vías: cuando Templater se dispara al crear el archivo, y
// cuando la plantilla se invoca a mano desde la paleta de comandos. En el
// segundo caso la nota nace donde Obsidian ponga los archivos nuevos, asi que
// ademas se mueve. Si algo falla, avisa en pantalla en vez de dejar una nota
// vacia sin explicacion.
const ramo = "Medición y Análisis";
const codigo = "S1.2";
const carpeta = "clases";
try {
  let nombre = `${codigo} - ${tp.date.now("YYYY-MM-DD")} ${ramo}`;
  if (tp.file.find_tfile(`${carpeta}/${nombre}`)) nombre += ` ${tp.date.now("HH.mm")}`;
  if (tp.file.folder(true) === carpeta) await tp.file.rename(nombre);
  else await tp.file.move(`${carpeta}/${nombre}`);
} catch (e) {
  new tp.obsidian.Notice(`Plantilla de ${ramo}: no se pudo nombrar la nota. ${e.message}`, 10000);
}
-%>
---
creado: <% tp.date.now("YYYY-MM-DD HH:mm") %>
ramo: Medición y Análisis
tags:
  - clase
  - malla/sem1/s1-2
---

