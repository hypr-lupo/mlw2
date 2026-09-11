#!/usr/bin/env python3
"""
Exporta un trabajo de Markdown a .docx o .pdf.

El Markdown es el original; lo exportado es derivado y desechable. El script no
toca la nota: lee, transforma en memoria y escribe en trabajos/_export/.

Formato institucional
---------------------
Si existe una plantilla en trabajos/_recursos/ —plantilla.dotx o plantilla.docx—
el .docx sale con sus estilos, sus margenes, su tipografia y sus encabezados.

Pandoc solo admite .docx como documento de referencia. Un .dotx es el mismo
paquete OOXML con otro tipo de contenido declarado, asi que el script lo
convierte a .docx en cache y le pasa esa copia a Pandoc. La plantilla original
no se modifica.

El PDF se produce entonces desde el .docx ya maquetado, con LibreOffice, para
que conserve el formato. Sin plantilla, el PDF sale por la via LaTeX de Pandoc,
que ignora cualquier estilo de Word.

    Markdown --pandoc--> .docx (estilos de la plantilla) --soffice--> .pdf

Uso:
    python trabajos/_recursos/exportar.py "<nota>"
    python trabajos/_recursos/exportar.py "<nota>" --formato pdf
    python trabajos/_recursos/exportar.py --todos
    python trabajos/_recursos/exportar.py --todos --ramo S1.2
    python trabajos/_recursos/exportar.py "<nota>" --plantilla "otra.dotx"
    python trabajos/_recursos/exportar.py --sin-plantilla

Requiere Pandoc. Para PDF con plantilla, LibreOffice. Para PDF sin plantilla, un
motor LaTeX. Fuera de eso, solo biblioteca estandar.
"""

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

RAIZ = "trabajos"
SALIDA = "_export"
RECURSOS = "_recursos"
NOMBRES_PLANTILLA = ("plantilla.dotx", "plantilla.docx")
# El ramo vive en el nombre del archivo, no en la carpeta: trabajos/ es plana.
NOTA_DE_RAMO = re.compile(r"^(S\d|SEM)")

# Tipo de contenido de la parte principal: lo unico que distingue un .dotx de
# un .docx a ojos de Pandoc.
CT_PLANTILLA = ("application/vnd.openxmlformats-officedocument"
                ".wordprocessingml.template.main+xml")
CT_DOCUMENTO = ("application/vnd.openxmlformats-officedocument"
                ".wordprocessingml.document.main+xml")


# --------------------------------------------------------------- plantilla

def buscar_plantilla(raiz: Path):
    for nombre in NOMBRES_PLANTILLA:
        cand = raiz / RAIZ / RECURSOS / nombre
        if cand.is_file():
            return cand
    return None


def dotx_a_docx(dotx: Path, cache: Path) -> Path:
    """Reescribe [Content_Types].xml y devuelve un .docx equivalente.

    Se regenera solo si la plantilla cambio: se compara la fecha de
    modificacion, no el contenido, que basta para un archivo que edita una
    persona.
    """
    cache.parent.mkdir(parents=True, exist_ok=True)
    if cache.is_file() and cache.stat().st_mtime >= dotx.stat().st_mtime:
        return cache
    with zipfile.ZipFile(dotx) as z:
        nombres = z.namelist()
        if "[Content_Types].xml" not in nombres:
            raise ValueError(f"{dotx.name} no es un paquete OOXML valido")
        datos = {n: z.read(n) for n in nombres}
    ct = datos["[Content_Types].xml"].decode("utf-8")
    if CT_PLANTILLA not in ct and CT_DOCUMENTO not in ct:
        raise ValueError(f"{dotx.name} no declara una parte principal de Word")
    datos["[Content_Types].xml"] = ct.replace(CT_PLANTILLA, CT_DOCUMENTO).encode("utf-8")
    with zipfile.ZipFile(cache, "w", zipfile.ZIP_DEFLATED) as z:
        for n, b in datos.items():
            z.writestr(n, b)
    return cache


def referencia(raiz: Path, ruta_plantilla, sin_plantilla: bool):
    """Devuelve (ruta .docx de referencia | None, mensaje para el usuario)."""
    if sin_plantilla:
        return None, "sin plantilla, por peticion expresa"
    p = Path(ruta_plantilla) if ruta_plantilla else buscar_plantilla(raiz)
    if p is None:
        return None, ("sin plantilla: deja plantilla.dotx en "
                      f"{RAIZ}/{RECURSOS}/ y el formato se aplica solo")
    if not p.is_file():
        raise FileNotFoundError(f"No existe la plantilla: {p}")
    if p.suffix.lower() == ".dotx":
        cache = raiz / RAIZ / SALIDA / ".plantilla" / (p.stem + ".docx")
        return dotx_a_docx(p, cache), f"plantilla: {p.name} (convertida a .docx en cache)"
    return p, f"plantilla: {p.name}"


# ------------------------------------------------------------------ nota

def separar_frontmatter(texto: str):
    if not texto.startswith("---"):
        return {}, texto
    fin = texto.find("\n---", 3)
    if fin == -1:
        return {}, texto
    campos = {}
    for linea in texto[3:fin].splitlines():
        if not linea.strip() or linea.startswith(" ") or linea.lstrip().startswith("-"):
            continue
        if ":" not in linea:
            continue
        c, _, v = linea.partition(":")
        campos[c.strip()] = v.strip()
    return campos, texto[fin + 4:].lstrip("\n")


def limpiar(cuerpo: str) -> str:
    cuerpo = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", cuerpo)
    cuerpo = re.sub(r"\[\[([^\]]+)\]\]", r"\1", cuerpo)
    cuerpo = re.sub(r"^!\s*$", "", cuerpo, flags=re.M)
    return cuerpo


def portada(campos: dict) -> str:
    orden = [("ramo", "Asignatura"), ("tipo", "Tipo"),
             ("ponderacion", "Ponderacion"), ("entrega", "Entrega")]
    filas = []
    for clave, rotulo in orden:
        v = (campos.get(clave) or "").strip()
        if v:
            if clave == "ponderacion" and not v.endswith("%"):
                v += " %"
            filas.append(f"**{rotulo}:** {v}")
    return "  \n".join(filas) + "\n\n" if filas else ""


# --------------------------------------------------------------- conversion

def a_docx(nota: Path, destino: Path, ref) -> Path:
    texto = nota.read_text(encoding="utf-8")
    campos, cuerpo = separar_frontmatter(texto)
    titulo = campos.get("titulo") or nota.stem
    documento = f"% {titulo}\n\n" + portada(campos) + limpiar(cuerpo)

    destino.mkdir(parents=True, exist_ok=True)
    salida = destino / f"{nota.stem}.docx"
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     encoding="utf-8") as tmp:
        tmp.write(documento)
        ruta_tmp = Path(tmp.name)
    orden = ["pandoc", str(ruta_tmp), "-f", "markdown+footnotes",
             "-o", str(salida), "--standalone"]
    if ref:
        orden += [f"--reference-doc={ref}"]
    try:
        r = subprocess.run(orden, capture_output=True, text=True)
    finally:
        ruta_tmp.unlink(missing_ok=True)
    if r.returncode != 0:
        print(f"  FALLO  {nota.name}\n{r.stderr.strip()[:600]}", file=sys.stderr)
        return None
    return salida


def docx_a_pdf(docx: Path) -> Path:
    """Convierte con LibreOffice, que respeta los estilos de la plantilla."""
    perfil = Path(tempfile.mkdtemp(prefix="lo-"))
    orden = ["soffice", "--headless", f"-env:UserInstallation=file://{perfil}",
             "--convert-to", "pdf", "--outdir", str(docx.parent), str(docx)]
    try:
        r = subprocess.run(orden, capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        print("  FALLO  LibreOffice no respondio en 180 s", file=sys.stderr)
        return None
    finally:
        shutil.rmtree(perfil, ignore_errors=True)
    pdf = docx.with_suffix(".pdf")
    if r.returncode != 0 or not pdf.is_file():
        print(f"  FALLO  conversion a PDF\n{r.stderr.strip()[:400]}", file=sys.stderr)
        return None
    return pdf


def a_pdf_latex(nota: Path, destino: Path) -> Path:
    texto = nota.read_text(encoding="utf-8")
    campos, cuerpo = separar_frontmatter(texto)
    titulo = campos.get("titulo") or nota.stem
    documento = f"% {titulo}\n\n" + portada(campos) + limpiar(cuerpo)
    destino.mkdir(parents=True, exist_ok=True)
    salida = destino / f"{nota.stem}.pdf"
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     encoding="utf-8") as tmp:
        tmp.write(documento)
        ruta_tmp = Path(tmp.name)
    orden = ["pandoc", str(ruta_tmp), "-f", "markdown+footnotes", "-o", str(salida),
             "--standalone", "--pdf-engine=xelatex", "-V", "lang=es",
             "-V", "geometry:margin=2.5cm", "-V", "fontsize=12pt"]
    try:
        r = subprocess.run(orden, capture_output=True, text=True)
    finally:
        ruta_tmp.unlink(missing_ok=True)
    if r.returncode != 0:
        print(f"  FALLO  {nota.name}\n{r.stderr.strip()[:600]}", file=sys.stderr)
        return None
    return salida


def exportar(nota: Path, formato: str, destino: Path, ref):
    if formato == "docx":
        s = a_docx(nota, destino, ref)
    elif ref:
        d = a_docx(nota, destino, ref)
        s = docx_a_pdf(d) if d else None
    else:
        s = a_pdf_latex(nota, destino)
    if s:
        print(f"  {s}  ({s.stat().st_size // 1024} KB)")
    return s


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Exporta trabajos a .docx o .pdf.")
    ap.add_argument("nota", nargs="?", type=Path)
    ap.add_argument("--formato", choices=("docx", "pdf"), default="docx")
    ap.add_argument("--todos", action="store_true")
    ap.add_argument("--ramo")
    ap.add_argument("--plantilla", help="Ruta a un .dotx o .docx de referencia")
    ap.add_argument("--sin-plantilla", action="store_true",
                    help="Ignora la plantilla institucional")
    ap.add_argument("--raiz", type=Path, default=Path("."))
    args = ap.parse_args()

    if not shutil.which("pandoc"):
        print("Pandoc no esta en el PATH. Sin el no hay exportacion.", file=sys.stderr)
        return 2

    try:
        ref, aviso = referencia(args.raiz, args.plantilla, args.sin_plantilla)
    except (FileNotFoundError, ValueError) as e:
        print(str(e), file=sys.stderr)
        return 2
    print(aviso)

    if args.formato == "pdf":
        if ref and not shutil.which("soffice"):
            print("Con plantilla, el PDF exige LibreOffice. Exporta a docx y "
                  "conviertelo en Word.", file=sys.stderr)
            return 2
        if not ref and not any(shutil.which(m) for m in
                               ("xelatex", "pdflatex", "lualatex")):
            print("Sin plantilla, el PDF exige un motor LaTeX.", file=sys.stderr)
            return 2

    destino = args.raiz / RAIZ / SALIDA

    if args.todos:
        base = args.raiz / RAIZ
        notas = [p for p in sorted(base.rglob("*.md"))
                 if not p.parent.name.startswith("_")
                 and NOTA_DE_RAMO.match(p.name)
                 and (not args.ramo or p.name.startswith(args.ramo))]
        if not notas:
            print("No hay trabajos que exportar todavia.")
            return 0
        print(f"Exportando {len(notas)} trabajos a {destino}:")
        fallos = sum(1 for n in notas if exportar(n, args.formato, destino, ref) is None)
        return 1 if fallos else 0

    if not args.nota:
        ap.error("indica una nota o usa --todos")
    if not args.nota.is_file():
        print(f"No existe: {args.nota}", file=sys.stderr)
        return 2
    return 0 if exportar(args.nota, args.formato, destino, ref) else 1


if __name__ == "__main__":
    sys.exit(main())
