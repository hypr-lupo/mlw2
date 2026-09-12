#!/usr/bin/env python3
"""
Diagnostico del grafo de la wiki.

Construye el grafo desde los wikilinks y el campo sources[] del frontmatter,
aplica el modelo de relevancia de cuatro senales y reporta los hallazgos
definidos en references/grafo.md: paginas aisladas, clusteres dispersos, nodos
puente, nodos centrales, conexiones inesperadas, referencias cruzadas
faltantes y enlaces rotos.

Uso:
    python scripts/grafo.py wiki/
    python scripts/grafo.py wiki/ --comunidades
    python scripts/grafo.py wiki/ --json

Sólo biblioteca estándar.
"""

import argparse
import json
import math
import random
import re
import signal
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

PESO_FUENTE = 4.0
PESO_ENLACE = 3.0
PESO_VECINO = 1.5
PESO_TIPO = 1.0

COHESION_MINIMA = 0.15
GRADO_AISLADA = 1
PUENTE_MINIMO = 3

# El lookbehind excluye los embeds de Obsidian (![[figura.png]]): un adjunto
# de raw/assets/ no es una pagina y no debe contarse como enlace roto.
RE_WIKILINK = re.compile(r"(?<!!)\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
RE_LISTA = re.compile(r"\[(.*?)\]", re.S)

# "purpose" y "schema" viven en la raiz del vault, no en wiki/, pero son
# documentos de servicio igual que los demas: enlazarlos no es un enlace roto.
SERVICIO = {"indice", "index", "bitacora", "log", "panorama", "overview",
            "pendientes", "revision", "referencias", "purpose", "schema"}


# --------------------------------------------------------------------------- #
# Lectura

def frontmatter(texto: str):
    if not texto.startswith("---"):
        return {}, texto
    partes = texto.split("---", 2)
    if len(partes) < 3:
        return {}, texto
    campos = {}
    for linea in partes[1].splitlines():
        if ":" not in linea or linea.lstrip().startswith("#"):
            continue
        clave, _, valor = linea.partition(":")
        campos[clave.strip()] = valor.strip()
    return campos, partes[2]


def lista(valor: str):
    if not valor:
        return []
    m = RE_LISTA.search(valor)
    interior = m.group(1) if m else valor
    # Los nombres de archivo del corpus contienen comas ("1996 - Gambetta - La
    # mafia siciliana, el negocio de la proteccion privada.pdf"). Partir por coma
    # sin respetar las comillas parte un archivo en dos fuentes falsas e infla la
    # senal de solapamiento. Se parte solo por las comas fuera de comillas.
    piezas, actual, comilla = [], [], None
    for ch in interior:
        if comilla:
            if ch == comilla:
                comilla = None
            else:
                actual.append(ch)
        elif ch in "\"'":
            comilla = ch
        elif ch == ",":
            piezas.append("".join(actual)); actual = []
        else:
            actual.append(ch)
    piezas.append("".join(actual))
    return [x.strip() for x in piezas if x.strip()]


def cargar(raiz: Path):
    paginas = {}
    for ruta in sorted(raiz.rglob("*.md")):
        slug = ruta.stem
        if slug.lower() in SERVICIO:
            continue
        fm, cuerpo = frontmatter(ruta.read_text(encoding="utf-8", errors="replace"))
        paginas[slug] = {
            "ruta": ruta,
            "title": fm.get("title") or fm.get("titulo") or slug,
            "type": fm.get("type") or fm.get("tipo") or "sin-tipo",
            "cluster": fm.get("cluster") or "sin-cluster",
            "procedencia": fm.get("procedencia", ""),
            "sources": set(lista(fm.get("sources") or fm.get("fuentes", ""))),
            "enlaces": {m.group(1).strip() for m in RE_WIKILINK.finditer(cuerpo)},
        }
    return paginas


# --------------------------------------------------------------------------- #
# Grafo

def construir(paginas):
    """Devuelve adyacencia no dirigida, pesos por par y enlaces rotos."""
    ady = defaultdict(set)
    rotos = []

    for slug, p in paginas.items():
        for destino in p["enlaces"]:
            if destino == slug:
                continue
            if destino in paginas:
                ady[slug].add(destino)
                ady[destino].add(slug)
            elif destino.lower() not in SERVICIO:
                rotos.append((slug, destino))

    # aristas por solapamiento de fuentes
    por_fuente = defaultdict(set)
    for slug, p in paginas.items():
        for f in p["sources"]:
            por_fuente[f].add(slug)

    for slug in paginas:
        ady.setdefault(slug, set())

    grado = {s: len(ady[s]) for s in paginas}

    pesos = {}
    for a, b in combinations(sorted(paginas), 2):
        pa, pb = paginas[a], paginas[b]
        w = 0.0
        detalle = []

        comunes = pa["sources"] & pb["sources"]
        if comunes:
            w += PESO_FUENTE * len(comunes)
            detalle.append(f"fuentes:{len(comunes)}")

        if b in ady[a]:
            w += PESO_ENLACE
            detalle.append("enlace")

        vecinos = ady[a] & ady[b]
        if vecinos:
            aporte = sum(1 / math.log(grado[v]) for v in vecinos
                         if grado.get(v, 0) > 1)
            if aporte:
                w += PESO_VECINO * aporte
                detalle.append(f"vecinos:{len(vecinos)}")

        if pa["type"] == pb["type"] and pa["type"] != "sin-tipo":
            w += PESO_TIPO
            detalle.append("tipo")

        if w > 0:
            pesos[(a, b)] = (round(w, 2), detalle)

    return ady, grado, pesos, rotos, por_fuente


def cohesion(paginas, ady):
    filas = []
    grupos = defaultdict(list)
    for slug, p in paginas.items():
        grupos[p["cluster"]].append(slug)

    for nombre, miembros in sorted(grupos.items()):
        n = len(miembros)
        posibles = n * (n - 1) / 2
        conjunto = set(miembros)
        internas = sum(1 for a, b in combinations(miembros, 2) if b in ady[a])
        valor = internas / posibles if posibles else 0.0
        filas.append({
            "cluster": nombre, "paginas": n, "internas": internas,
            "posibles": int(posibles), "cohesion": round(valor, 3),
            "disperso": n >= 3 and valor < COHESION_MINIMA,
        })
    return filas


def comunidades(paginas, ady, semilla=0):
    """Propagacion de etiquetas. No determinista: comparar dos corridas."""
    rnd = random.Random(semilla)
    etiqueta = {s: i for i, s in enumerate(paginas)}
    nodos = list(paginas)
    for _ in range(30):
        rnd.shuffle(nodos)
        cambios = 0
        for s in nodos:
            if not ady[s]:
                continue
            cuenta = defaultdict(int)
            for v in ady[s]:
                cuenta[etiqueta[v]] += 1
            mejor = max(cuenta.values())
            candidatas = sorted(k for k, v in cuenta.items() if v == mejor)
            elegida = rnd.choice(candidatas)
            if elegida != etiqueta[s]:
                etiqueta[s] = elegida
                cambios += 1
        if not cambios:
            break
    grupos = defaultdict(list)
    for s, e in etiqueta.items():
        grupos[e].append(s)
    return [sorted(v) for v in grupos.values() if len(v) > 1]


# --------------------------------------------------------------------------- #
# Diagnostico

def diagnosticar(paginas, ady, grado, pesos, rotos, por_fuente):
    d = {}

    d["aisladas"] = sorted(s for s in paginas if grado[s] <= GRADO_AISLADA)

    d["clusteres"] = cohesion(paginas, ady)

    puentes = []
    for s in paginas:
        cl = {paginas[v]["cluster"] for v in ady[s]} - {"sin-cluster"}
        if len(cl) >= PUENTE_MINIMO:
            puentes.append((s, sorted(cl)))
    d["puentes"] = sorted(puentes, key=lambda x: -len(x[1]))

    if grado:
        orden = sorted(grado.items(), key=lambda x: -x[1])
        corte = max(1, len(orden) // 10)
        d["centrales"] = [(s, g) for s, g in orden[:corte] if g > 1]
    else:
        d["centrales"] = []

    inesperadas = []
    for (a, b), (w, det) in pesos.items():
        ca, cb = paginas[a]["cluster"], paginas[b]["cluster"]
        if ca != cb and "sin-cluster" not in (ca, cb) and w >= PESO_FUENTE:
            inesperadas.append((a, b, w, ca, cb, det))
    d["inesperadas"] = sorted(inesperadas, key=lambda x: -x[2])[:15]

    faltantes = []
    for (a, b), (w, det) in pesos.items():
        comunes = paginas[a]["sources"] & paginas[b]["sources"]
        if len(comunes) >= 2 and b not in ady[a]:
            faltantes.append((a, b, len(comunes)))
    d["faltantes"] = sorted(faltantes, key=lambda x: -x[2])[:20]

    d["rotos"] = rotos

    total = len(paginas)
    d["fuentes_dominantes"] = sorted(
        ((f, len(ps)) for f, ps in por_fuente.items()
         if total and len(ps) / total > 1 / 3),
        key=lambda x: -x[1],
    )

    d["sin_fuentes"] = sorted(
        s for s, p in paginas.items()
        if not p["sources"] and p["procedencia"] != "autor"
    )

    return d


def imprimir(paginas, grado, d, com=None):
    def enc(t):
        print(f"\n{t}\n{'-' * len(t)}")

    print(f"{len(paginas)} paginas | grado medio "
          f"{sum(grado.values()) / len(grado):.1f}" if paginas else "wiki vacia")

    if d["aisladas"]:
        enc(f"PAGINAS AISLADAS ({len(d['aisladas'])}) — grado <= {GRADO_AISLADA}")
        for s in d["aisladas"]:
            print(f"  {s}")

    enc("CLUSTERES")
    for c in d["clusteres"]:
        marca = "  <-- DISPERSO" if c["disperso"] else ""
        print(f"  {c['cohesion']:.3f}  {c['paginas']:3d} pag  "
              f"{c['internas']}/{c['posibles']} aristas  {c['cluster']}{marca}")

    if d["puentes"]:
        enc(f"NODOS PUENTE ({len(d['puentes'])}) — enlazan {PUENTE_MINIMO}+ clusteres")
        for s, cl in d["puentes"]:
            print(f"  {s}  ->  {', '.join(cl)}")

    if d["centrales"]:
        enc("NODOS CENTRALES — decil superior de grado")
        for s, g in d["centrales"]:
            print(f"  {g:3d}  {s}")

    if d["inesperadas"]:
        enc("CONEXIONES INESPERADAS — aristas fuertes entre clusteres")
        for a, b, w, ca, cb, det in d["inesperadas"]:
            print(f"  {w:6.2f}  {a} [{ca}] <-> {b} [{cb}]  ({', '.join(det)})")

    if d["faltantes"]:
        enc("REFERENCIAS CRUZADAS FALTANTES — 2+ fuentes comunes, sin enlace")
        for a, b, n in d["faltantes"]:
            print(f"  {n} fuentes  {a} <-> {b}")

    if d["rotos"]:
        enc(f"ENLACES ROTOS ({len(d['rotos'])})")
        for origen, destino in d["rotos"]:
            print(f"  {origen}  ->  [[{destino}]]")

    if d["sin_fuentes"]:
        enc(f"PAGINAS SIN FUENTES ({len(d['sin_fuentes'])})")
        for s in d["sin_fuentes"]:
            print(f"  {s}")

    if d["fuentes_dominantes"]:
        enc("FUENTES DOMINANTES — presentes en mas de un tercio de las paginas")
        for f, n in d["fuentes_dominantes"]:
            print(f"  {n:3d} paginas  {f}")
        print("\n  Aplanan la senal de solapamiento. Considerar excluirlas del")
        print("  calculo o ingerirlas por capitulos.")

    if com is not None:
        enc(f"COMUNIDADES DETECTADAS ({len(com)}) — propagacion de etiquetas")
        for i, grupo in enumerate(com, 1):
            decl = {paginas[s]["cluster"] for s in grupo}
            coincide = "coincide" if len(decl) == 1 else f"cruza {len(decl)} declarados"
            print(f"  [{i}] {len(grupo)} pag — {coincide}: {', '.join(sorted(decl))}")
        print("\n  No determinista. Correr dos veces con --semilla distinta;")
        print("  si las particiones difieren mucho, no hay estructura comunitaria.")


def main():
    ap = argparse.ArgumentParser(description="Diagnostico del grafo de la wiki.")
    ap.add_argument("wiki", type=Path, help="Directorio wiki/")
    ap.add_argument("--comunidades", action="store_true",
                    help="Detecta comunidades por topologia y las contrasta")
    ap.add_argument("--semilla", type=int, default=0)
    ap.add_argument("--json", action="store_true", help="Salida en JSON")
    args = ap.parse_args()

    if not args.wiki.is_dir():
        print(f"No es un directorio: {args.wiki}", file=sys.stderr)
        return 2

    paginas = cargar(args.wiki)
    if not paginas:
        print("No se encontraron paginas de contenido.")
        return 0

    ady, grado, pesos, rotos, por_fuente = construir(paginas)
    d = diagnosticar(paginas, ady, grado, pesos, rotos, por_fuente)
    com = comunidades(paginas, ady, args.semilla) if args.comunidades else None

    if args.json:
        d["comunidades"] = com
        print(json.dumps(d, ensure_ascii=False, indent=2, default=list))
    else:
        imprimir(paginas, grado, d, com)

    problemas = len(d["aisladas"]) + len(d["rotos"]) + \
        sum(1 for c in d["clusteres"] if c["disperso"])
    return 1 if problemas else 0


if __name__ == "__main__":
    # permite canalizar la salida a head/less sin traza de error
    if hasattr(signal, "SIGPIPE"):
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    sys.exit(main())
