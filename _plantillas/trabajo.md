<%*
// Una sola plantilla para los dieciseis ramos. trabajos/ es plana: el codigo de
// asignatura sale del prefijo del nombre del archivo. Si la nota nacio sin ese
// prefijo —por ejemplo, invocando la plantilla desde la paleta de comandos— se
// pregunta y despues se mueve.
const RAMOS = {
  "S1.1": ["Intro Criminología", "malla/sem1/s1-1"],
  "S1.2": ["Medición y Análisis", "malla/sem1/s1-2"],
  "S1.3": ["Sistema Penal", "malla/sem1/s1-3"],
  "S2.1": ["Violencia Urbana", "malla/sem2/s2-1"],
  "S2.2": ["Victimología", "malla/sem2/s2-2"],
  "S2.3": ["Prevención Local", "malla/sem2/s2-3"],
  "S2.4": ["Violencia Juvenil", "malla/sem2/s2-4"],
  "S3.1": ["Diseño Proyectos", "malla/sem3/s3-1"],
  "S3.2": ["Salud Mental", "malla/sem3/s3-2"],
  "S3.3": ["Violencia Género", "malla/sem3/s3-3"],
  "S3.E1": ["Electivo Cárceles", "malla/sem3/s3-e1"],
  "S3.E2": ["Electivo Migración", "malla/sem3/s3-e2"],
  "S3.E3": ["Electivo Policía", "malla/sem3/s3-e3"],
  "S3.E4": ["Electivo Crimen Organizado", "malla/sem3/s3-e4"],
  "SEM": ["Seminario", "malla/seminario"],
  "S4": ["Trabajo Grado", "malla/trabajo-grado"]
};

const TIPOS = {
  "Análisis crítico de una investigación": "analisis-critico",
  "Diseño de investigación aplicada": "diseno-investigacion",
  "Reseña audiovisual": "resena-audiovisual",
  "Trabajo de investigación final": "investigacion-final",
  "Ensayo": "ensayo",
  "Preparación de prueba": "preparacion-prueba",
  "Otro": "otro"
};

const ESQUEMAS = {
  "analisis-critico": "## Investigación analizada\n\n_(referencia APA 7 completa del artículo o informe que se analiza)_\n\n## Problema y pregunta\n\n## Diseño metodológico declarado\n\n## Evidencia y resultados\n\n## Crítica\n\nFortalezas, límites y supuestos no declarados. Cada juicio se sostiene en un pasaje concreto, con página.\n\n## Conclusión\n\n## Referencias\n",
  "diseno-investigacion": "## Problema\n\n## Pregunta e hipótesis\n\n## Objetivos\n\nGeneral y específicos.\n\n## Marco conceptual\n\n## Diseño metodológico\n\nEnfoque, alcance, unidad de análisis, muestra, técnicas de producción de datos y plan de análisis.\n\n## Anclaje empírico\n\nPolítica, programa o proyecto concreto sobre el que se aplica.\n\n## Cronograma\n\n## Consideraciones éticas\n\n## Referencias\n",
  "resena-audiovisual": "## Obra reseñada\n\nTítulo, dirección, año, país, duración.\n\n## Sinopsis\n\nBreve y sin juicio.\n\n## Análisis desde los contenidos del curso\n\nConceptos del curso que la obra permite discutir, cada uno anclado a una escena o secuencia concreta.\n\n## Tensiones y omisiones\n\n## Conclusión\n\n## Referencias\n",
  "investigacion-final": "## Problema\n\n## Pregunta\n\n## Marco teórico\n\n## Método\n\n## Desarrollo\n\n## Conclusiones\n\n## Referencias\n",
  "ensayo": "## Tesis\n\nUna sola oración.\n\n## Argumento\n\n## Objeciones\n\n## Conclusión\n\n## Referencias\n",
  "preparacion-prueba": "## Contenidos que entran\n\n## Conceptos por definir\n\n## Autores y posiciones\n\n## Preguntas probables\n\n## Vacíos detectados\n",
  "otro": "## Desarrollo\n\n## Referencias\n"
};

let ramo = "", etiqueta = "", carpeta = "", titulo = "", tipo = "otro", ponderacion = "", entrega = "";

try {
  const actual = tp.file.folder(true);
  const codigo = tp.file.title.split(" - ")[0].trim();

  if (codigo && RAMOS[codigo]) {
    ramo = codigo;
  } else {
    const codigos = Object.keys(RAMOS);
    const rotulos = codigos.map(c => `${c} — ${RAMOS[c][0]}`);
    ramo = await tp.system.suggester(rotulos, codigos, false, "¿De qué ramo es el trabajo?");
    if (!ramo) throw new Error("no se eligió ramo");
  }
  etiqueta = RAMOS[ramo][1];
  carpeta = "trabajos";

  const nombres = Object.keys(TIPOS);
  const elegido = await tp.system.suggester(nombres, nombres, false, "Tipo de trabajo");
  if (!elegido) throw new Error("no se eligió tipo");
  tipo = TIPOS[elegido];

  titulo = await tp.system.prompt("Título del trabajo", elegido);
  if (!titulo) titulo = elegido;
  ponderacion = await tp.system.prompt("Ponderación en porcentaje (vacío si no aplica)", "") || "";
  entrega = await tp.system.prompt("Fecha de entrega AAAA-MM-DD (vacío si no se conoce)", "") || "";

  let nombre = `${ramo} - ${titulo}`;
  if (tp.file.find_tfile(`${carpeta}/${nombre}`)) nombre += ` ${tp.date.now("HH.mm")}`;
  if (actual === carpeta) await tp.file.rename(nombre);
  else await tp.file.move(`${carpeta}/${nombre}`);
} catch (e) {
  new tp.obsidian.Notice(`Plantilla de trabajo: ${e.message}`, 10000);
}
-%>
---
titulo: <% titulo %>
tipo: <% tipo %>
ramo: <% ramo %>
ponderacion: <% ponderacion %>
entrega: <% entrega %>
estado: sin empezar
nota:
tags:
  - trabajo
  - <% etiqueta %>
creado: <% tp.date.now("YYYY-MM-DD HH:mm") %>
---

# <% titulo %>

<% ESQUEMAS[tipo] %>
