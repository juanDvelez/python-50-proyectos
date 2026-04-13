
# =================================================================
# Proyecto 09 - Convertidor de unidades
# Autor: Juan David velez
# ================================================================

# --- Factores de la conversion a la unidad base (metros) ---

CONVERSIONES = {
    "Longitud": {
        "unidades": ["metros", "kilómetros", "centímetros", "milímetros", "pulgadas", "pies", "millas"],
        "a_base": [1, 1000, 0.01, 0.001, 0.0254, 0.3048, 1609.34],
        "simbolo": ["m", "km", "cm", "mm", "in", "ft", "mi"]
    },
    "Peso": {
        "unidades": ["kilogramos", "gramos", "libras", "onzas", "toneladas"],
        "a_base": [1, 0.001, 0.453592, 0.0283495, 1000],
        "simbolo": ["kg", "g", "lb", "oz", "t"]
    },
    "Temperatura": {
        "unidades": ["Celsius", "Fahrenheit", "Kelvin"],
        "a_base": None,  # La conversión de temperatura no es lineal, se manejará con funciones específicas
        "simbolo": ["°C", "°F", "K"]
    },
    "Velocidad": {
        "unidades": ["metros por segundo", "kilómetros por hora", "millas por hora", "nudos"],
        "a_base": [1, 0.277778, 0.44704, 0.514444],
        "simbolo": ["m/s", "km/h", "mph", "kn"]
    },
    "Area": {
        "unidades": ["metros cuadrados", "kilómetros cuadrados", "hectáreas", "pies cuadrados", "acres"],
        "a_base": [1, 1000000, 10000, 9.2903, 4046.86],
        "simbolo": ["m²", "km²", "ha", "ft²", "ac"]
    }
}


def convertir_temperatura(valor, unidad_origen, unidad_destino):
    """Conversion especial para temperatura"""

    # Primero convertir a Celsius como base
    if unidad_origen == "Fahrenheit":  # Fahrenheit a Celsius
        # Formula de conversion de Fahrenheit a Celsius
        celsius = (valor - 32) * 5.0/9.0
    elif unidad_origen == "Kelvin":
        celsius = valor - 273.15  # Formula de conversion de Kelvin a Celsius
    else:
        celsius = valor

    # Luego convertir de Celsius a la unidad destino
    if unidad_destino == "Fahrenheit":  # Celsius a Fahrenheit
        return celsius * 9.0/5.0 + 32  # Formula de conversion de Celsius a Fahrenheit
    elif unidad_destino == "Kelvin":
        return celsius + 273.15  # Formula de conversion de Celsius a Kelvin
    else:
        return celsius


def convertir(valor, categoria, idx_origen, idx_destino):
    """Convertir un valor entre unidades."""
    datos = CONVERSIONES[categoria]

    # Caso especial: Temperatura
    if categoria == "Temperatura":
        origen = datos["unidades"][idx_origen]  # Obtener la unidad de origen
        # Obtener la unidad de destino
        destino = datos["unidades"][idx_destino]
        # Llamar a la funcion de conversion de temperatura
        return convertir_temperatura(valor, origen, destino)

    # Conversion general: origen -> base -> destino
    # Obtener el factor de conversion a la unidad base para la unidad de origen
    factor_origen = datos["a_base"][idx_origen]
    # Obtener el factor de conversion a la unidad base para la unidad de destino
    factor_destino = datos["a_base"][idx_destino]

    valor_base = valor * factor_origen  # Convertir el valor a la unidad base
    # Convertir el valor de la unidad base a la unidad destino
    valor_destino = valor_base / factor_destino
    return valor_destino


def mostrar_menu_unidades(categoria):
    """Muestra las unidades disponibles para una categoría."""
    datos = CONVERSIONES[categoria]
    print(f"\n Unidades disponibles para {categoria}:")
    for i, (unidad, simbolo) in enumerate(zip(datos["unidades"], datos["simbolo"]), 1):
        print(f"  {i}. {unidad} ({simbolo})")


if __name__ == "__main__":
    print("============================")
    print("    CONVERTIDOR DE UNIDADES ")
    print("============================")

    while True:
        # Menú de categorías
        print("\n¿Qué deseas convertir?")
        categorias = list(CONVERSIONES.keys())

        for i, cat in enumerate(categorias, 1):
            print(f"  {i}. {cat}")
        print(f"  {len(categorias) + 1}. Salir")

        try:
            opcion = int(input("\nOpción: "))

            if opcion == len(categorias) + 1:
                print("\n👋 ¡Hasta luego!")
                break

            elif 1 <= opcion <= len(categorias):
                categoria = categorias[opcion - 1]

            else:
                print("⚠️  Opción inválida.")
                continue

        except ValueError:
            print("⚠️  Ingresa solo números.")
            continue

        # Mostrar unidades disponibles
        mostrar_menu_unidades(categoria)
        total = len(CONVERSIONES[categoria]["unidades"])

        # Seleccionar unidad origen
        try:
            origen = int(input("\n  De (número): "))
            destino = int(input("  A  (número): "))

            if not (1 <= origen <= total) or \
               not (1 <= destino <= total):
                print("⚠️  Número fuera de rango.")
                continue

            valor = float(input("  Valor a convertir: "))

        except ValueError:
            print("⚠️  Ingresa solo números.")
            continue

        # Calcular y mostrar resultado
        resultado = convertir(valor, categoria, origen - 1, destino - 1)

        simbolos = CONVERSIONES[categoria]["simbolo"]
        unidades = CONVERSIONES[categoria]["unidades"]

        print(f"\n  ✅ {valor} {simbolos[origen - 1]}"
              f" = {round(resultado, 6)} {simbolos[destino - 1]}")
        print(f"     ({unidades[origen - 1]} → {unidades[destino - 1]})")
