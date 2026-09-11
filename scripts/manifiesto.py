#!/usr/bin/env python3
"""
Manifiesto de fuentes: control de ingesta incremental.

Compara el estado actual de sources/ contra MANIFIESTO.json y reporta qué
fuentes son nuevas, cuáles cambiaron, cuáles desaparecieron y cuáles siguen
igual. Reingerir una fuente sin cambios gasta contexto y sobrescribe ajustes
manuales; este script evita ambas cosas.

Uso:
    python scripts/manifiesto.py sources/
    python scripts/manifiesto.py sources/ --manifiesto MANIFIESTO.json
    python scripts/manifiesto.py sources/ --registrar archivo.pdf --ficha wiki/fuentes/x.md
    python scripts/manifiesto.py sources/ --bitacora

Sólo biblioteca estándar.
"""

import argparse
import hashlib
import json
import signal
import sys
from datetime import date
from pathlib import Path

EXTENSIONES = {
    ".pdf", ".docx", ".doc", ".pptx", ".xlsx", ".xls", ".csv",
    ".md", ".txt", ".rtf", ".odt", ".epub", ".html", ".htm",
}

IGNORAR = {".gitkeep", ".DS_Store", "Thumbs.db", "LEEME.md", "README.md"}


def sha256(ruta: Path, bloque: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with ruta.open("rb") as f:
        for trozo in iter(lambda: f.read(bloque), b""):
            h.update(trozo)
    return h.hexdigest()


def cargar(ruta: Path) -> dict:
    if not ruta.exists():
        return {"version": 1, "fuentes": {}}
    try:
        datos = json.loads(ruta.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"MANIFIESTO ilegible ({e}). Abortando para no perder datos.",
              file=sys.stderr)
        sys.exit(2)
    datos.setdefault("version", 1)
    datos.setdefault("fuentes", {})
    return datos


def escanear(raiz: Path) -> dict:
    actual = {}
    for ruta in sorted(raiz.rglob("*")):
        if not ruta.is_file():
            continue
        if ruta.name in IGNORAR or ruta.name.startswith("."):
            continue
        if ruta.suffix.lower() not in EXTENSIONES:
            continue
        # las imágenes de sources/assets/ no son fuentes ingeribles
        if "assets" in ruta.relative_to(raiz).parts:
            continue
        clave = ruta.relative_to(raiz).as_posix()
        actual[clave] = {"sha256": sha256(ruta), "bytes": ruta.stat().st_size}
    return actual


def comparar(actual: dict, previo: dict):
    nuevas, modificadas, sin_cambios = [], [], []
    for clave, info in actual.items():
        anterior = previo.get(clave)
        if anterior is None:
            nuevas.append(clave)
        elif anterior.get("sha256") != info["sha256"]:
            modificadas.append(clave)
        else:
            sin_cambios.append(clave)
    eliminadas = [k for k in previo if k not in actual]
    return nuevas, modificadas, eliminadas, sin_cambios


def informe(nuevas, modificadas, eliminadas, sin_cambios, raiz: Path):
    def bloque(titulo, items, nota=""):
        if not items:
            return
        print(f"\n{titulo} ({len(items)}){nota}")
        for i in items:
            print(f"  {i}")

    bloque("NUEVAS — ingerir", nuevas)
    bloque("MODIFICADAS — reingerir", modificadas,
           "\n  El contenido cambió. La ficha existente quedó desactualizada.")
    bloque("ELIMINADAS — retirar en cascada", eliminadas,
           "\n  Ejecutar la operacion 5: no basta con borrar la ficha.")
    bloque("SIN CAMBIOS — omitir", sin_cambios)

    total = len(nuevas) + len(modificadas)
    print(f"\n{len(nuevas) + len(modificadas) + len(sin_cambios)} fuentes en "
          f"{raiz} | {total} requieren ingesta | {len(eliminadas)} requieren retiro")

    # distribución por carpeta: detecta corpus desbalanceados antes de ingerir
    carpetas = {}
    for clave in list(nuevas) + list(modificadas) + list(sin_cambios):
        carpeta = "/".join(clave.split("/")[:-1]) or "(raiz)"
        carpetas[carpeta] = carpetas.get(carpeta, 0) + 1
    if len(carpetas) > 1:
        universo = sum(carpetas.values())
        print("\nDistribucion por carpeta:")
        for carpeta, n in sorted(carpetas.items(), key=lambda x: -x[1]):
            pct = 100 * n / universo
            marca = "  <-- concentracion alta" if pct > 40 else ""
            print(f"  {n:4d}  {pct:5.1f}%  {carpeta}{marca}")
        if max(carpetas.values()) / universo > 0.40:
            print("\n  Una carpeta concentra mas del 40% del corpus. Ingerirla")
            print("  primero fija un encuadre que sesga toda clasificacion")
            print("  posterior. Considerar orden inverso al volumen.")


def bitacora(nuevas, modificadas, eliminadas):
    hoy = date.today().isoformat()
    print(f"\n---\n## [{hoy}] manifiesto | Revision de fuentes")
    print(f"- Nuevas: {len(nuevas)}")
    print(f"- Modificadas: {len(modificadas)}")
    print(f"- Eliminadas: {len(eliminadas)}")
    print("- Notas: ")


def main():
    ap = argparse.ArgumentParser(description="Control de ingesta incremental.")
    ap.add_argument("fuentes", type=Path, help="Directorio sources/")
    ap.add_argument("--manifiesto", type=Path, default=Path("MANIFIESTO.json"))
    ap.add_argument("--registrar", metavar="RUTA",
                    help="Marca una fuente como ingerida y actualiza el manifiesto")
    ap.add_argument("--ficha", metavar="RUTA",
                    help="Ruta de la ficha creada, para --registrar")
    ap.add_argument("--bitacora", action="store_true",
                    help="Emite una entrada lista para pegar en bitacora.md")
    args = ap.parse_args()

    if not args.fuentes.is_dir():
        print(f"No es un directorio: {args.fuentes}", file=sys.stderr)
        return 2

    previo = cargar(args.manifiesto)
    actual = escanear(args.fuentes)

    if args.registrar:
        clave = args.registrar
        if clave not in actual:
            print(f"No encontrada en {args.fuentes}: {clave}", file=sys.stderr)
            return 2
        entrada = dict(actual[clave])
        entrada["ingerido"] = date.today().isoformat()
        if args.ficha:
            entrada["ficha"] = args.ficha
        previo["fuentes"][clave] = entrada
        args.manifiesto.write_text(
            json.dumps(previo, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Registrada: {clave}")
        return 0

    n, m, e, s = comparar(actual, previo["fuentes"])
    informe(n, m, e, s, args.fuentes)
    if args.bitacora:
        bitacora(n, m, e)
    return 0


if __name__ == "__main__":
    # permite canalizar la salida a head/less sin traza de error
    if hasattr(signal, "SIGPIPE"):
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    sys.exit(main())
