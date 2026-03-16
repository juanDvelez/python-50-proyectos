# ================================
# Proyecto 04 - Adivina el Número
# Autor: juan David velez
# ================================

import random


print("===============================")
print("       ADIVINA EL NÚMERO       ")
print("===============================")

# ----- Elegir dificultad -----
print("\nElegir dificultad:")
print(" 1. Facil  (1-50, 10 intentos)")
print(" 2. Medio  (1-100, 7 intentos)")
print(" 3. Dificil (1-200, 5 intentos)")

dificulta = input("\nOpción (1/2/3):  ")

if dificulta == "1": 
    limite   = 50
    intentos = 10
    nivel    = "Fácil"
elif dificulta == "2":
    limite   = 100
    intentos = 7
    nivel    = "Medio"
elif dificulta == "3":
    limite   = 200
    intentos = 5
    nivel    = "Difícil"
else:
    print("🚨 Opción no válida. Se usara nivel Medio por defecto.")
    limite   = 100
    intentos = 7
    nivel    = "Medio"

# ----- Generar número aleatorio -----
numero_secreto  = random.randint(1, limite)
intentos_usados = 0
adivinado       = False

print(f"\n🎯 Nivel: {nivel} | Rango: 1 - {limite} | Intentos: {intentos}")
print("-" * 40) # esto hace una linea de guiones para separar la informacion


# ----- Bucle principal del juego -----
while intentos_usados < intentos:
    intentos_restantes = intentos - intentos_usados
    intento = input(f"\nIntento {intentos_usados + 1} de {intentos} - Ingresa tu número: ")
    if not intento.isdigit():
        print("🚨 Por favor ingresa un número válido.")
        continue

    intento = int(intento)
    intentos_usados += 1

    # Verificar
    if intento == numero_secreto:
        adivinado = True
        break
    elif intento < numero_secreto:
        print(f"  📈 El número es MAYOR que {intento}")
    else:
        print(f"  📉 El número es MENOR que {intento}")

    # Pista extra cuando quedan pocos intentos
    if intentos_restantes == 2:
        if numero_secreto % 2 == 0:
            print("  💡 Pista: el número es PAR")
        else:
            print("  💡 Pista: el número es IMPAR")

# --- Resultado final ---
print("\n============================")
if adivinado:
    print(f"  🏆 ¡CORRECTO!")
    print(f"  El número era: {numero_secreto}")
    print(f"  Lo lograste en {intentos_usados} intento(s)")

    if intentos_usados == 1:
        print("  ⭐ ¡Increíble, a la primera!")
    elif intentos_usados <= intentos // 2:
        print("  ⭐ ¡Excelente puntaje!")
    else:
        print("  👍 ¡Bien hecho!")
else:
    print(f"  💀 ¡Se acabaron los intentos!")
    print(f"  El número era: {numero_secreto}")
print("============================")