# ================================
# Proyecto 05 - Reloj Digital
# Autor: Juan David velez
# ================================

import tkinter as tk
from datetime import datetime

# --- Función que actualiza el reloj ---
def actualizar_reloj():
    # Obtener hora actual
    ahora        = datetime.now()
    hora         = ahora.strftime("%H:%M:%S")
    fecha        = ahora.strftime("%A, %d de %B del %Y")
    
    # Actualizar los labels
    label_hora.config(text=hora)
    label_fecha.config(text=fecha)
    
    # Llamarse a sí misma cada 1000ms (1 segundo)
    ventana.after(1000, actualizar_reloj)

# --- Crear la ventana principal ---
ventana = tk.Tk()
ventana.title("Reloj Digital")
ventana.geometry("400x200")
ventana.resizable(False, False)
ventana.configure(bg="#1a1a2e")

# --- Título ---
label_titulo = tk.Label(
    ventana,
    text="🕐 RELOJ DIGITAL",
    font=("Courier", 14, "bold"),
    bg="#1a1a2e",
    fg="#e94560"
)
label_titulo.pack(pady=10)

# --- Label de la hora ---
label_hora = tk.Label(
    ventana,
    text="",
    font=("Courier", 52, "bold"),
    bg="#1a1a2e",
    fg="#00d4ff"
)
label_hora.pack()

# --- Label de la fecha ---
label_fecha = tk.Label(
    ventana,
    text="",
    font=("Courier", 12),
    bg="#1a1a2e",
    fg="#a8a8b3"
)
label_fecha.pack(pady=10)

# --- Arrancar el reloj ---
actualizar_reloj()
ventana.mainloop()