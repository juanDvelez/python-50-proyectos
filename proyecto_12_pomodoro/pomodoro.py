# ================================
# Proyecto 12 - Pomodoro Timer
# Autor: tu nombre
# ================================

import time
import os

# ---- Configuracion -------

CONFIG = {
    "trabajo": 25,  # Duración del trabajo en minutos
    "descanso_corto": 5,  # Duración del descanso corto en minutos
    "descanso_largo": 15,  # Duración del descanso largo en minutos
    "ciclos_maximos": 4,  # Número de ciclos antes del descanso largo
}

def clear_console():
    """Limpia la pantalla segun el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear') # Limpia la pantalla en Windows o Linux/Mac

def formatear_tiempo(segundos): # nos sirve para convertir segundos a formato mm:ss
    """Convierte segundos a formato mm:ss."""
    minutos, segundos = divmod(segundos, 60)
    return f"{minutos:02d}:{segundos:02d}"

def barra_progreso(restante, total, ancho=30): # nos sirve para generar una barra de progreso visual
    """Genera una barra de progreso visaul."""
    transcurrido = total - restante
    lleno        = int((transcurrido / total) * ancho)
    vacio        = ancho - lleno
    barra        = "█" * lleno + "░" * vacio
    porcentaje   = int((transcurrido / total) * 100)
    return f"[{barra}] {porcentaje}%"

def reproducir_aleta():
    """Hace un pitido de alerta."""
    print("\a", end="", flush=True )  # Esto hace un pitido en la mayoría de los sistemas"""
    time.sleep(0.2) # Pausa breve para que el pitido se escuche
    print("\a", end="", flush=True )  # Segundo pitido

def cuenta_regresiva(segundos_total, titulo, emoji):
    """Ejecuta la cuenta regresiva con visualización de barra de progreso y tiempo restante."""
    for restante in range(segundos_total, -1, -1):
        clear_console()

        print("=" * 40)
        print(f"{emoji} {titulo} {emoji}")
        print("=" * 40)

        tiempo = formatear_tiempo(restante)
        barra = barra_progreso(restante, segundos_total)

        print(f"\n ⏰ {tiempo}")
        print(f"\n {barra}")

        if restante <= 10 and restante > 0: # Alerta cuando quedan 10 segundos o menos
            print(f"\n ⚠️ ¡{restante} segundos restantes! ⚠️")

            print("\n Presione Ctrl+C para detener el temporizador.")
            print("= " * 40)

            if  restante > 0:
                time.sleep(1)  # Espera un segundo antes de actualizar la cuenta regresiva

        reproducir_aleta()  # Reproduce un pitido al finalizar la cuenta regresiva

def mostrar_estado(ciclo, ciclos_maximos, completados):
    """Muestra el estado actual del pomodoro, incluyendo el ciclo actual y los ciclos completados."""
    clear_console()
    print("=" * 40)
    print("  🍅 POMODORO TIMER")
    print("=" * 40)
    print(f"\n  Ciclo actual  : {ciclo}/{ciclos_maximos}")
    print(f"  Completados   : {completados} pomodoro(s)")

    progreso = "🍅" * completados + "⬜" * (ciclos_maximos - completados)
    print(f"  Progreso      : {progreso}")
    print("=" * 40)

# --- Programa principal ---
clear_console()
print("=" * 40)
print("  🍅 BIENVENIDO AL POMODORO TIMER")
print("=" * 40)
print("\n  Técnica Pomodoro:")
print("  → 25 min trabajo")
print("  → 5  min descanso corto")
print("  → 15 min descanso largo (cada 4 ciclos)")

print("\n¿Personalizar tiempos? (s/n): ", end="")
personalizar = input().lower()

if personalizar == "s":
    try:
        CONFIG["trabajo"]        = int(input("  Minutos de trabajo (default 25): ") or 25)
        CONFIG["descanso_corto"] = int(input("  Minutos descanso corto (default 5): ") or 5)
        CONFIG["descanso_largo"] = int(input("  Minutos descanso largo (default 15): ") or 15)
        CONFIG["ciclos_maximos"]     = int(input("  Ciclos antes del descanso largo (default 4): ") or 4)
    except ValueError:
        print("⚠️  Valores inválidos. Se usarán los defaults.")

input("\n  Presiona Enter para comenzar...")

ciclo_actual = 1
completados  = 0

try:
    while True:
        # --- Sesión de trabajo ---
        mostrar_estado(ciclo_actual, CONFIG["ciclos_maximos"], completados)
        input(f"\n  ▶️  Iniciar sesión de trabajo #{ciclo_actual}. Enter...")

        cuenta_regresiva(
            CONFIG["trabajo"] * 60,
            f"TRABAJANDO — Sesión #{ciclo_actual}",
            "💼"
        )

        completados += 1
        print(f"\n  ✅ ¡Sesión #{ciclo_actual} completada!")
        time.sleep(2)

        # --- Tipo de descanso ---
        if completados % CONFIG["ciclos_maximos"] == 0:
            tipo     = "descanso_largo"
            titulo   = "DESCANSO LARGO"
            emoji    = "🌴"
            minutos  = CONFIG["descanso_largo"]
        else:
            tipo     = "descanso_corto"
            titulo   = "DESCANSO CORTO"
            emoji    = "☕"
            minutos  = CONFIG["descanso_corto"]

        input(f"\n  ☕ Iniciar {titulo} ({minutos} min). Enter...")

        cuenta_regresiva(
            minutos * 60,
            titulo,
            emoji
        )

        print(f"\n  ✅ ¡Descanso terminado!")
        ciclo_actual += 1
        time.sleep(2)

except KeyboardInterrupt:
    print("\n\n  ⏸️  Timer pausado.")
    print(f"  Completaste {completados} pomodoro(s) hoy.")
    print("  ¡Buen trabajo! 🍅")


