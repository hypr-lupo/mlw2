#!/usr/bin/env python3
"""
Valida las invariantes estructurales del frontmatter de la wiki.

Comprueba lo que el marco de diseño declara obligatorio y lo que el motor de
grafo de LLM Wiki necesita para funcionar. No corrige nada: informa.

Uso:
    python scripts/validar_frontmatter.py wiki/
    python scripts/validar_frontmatter.py wiki/ --estricto

Sin dependencias externas: parsea el bloque YAML a mano para evitar exigir
PyYAML en un entorno de estudio.
"""

import argparse
import re
import sys
from pathlib import Path

# Ocho tipos de contenido, uno por carpeta de wiki/. Vocabulario en ingles, como
# los nombres de carpeta que la aplicacion LLM Wiki tiene comprometidos.
# «politica» y «caso» se evaluaran como tipos propios por la operacion 8 cuando
# se elija el caso de anclaje del trabajo de grado; hoy son entity + subtipo.
TIPOS_CONTENIDO = {
    "source", "entity", "concept", "method",
    "query", "synthesis", "comparison", "thesis",
}
TIPOS_SERVICIO = {"index", "log", "overview", "reference", "pendientes", "revision"}
TIPOS = TIPOS_CONTENIDO | TIPOS_SERVICIO

SUBTIPOS_ENTITY = {"persona", "organismo", "politica", "programa", "territorio"}
# La politica publica chilena y las cifras oficiales caducan; la teoria, no.
SUBTIPOS_CON_VIGENCIA = {"politica", "programa"}
VIGENCIAS = {"vigente", "superado", "incierto"}

OBLIGATORIOS_ESTRUCTURALES = ["title", "type", "sources"]
OBLIGATORIOS_DOMINIO = ["procedencia", "estado", "creado", "actualizado"]

PROCEDENCIAS = {"fuentes", "autor", "mixta"}
ESTADOS = {"borrador", "revisado", "estable"}

# Clusteres declarados en schema.md, seccion 3 bis. Toda pagina de contenido
# declara uno; sin cluster no hay medida de cohesion posible.
CLUSTERS = {
    "marco-institucional",
    "explicacion-del-delito",
    "prevencion",
    "medicion-y-metodo",
    "sistema-penal",
    "victimizacion-e-inseguridad",
    "gobernanza-criminal",
    "caso-de-grado",
}

PREFIJOS = {
    "thesis": "tesis-",
}

RE_NOTA = re.compile(r"\[\^(ext|inf|amb)-\d+\]")
RE_CONFIANZA = re.compile(r"confianza\s+(0(?:\.\d+)?|1(?:\.0+)?)")


def leer_frontmatter(texto: str):
    """Devuelve (dict, cuerpo). Parseo plano, suficiente para este esquema."""
    if not texto.startswith("---"):
        return None, texto
    partes = texto.split("---", 2)
    if len(partes) < 3:
        return None, texto
    campos = {}
    for linea in partes[1].splitlines():
        if not linea.strip() or linea.lstrip().startswith("#"):
            continue
        if ":" not in linea:
            continue
        clave, _, valor = linea.partition(":")
        campos[clave.strip()] = valor.strip()
    return campos, partes[2]


def validar(ruta: Path, estricto: bool):
    errores, avisos = [], []
    texto = ruta.read_text(encoding="utf-8")
    fm, cuerpo = leer_frontmatter(texto)

    if fm is None:
        return [f"{ruta}: sin frontmatter YAML"], []

    for campo in OBLIGATORIOS_ESTRUCTURALES:
        if campo not in fm:
            errores.append(f"{ruta}: falta el campo estructural '{campo}'")

    tipo = fm.get("type", "")
    if tipo and tipo not in TIPOS:
        errores.append(f"{ruta}: type '{tipo}' no pertenece al esquema")

    if tipo in TIPOS_CONTENIDO:
        for campo in OBLIGATORIOS_DOMINIO:
            if campo not in fm:
                errores.append(f"{ruta}: falta el campo de dominio '{campo}'")

        proc = fm.get("procedencia", "")
        if proc and proc not in PROCEDENCIAS:
            errores.append(f"{ruta}: procedencia '{proc}' inválida")

        est = fm.get("estado", "")
        if est and est not in ESTADOS:
            errores.append(f"{ruta}: estado '{est}' inválido")

        # cluster declarado: obligatorio salvo en paginas de autoria propia
        cl = fm.get("cluster", "").strip()
        if not cl:
            if tipo != "thesis":
                errores.append(f"{ruta}: falta 'cluster'; la cohesión no se puede medir")
        elif cl not in CLUSTERS:
            errores.append(f"{ruta}: cluster '{cl}' no está declarado en schema.md")

        # D4: separación autor / fuente
        if proc == "mixta" and ruta.parent.name != "queries":
            errores.append(
                f"{ruta}: procedencia 'mixta' sólo se admite en wiki/queries/"
            )
        if tipo == "thesis" and proc != "autor":
            errores.append(f"{ruta}: type 'thesis' exige procedencia 'autor'")
        if proc == "autor" and tipo != "thesis":
            avisos.append(
                f"{ruta}: procedencia 'autor' con type '{tipo}'; revisar si corresponde 'thesis'"
            )

        # subtipo y vigencia: schema.md, seccion «Tipos de pagina» y «Vigencia»
        sub = fm.get("subtipo", "").strip()
        if tipo == "entity" and sub and sub not in SUBTIPOS_ENTITY:
            errores.append(f"{ruta}: subtipo '{sub}' no está declarado en schema.md")
        vig = fm.get("vigencia", "").strip()
        if vig and vig not in VIGENCIAS:
            errores.append(f"{ruta}: vigencia '{vig}' inválida")
        if sub in SUBTIPOS_CON_VIGENCIA and not vig:
            errores.append(
                f"{ruta}: subtipo '{sub}' exige 'vigencia'; la política pública caduca"
            )

        # prefijos de nombre de archivo
        pref = PREFIJOS.get(tipo)
        if pref and not ruta.name.startswith(pref):
            errores.append(f"{ruta}: type '{tipo}' exige el prefijo '{pref}'")

        # sources vacío
        srcs = fm.get("sources", "").strip()
        if srcs in {"", "[]"} and tipo != "thesis":
            errores.append(
                f"{ruta}: 'sources' vacío; la señal de solapamiento (x4.0) no se calculará"
            )

        # verificación bibliográfica de fichas de fuente
        if tipo == "source":
            if "apa" not in fm:
                errores.append(f"{ruta}: ficha de fuente sin campo 'apa'")
            if fm.get("verificacion_bibliografica") == "pendiente" and estricto:
                errores.append(f"{ruta}: verificación bibliográfica pendiente")

        # trazabilidad
        if proc == "fuentes" and not RE_NOTA.search(cuerpo):
            avisos.append(f"{ruta}: sin ninguna nota de procedencia [^ext-N]/[^inf-N]")

        # inferencias sin confianza declarada
        for linea in cuerpo.splitlines():
            if linea.startswith("[^inf-") and not RE_CONFIANZA.search(linea):
                errores.append(
                    f"{ruta}: nota inferida sin nivel de confianza -> {linea.strip()[:60]}"
                )

    # nombre de archivo
    if ruta.stem != ruta.stem.lower() or " " in ruta.name:
        errores.append(f"{ruta}: nombre de archivo con mayúsculas o espacios")

    return errores, avisos


def main():
    ap = argparse.ArgumentParser(description="Valida el frontmatter de la wiki.")
    ap.add_argument("directorio", type=Path, help="Directorio wiki/ a revisar")
    ap.add_argument(
        "--estricto",
        action="store_true",
        help="Trata la verificación bibliográfica pendiente como error",
    )
    args = ap.parse_args()

    if not args.directorio.is_dir():
        print(f"No es un directorio: {args.directorio}", file=sys.stderr)
        return 2

    archivos = sorted(args.directorio.rglob("*.md"))
    if not archivos:
        print("No se encontraron archivos .md")
        return 0

    tot_err, tot_avi = [], []
    for archivo in archivos:
        e, a = validar(archivo, args.estricto)
        tot_err.extend(e)
        tot_avi.extend(a)

    for linea in tot_err:
        print(f"ERROR   {linea}")
    for linea in tot_avi:
        print(f"AVISO   {linea}")

    print(
        f"\n{len(archivos)} archivos | {len(tot_err)} errores | {len(tot_avi)} avisos"
    )
    return 1 if tot_err else 0


if __name__ == "__main__":
    sys.exit(main())
