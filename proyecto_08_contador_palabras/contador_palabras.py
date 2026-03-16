# ================================
# Proyecto 08 - Contador de Palabras
# Autor: tu nombre
# ================================

import os
from collections import Counter

# --- Palabras a ignorar (artículos, preposiciones) ---
PALABRAS_IGNORAR = {
    "de", "la", "el", "en", "y", "a", "los", "las",
    "un", "una", "que", "se", "con", "por", "para",
    "es", "al", "del", "le", "su", "lo", "como",
    "the", "a", "an", "is", "in", "of", "to", "and"
}

def limpiar_texto(texto):
    """Elimina caracteres especiales y convierte a minúsculas."""
    caracteres_especiales = ".,;:!?¡¿()[]{}\"'—-\n\t"
    for char in caracteres_especiales:
        texto = texto.replace(char, " ")
    return texto.lower()

def analizar_texto(texto):
    """Analiza el texto y devuelve estadísticas."""
    texto_limpio  = limpiar_texto(texto)
    palabras      = texto_limpio.split()

    # Filtrar palabras vacías e ignoradas
    palabras_filtradas = [
        p for p in palabras
        if p not in PALABRAS_IGNORAR and len(p) > 1
    ]

    conteo = Counter(palabras_filtradas)

    return {
        "total_caracteres"  : len(texto),
        "total_palabras"    : len(palabras),
        "palabras_unicas"   : len(conteo),
        "mas_frecuentes"    : conteo.most_common(10),
        "promedio_longitud" : round(
            sum(len(p) for p in palabras) / len(palabras), 2
        ) if palabras else 0
    }

def mostrar_resultados(stats):
    """Muestra los resultados del análisis."""
    print("\n============================")
    print("       ANÁLISIS DE TEXTO    ")
    print("============================")
    print(f"  Total caracteres : {stats['total_caracteres']}")
    print(f"  Total palabras   : {stats['total_palabras']}")
    print(f"  Palabras únicas  : {stats['palabras_unicas']}")
    print(f"  Promedio letras  : {stats['promedio_longitud']}")
    print("\n  Top 10 palabras más usadas:")
    print("  ─" * 20)
    for i, (palabra, cantidad) in enumerate(stats["mas_frecuentes"], 1):
        barra = "█" * cantidad
        print(f"  {i:>2}. {palabra:<20} {cantidad:>3}x  {barra}")
    print("============================")

# --- Programa principal ---
print("============================")
print("     CONTADOR DE PALABRAS   ")
print("============================")
print("\n¿Qué deseas analizar?")
print("  1. Escribir texto directo")
print("  2. Analizar un archivo .txt")

opcion = input("\nOpción: ")

if opcion == "1":
    print("\nEscribe o pega tu texto.")
    print("Cuando termines escribe FIN en una línea aparte.")
    lineas = []
    while True:
        linea = input()
        if linea.strip().upper() == "FIN":
            break
        lineas.append(linea)
    texto = "\n".join(lineas)

elif opcion == "2":
    ruta = input("Ruta del archivo .txt: ").strip()
    if not os.path.exists(ruta):
        print("❌ Archivo no encontrado.")
        exit()
    with open(ruta, "r", encoding="utf-8") as archivo:
        texto = archivo.read()

else:
    print("⚠️ Opción inválida.")
    exit()

if texto.strip():
    stats = analizar_texto(texto)
    mostrar_resultados(stats)
else:
    print("⚠️ No hay texto para analizar.")