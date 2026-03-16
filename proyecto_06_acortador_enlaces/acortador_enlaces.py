# ================================
# Proyecto 06 - Acortador de Enlaces
# Autor: Juan David Velez
# ================================

import pyshorteners  # Importamos la biblioteca pyshorteners para acortar enlaces

# --- Historial de URLs acortadas ---
historial = []  # Lista para almacenar el historial de URLs acortadas

print("============================")
print("     ACORTADOR DE ENLACES   ")
print("============================")

while True:
    print("\n¿Qué deseas hacer?")
    print("1. Acortar un enlace")
    print("2. Ver historial de enlaces acortados")
    print("3. Salir")

    opcion = input("Selecciona una opción (1, 2 o 3): ")

    # --- Acortar un enlace ---
    if opcion == '1':
        # Solicitamos al usuario que ingrese la URL y eliminamos espacios en blanco
        url = input("Pega tu enlace aquí: ").strip()

        # Validamos que sea una URL válida (simple validación)
        if not url.startswith("http://") and not url.startswith("https://"):
            print("Por favor, ingresa una URL válida que comience con http:// o https://")
            continue

        # intentar acortar la URL

        try:
            acortador = pyshorteners.Shortener()  # Creamos una instancia del acortador
            # Acortamos la URL utilizando el servicio TinyURL
            url_acortada = acortador.tinyurl.short(url)

            print(f"\n✅ URL original: {url}")
            print(f"✅ URL acortada: {url_acortada}")

            # Guardamos en el historial
            historial.append({
                "original": url,
                "acortada": url_acortada
            })

        except Exception as error:
            print(f"❌ Error al acortar: {error}")
            print("   Verifica tu conexión a internet.")

    # --- Ver historial ---
    elif opcion == "2":
        if len(historial) == 0:
            print("\n📭 No hay URLs en el historial.")
        else:
            print(f"\n📋 Historial ({len(historial)} enlaces):")
            print("─" * 45)
            for i, item in enumerate(historial, 1):
                print(f"{i}. Original: {item['original']}")
                print(f"   Corta:    {item['corta']}")
                print("─" * 45)

    # --- Salir ---
    elif opcion == "3":
        print("\n👋 ¡Hasta luego!")
        break

    else:
        print("⚠️  Opción inválida.")
