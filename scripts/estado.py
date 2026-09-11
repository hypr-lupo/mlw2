#!/usr/bin/env python3
"""
Estado del despliegue: reconciliacion del corpus contra la wiki.

Cruza raw/sources/ con MANIFIESTO.json, wiki/sources/, wiki/index.md,
wiki/referencias.md y despliegue/fase1/, clasifica cada documento en uno de
cuatro estados y escribe ESTADO.md.

raw/sources/ es plano desde el 05-09-2026: la agrupacion por cumulos ya no sale
de las carpetas sino de las tablas de INVENTARIO.md, que es su unica taxonomia.
Las reglas del esquema estan en schema.md.

    pendiente --> fase1 --> fase2 --> completo

Vista derivada y regenerable. Nunca es fuente de verdad: ante discrepancia
manda MANIFIESTO.json.

Uso:
    python scripts/estado.py
    python scripts/estado.py --sin-escribir
    python scripts/estado.py --verificar-hash
    python scripts/estado.py --incluir-institucional

Devuelve 0 si la reconciliacion es consistente, 1 si detecta anomalias.
Solo biblioteca estandar.
"""

import argparse
import hashlib
import json
import re
import signal
import sys
from datetime import date
from pathlib import Path

# Mismos criterios que scripts/manifiesto.py: el universo debe coincidir.
EXTENSIONES = {
    ".pdf", ".docx", ".doc", ".pptx", ".xlsx", ".xls", ".csv",
    ".md", ".txt", ".rtf", ".odt", ".epub", ".html", ".htm",
}
IGNORAR = {".gitkeep", ".DS_Store", "Thumbs.db", "LEEME.md", "README.md"}

# El cumulo institucional no entra en el universo del despliegue: son programas
# de curso y horarios, que se ingieren por excepcion. El nombre debe coincidir
# exactamente con el encabezado de su tabla en INVENTARIO.md.
INSTITUCIONAL = "Programas oficiales y malla"
SIN_CUMULO = "(fuera de INVENTARIO.md)"

ESTADOS = ("pendiente", "fase1", "fase2", "completo")


# --------------------------------------------------------------------------
# Lectura
# --------------------------------------------------------------------------

def sha256(ruta: Path, bloque: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with ruta.open("rb") as f:
        for trozo in iter(lambda: f.read(bloque), b""):
            h.update(trozo)
    return h.hexdigest()


def texto(ruta: Path) -> str:
    try:
        return ruta.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def partir_lista(bruto: str) -> list:
    """Divide una lista YAML en linea respetando las comas entre comillas."""
    bruto = bruto.strip()
    if bruto.startswith("[") and bruto.endswith("]"):
        bruto = bruto[1:-1]
    partes, actual, comilla = [], [], None
    for c in bruto:
        if comilla:
            if c == comilla:
                comilla = None
            else:
                actual.append(c)
        elif c in "\"'":
            comilla = c
        elif c == ",":
            partes.append("".join(actual).strip())
            actual = []
        else:
            actual.append(c)
    partes.append("".join(actual).strip())
    return [p for p in partes if p]


def frontmatter(contenido: str) -> dict:
    """Subconjunto de YAML suficiente para el esquema: clave: valor y listas."""
    if not contenido.startswith("---"):
        return {}
    fin = contenido.find("\n---", 3)
    if fin == -1:
        return {}
    campos = {}
    for linea in contenido[3:fin].splitlines():
        if not linea.strip() or linea.lstrip().startswith("#"):
            continue
        if ":" not in linea or linea.startswith(" "):
            continue
        clave, _, valor = linea.partition(":")
        campos[clave.strip()] = valor.strip()
    return campos


def leer_cumulos(ruta_inventario: Path) -> dict:
    """INVENTARIO.md -> {nombre de archivo: cumulo}. Sustituye a la carpeta de
    origen, que desaparecio al aplanarse el corpus."""
    cumulos = {}
    if not ruta_inventario.is_file():
        return cumulos
    actual = None
    for linea in texto(ruta_inventario).splitlines():
        m = re.match(r"^## (.+?) · \d+ doc\.$", linea)
        if m:
            actual = m.group(1)
            continue
        m = re.match(r"^\| (.+?) \| [\d.]+ \| `", linea)
        if m and actual:
            cumulos[m.group(1)] = actual
    return cumulos


def escanear_corpus(raiz_fuentes: Path, incluir_institucional: bool,
                    cumulos: dict) -> dict:
    """Universo del despliegue: ruta relativa -> bytes."""
    corpus = {}
    if not raiz_fuentes.is_dir():
        return corpus
    for ruta in sorted(raiz_fuentes.rglob("*")):
        if not ruta.is_file():
            continue
        if ruta.name in IGNORAR or ruta.name.startswith("."):
            continue
        if ruta.suffix.lower() not in EXTENSIONES:
            continue
        rel = ruta.relative_to(raiz_fuentes)
        if "assets" in rel.parts:
            continue
        if (not incluir_institucional
                and cumulos.get(rel.name) == INSTITUCIONAL):
            continue
        corpus[rel.as_posix()] = ruta
    return corpus


def leer_fase1(dir_fase1: Path) -> dict:
    """Analisis de fase 1 -> ruta de la fuente que declara. Se lee la linea
    '**Fuente:** `<ruta>`' del encabezado."""
    declarados, huerfanos = {}, []
    if not dir_fase1.is_dir():
        return {"por_fuente": declarados, "sin_fuente": huerfanos}
    patron = re.compile(r"^\*\*Fuente:\*\*\s*`([^`]+)`", re.M)
    for ruta in sorted(dir_fase1.glob("*.md")):
        if ruta.name in IGNORAR:
            continue
        m = patron.search(texto(ruta))
        if m:
            declarados.setdefault(m.group(1).strip(), []).append(ruta)
        else:
            huerfanos.append(ruta)
    return {"por_fuente": declarados, "sin_fuente": huerfanos}


def leer_fichas(dir_fichas: Path) -> dict:
    """Ficha -> lista de nombres de archivo que declara en sources[]."""
    fichas = {}
    if not dir_fichas.is_dir():
        return fichas
    for ruta in sorted(dir_fichas.glob("*.md")):
        if ruta.name in IGNORAR:
            continue
        campos = frontmatter(texto(ruta))
        fichas[ruta.stem] = {
            "ruta": ruta,
            "sources": partir_lista(campos.get("sources", "")),
            "verificacion": campos.get("verificacion_bibliografica", ""),
            "truncado": campos.get("truncado", ""),
        }
    return fichas


# --------------------------------------------------------------------------
# Reconciliacion
# --------------------------------------------------------------------------

def clasificar(corpus, manifiesto, fichas, fase1, indice, referencias, hashes,
               cumulos):
    """Un registro por documento del universo, con su estado y sus faltantes."""
    # nombre de archivo -> slug de ficha, por si el manifiesto aun no lo liga
    por_nombre = {}
    for slug, datos in fichas.items():
        for nombre in datos["sources"]:
            por_nombre.setdefault(Path(nombre).name, slug)

    registros = []
    for rel, ruta in corpus.items():
        entrada = manifiesto.get(rel, {})
        slug = None
        if entrada.get("ficha"):
            slug = Path(entrada["ficha"]).stem
        if slug not in fichas:
            slug = por_nombre.get(Path(rel).name)

        faltan = []
        if slug and slug in fichas:
            if not entrada.get("sha256"):
                faltan.append("manifiesto")
            elif hashes is not None and hashes.get(rel) != entrada["sha256"]:
                faltan.append("hash divergente")
            if f"[[{slug}]]" not in indice:
                faltan.append("indice")
            if f"[[{slug}]]" not in referencias:
                faltan.append("referencias")
            estado = "completo" if not faltan else "fase2"
        elif rel in fase1["por_fuente"]:
            estado = "fase1"
            faltan = ["ficha", "manifiesto", "indice", "referencias"]
        else:
            estado = "pendiente"

        registros.append({
            "fuente": rel,
            "cumulo": cumulos.get(Path(rel).name, SIN_CUMULO),
            "nombre": Path(rel).name,
            "estado": estado,
            "slug": slug,
            "faltan": faltan,
            "bytes": ruta.stat().st_size,
        })
    return registros


def anomalias(corpus, manifiesto, fichas, fase1, registros, cumulos):
    lista = []
    for rel in manifiesto:
        if rel not in corpus and cumulos.get(Path(rel).name) != INSTITUCIONAL:
            lista.append(f"manifiesto: `{rel}` ingerido pero ausente de raw/sources/ "
                         f"— exige retiro en cascada, no basta con borrar la ficha")
    ligados = {r["slug"] for r in registros if r["slug"]}
    institucionales = {Path(e["ficha"]).stem for e in manifiesto.values() if e.get("ficha")}
    for slug, datos in fichas.items():
        if slug not in ligados and slug not in institucionales:
            lista.append(f"ficha huerfana: `wiki/sources/{slug}.md` no corresponde a "
                         f"ningun documento del universo")
        if not datos["sources"]:
            lista.append(f"ficha sin procedencia: `wiki/sources/{slug}.md` "
                         f"no declara sources[]")
    for ruta in fase1["sin_fuente"]:
        lista.append(f"fase 1 sin fuente declarada: `{ruta.as_posix()}` "
                     f"carece de la linea '**Fuente:** `...`'")
    for r in registros:
        if r["cumulo"] == SIN_CUMULO:
            lista.append(f"inventario desactualizado: `{r['nombre']}` esta en "
                         f"raw/sources/ pero no en INVENTARIO.md")
    for rel, rutas in fase1["por_fuente"].items():
        if rel not in corpus and cumulos.get(Path(rel).name) != INSTITUCIONAL:
            lista.append(f"fase 1 huerfana: `{rutas[0].name}` declara `{rel}`, "
                         f"que no esta en el corpus")
        if len(rutas) > 1:
            lista.append(f"fase 1 duplicada: {len(rutas)} analisis declaran `{rel}`")
    return lista


# --------------------------------------------------------------------------
# Salida
# --------------------------------------------------------------------------

def resumen(registros):
    cuenta = {e: 0 for e in ESTADOS}
    for r in registros:
        cuenta[r["estado"]] += 1
    return cuenta


def por_cumulo(registros):
    tabla = {}
    for r in registros:
        fila = tabla.setdefault(r["cumulo"], {e: 0 for e in ESTADOS})
        fila[r["estado"]] += 1
    return dict(sorted(tabla.items()))


def informe_consola(registros, problemas, pendientes_verificacion):
    cuenta = resumen(registros)
    total = len(registros)
    print(f"\nUniverso del despliegue: {total} documentos\n")
    for estado in ESTADOS:
        n = cuenta[estado]
        pct = 100 * n / total if total else 0
        print(f"  {estado:10s} {n:4d}  {pct:5.1f}%")

    print("\nPor cumulo:")
    print(f"  {'cumulo':44s} {'tot':>4s} {'pend':>5s} {'f1':>4s} {'f2':>4s} {'comp':>5s}")
    for cumulo, fila in por_cumulo(registros).items():
        t = sum(fila.values())
        print(f"  {cumulo[:44]:44s} {t:4d} {fila['pendiente']:5d} "
              f"{fila['fase1']:4d} {fila['fase2']:4d} {fila['completo']:5d}")

    a_medias = [r for r in registros if r["estado"] in ("fase1", "fase2")]
    if a_medias:
        print(f"\nTrabajo a medio camino ({len(a_medias)}) — retomar por aqui:")
        for r in a_medias:
            falta = ", ".join(r["faltan"]) or "-"
            print(f"  [{r['estado']}] {r['nombre']}\n      falta: {falta}")

    if pendientes_verificacion:
        print(f"\nFichas con verificacion_bibliografica pendiente "
              f"({len(pendientes_verificacion)}): no citar todavia")
        for slug in pendientes_verificacion:
            print(f"  {slug}")

    if problemas:
        print(f"\nANOMALIAS ({len(problemas)}):")
        for p in problemas:
            print(f"  - {p}")
    else:
        print("\nSin anomalias.")


def escribir_estado(destino: Path, registros, problemas, pendientes_verificacion,
                    universo_institucional):
    cuenta = resumen(registros)
    total = len(registros)
    hoy = date.today().isoformat()
    L = []
    L.append("# Estado del despliegue")
    L.append("")
    L.append(f"**Generado:** {hoy} por `python scripts/estado.py`. "
             f"**No editar a mano:** se sobrescribe en cada corrida.")
    L.append("")
    L.append("Vista derivada de `MANIFIESTO.json`, `wiki/sources/`, `wiki/index.md`, "
             "`wiki/referencias.md` y `despliegue/fase1/`. Ante discrepancia manda el "
             "manifiesto, no este archivo.")
    L.append("")
    L.append(f"**Universo:** {total} documentos de `raw/sources/`, excluido "
             f"el cumulo `{INSTITUCIONAL}` ({universo_institucional} documentos, "
             f"que se ingieren por excepcion). Los cumulos son los de "
             f"`INVENTARIO.md`.")
    L.append("")
    L.append("## Resumen")
    L.append("")
    L.append("| Estado | Documentos | % |")
    L.append("|---|---:|---:|")
    for estado in ESTADOS:
        pct = 100 * cuenta[estado] / total if total else 0
        L.append(f"| `{estado}` | {cuenta[estado]} | {pct:.1f} % |")
    L.append("")
    L.append("## Por cumulo")
    L.append("")
    L.append("| Cumulo | Total | pendiente | fase1 | fase2 | completo |")
    L.append("|---|---:|---:|---:|---:|---:|")
    for cumulo, fila in por_cumulo(registros).items():
        t = sum(fila.values())
        L.append(f"| {cumulo} | {t} | {fila['pendiente']} | {fila['fase1']} | "
                 f"{fila['fase2']} | {fila['completo']} |")
    L.append("")

    a_medias = [r for r in registros if r["estado"] in ("fase1", "fase2")]
    L.append("## Trabajo a medio camino")
    L.append("")
    if a_medias:
        L.append("Punto de reanudacion. Un documento aqui tiene trabajo hecho que no "
                 "debe repetirse.")
        L.append("")
        for r in a_medias:
            falta = ", ".join(r["faltan"]) or "-"
            L.append(f"- `{r['estado']}` — {r['nombre']} · falta: {falta}")
    else:
        L.append("*Ninguno. Ninguna ingesta quedo interrumpida.*")
    L.append("")

    L.append("## Anomalias")
    L.append("")
    if problemas:
        for p in problemas:
            L.append(f"- {p}")
    else:
        L.append("*Ninguna.*")
    L.append("")

    L.append("## Verificacion bibliografica pendiente")
    L.append("")
    if pendientes_verificacion:
        L.append("Estas fichas no se citan hasta cotejarlas contra el documento.")
        L.append("")
        for slug in pendientes_verificacion:
            L.append(f"- [[{slug}]]")
    else:
        L.append("*Ninguna.*")
    L.append("")

    L.append("## Detalle por documento")
    L.append("")
    cumulo_actual = None
    for r in sorted(registros, key=lambda x: (x["cumulo"], x["nombre"])):
        if r["cumulo"] != cumulo_actual:
            cumulo_actual = r["cumulo"]
            L.append("")
            L.append(f"### {cumulo_actual}")
            L.append("")
        L.append(f"- `{r['estado']}` — {r['nombre']}")
    L.append("")
    destino.write_text("\n".join(L), encoding="utf-8")


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Reconcilia el corpus contra la wiki y escribe ESTADO.md.")
    ap.add_argument("--raiz", type=Path, default=Path("."),
                    help="Raiz del proyecto (por defecto, el directorio actual)")
    ap.add_argument("--salida", type=Path, default=None,
                    help="Archivo a escribir (por defecto, <raiz>/ESTADO.md)")
    ap.add_argument("--sin-escribir", action="store_true",
                    help="Solo informe en pantalla, no toca ESTADO.md")
    ap.add_argument("--verificar-hash", action="store_true",
                    help="Recalcula el sha256 de cada fuente ingerida y detecta deriva")
    ap.add_argument("--incluir-institucional", action="store_true",
                    help=f"Incluye «{INSTITUCIONAL}» en el universo")
    args = ap.parse_args()

    raiz = args.raiz
    fuentes = raiz / "raw" / "sources"
    if not fuentes.is_dir():
        print(f"No existe {fuentes}. ¿Es la raiz del proyecto?", file=sys.stderr)
        return 2

    cumulos = leer_cumulos(raiz / "INVENTARIO.md")
    corpus = escanear_corpus(fuentes, args.incluir_institucional, cumulos)
    n_institucional = (len(escanear_corpus(fuentes, True, cumulos))
                       - len(escanear_corpus(fuentes, False, cumulos)))

    ruta_manifiesto = raiz / "MANIFIESTO.json"
    manifiesto = {}
    if ruta_manifiesto.exists():
        try:
            manifiesto = json.loads(ruta_manifiesto.read_text(encoding="utf-8")).get("fuentes", {})
        except json.JSONDecodeError as e:
            print(f"MANIFIESTO.json ilegible ({e}).", file=sys.stderr)
            return 2

    fichas = leer_fichas(raiz / "wiki" / "sources")
    fase1 = leer_fase1(raiz / "despliegue" / "fase1")
    indice = texto(raiz / "wiki" / "index.md")
    referencias = texto(raiz / "wiki" / "referencias.md")

    hashes = None
    if args.verificar_hash:
        hashes = {rel: sha256(ruta) for rel, ruta in corpus.items() if rel in manifiesto}

    registros = clasificar(corpus, manifiesto, fichas, fase1, indice, referencias,
                           hashes, cumulos)
    problemas = anomalias(corpus, manifiesto, fichas, fase1, registros, cumulos)
    pendientes = sorted(s for s, d in fichas.items() if d["verificacion"] == "pendiente")

    informe_consola(registros, problemas, pendientes)

    if not args.sin_escribir:
        destino = args.salida or (raiz / "ESTADO.md")
        escribir_estado(destino, registros, problemas, pendientes, n_institucional)
        print(f"\nEscrito: {destino}")

    return 1 if problemas else 0


if __name__ == "__main__":
    if hasattr(signal, "SIGPIPE"):
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    sys.exit(main())
