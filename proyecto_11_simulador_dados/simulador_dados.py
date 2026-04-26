# ================================
# Proyecto 11 - Simulador de Dados
# Autor: tu nombre
# ================================

import random

# --- Tipos de dados disponibles ---
DADOS = {
    "1": {"nombre": "d4",  "caras": 4},# Puedes agregar más dados si quieres, por ejemplo:
    "2": {"nombre": "d6",  "caras": 6}, # Puedes agregar más dados si quieres, por ejemplo:
    "3": {"nombre": "d8",  "caras": 8},
    "4": {"nombre": "d10", "caras": 10},
    "5": {"nombre": "d12", "caras": 12},
    "6": {"nombre": "d20", "caras": 20},
}

def lanzar_dados(caras, cantidad, veces): 
    """Lanza varios dados múltiples veces."""
    resultados = []
    for _ in range(veces):
        total = sum(
            random.randint(1, caras)
            for _ in range(cantidad)
        )
        resultados.append(total)
    return resultados

def calcular_estadisticas(resultados, caras, cantidad):
    """Calcula estadísticas de los resultados."""
    total        = len(resultados)
    suma         = sum(resultados)
    media        = suma / total
    minimo       = min(resultados)
    maximo       = max(resultados)
    minimo_pos   = 1 * cantidad
    maximo_pos   = caras * cantidad

    # Frecuencia de cada resultado
    frecuencia = {}
    for r in resultados:
        frecuencia[r] = frecuencia.get(r, 0) + 1

    # Moda → el resultado más frecuente
    moda = max(frecuencia, key=frecuencia.get)

    return {
        "total"     : total,
        "media"     : round(media, 2),
        "minimo"    : minimo,
        "maximo"    : maximo,
        "min_pos"   : minimo_pos,
        "max_pos"   : maximo_pos,
        "moda"      : moda,
        "frecuencia": frecuencia
    }

def mostrar_grafica(frecuencia, veces):
    """Muestra gráfica de barras en consola."""
    max_frec  = max(frecuencia.values())
    max_barras = 30

    print("\n  📊 Distribución de resultados:")
    print("  " + "─" * 45)

    for valor in sorted(frecuencia.keys()):
        frec     = frecuencia[valor]
        porcentaje = (frec / veces) * 100
        barras   = int((frec / max_frec) * max_barras)
        barra    = "█" * barras

        print(f"  {valor:>4} | {barra:<30} {frec:>4}x {porcentaje:>5.1f}%")

    print("  " + "─" * 45)

def mostrar_estadisticas(stats):
    """Muestra el resumen estadístico."""
    print("\n  📈 Estadísticas:")
    print(f"  Lanzamientos : {stats['total']}")
    print(f"  Media        : {stats['media']}")
    print(f"  Más frecuente: {stats['moda']}")
    print(f"  Mínimo real  : {stats['minimo']} "
          f"(posible: {stats['min_pos']})")
    print(f"  Máximo real  : {stats['maximo']} "
          f"(posible: {stats['max_pos']})")

# --- Programa principal ---
print("==============================")
print("  SIMULADOR DE DADOS          ")
print("==============================")

while True:
    # Elegir tipo de dado
    print("\n  Tipo de dado:")
    for k, v in DADOS.items():
        print(f"    {k}. {v['nombre']} ({v['caras']} caras)")
    print("    0. Salir")

    opcion = input("\n  Opción: ")

    if opcion == "0":
        print("\n👋 ¡Hasta luego!")
        break

    if opcion not in DADOS:
        print("⚠️  Opción inválida.")
        continue

    dado = DADOS[opcion]

    try:
        cantidad = int(input(f"  ¿Cuántos {dado['nombre']} lanzar a la vez? "))
        veces    = int(input("  ¿Cuántas veces lanzar? (ej: 1000): "))

        if cantidad < 1 or veces < 1:
            print("⚠️  Ingresa números mayores a 0.")
            continue

    except ValueError:
        print("⚠️  Ingresa solo números enteros.")
        continue

    # Simular
    print(f"\n  🎲 Lanzando {cantidad}x{dado['nombre']} "
          f"un total de {veces} veces...")

    resultados = lanzar_dados(dado["caras"], cantidad, veces)
    stats      = calcular_estadisticas(
        resultados, dado["caras"], cantidad
    )

    mostrar_estadisticas(stats)
    mostrar_grafica(stats["frecuencia"], veces)