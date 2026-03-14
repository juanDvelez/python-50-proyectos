# ====================================
# Proyecto 02: Piedra, Papel o Tijera
# ====================================

# Importamos random para generar la jugada de la computadora
import random

# Función para obtener la jugada del usuario
opciones = ["piedra", "papel", "tijera"]

# Marcador

victorias_usuario = 0
victorias_computadora = 0
empates = 0

print("============================")
print("   PIEDRA, PAPEL O TIJERA   ")
print("============================")

# Bucle principal del juego
while True:

    # Turno del jugador
    # Convertimos la entrada a minúsculas para evitar problemas de mayúsculas
    jugador = input(
        "\nElige (piedra / papel / tijera) o 'salir' para terminar: ").lower()

    # Opcion para salir
    if jugador == "salir":  # Si el usuario quiere salir del juego
        print("\n 🤩 Gracias por jugar. ¡Hasta luego!")
        break  # Salimos del bucle para terminar el juego

    # Validamos la entrada del usuario sea correcta
    if jugador not in opciones:  # Si la entrada del usuario no es válida
        print("🚨 Entrada no válida. Por favor, elige piedra, papel o tijera.")
        continue  # Volvemos al inicio del bucle para pedir una nueva entrada

    # Turno de la computadora
    # La computadora elige una opción al azar
    computadora = random.choice(opciones)
    print(f"💻 La computadora eligió: {computadora}")
    print(f"👤 Tú elegiste: {jugador}")

    # Determinamos el ganador
    if jugador == computadora:  # Si ambos eligen lo mismo, es un empate
        print("🤝 ¡Es un empate!")
        empates += 1

    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):  # Si el jugador gana
        print("🎉 ¡Ganaste!")
        victorias_usuario += 1

    else:  # Si la computadora gana
        print("😞 ¡Perdiste!")
        victorias_computadora += 1

    # Mostramos el marcador actualizado
    print(f"\n📊 Marcador: Usuario {victorias_usuario} - Computadora {victorias_computadora} - Empates {empates}") 

    # Resumen final

print("\n============================")
print("        RESUMEN FINAL       ")
print("============================")
print(f"Victorias: {victorias}")
print(f"Derrotas:  {derrotas}")
print(f"Empates:   {empates}")
print("¡Gracias por jugar!")
print("============================")