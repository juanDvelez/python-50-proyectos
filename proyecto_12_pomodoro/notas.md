# Proyecto 12 - Pomodoro Timer

## Conceptos aprendidos

### time.sleep(n)
Pausa el programa exactamente n segundos.
import time
time.sleep(1)  → pausa 1 segundo

### divmod(a, b)
Devuelve cociente y residuo en una sola operación.
minutos, segs = divmod(90, 60)  → (1, 30)

### range(inicio, fin, paso)
Cuenta hacia atrás con paso negativo.
range(10, -1, -1) → 10, 9, 8 ... 1, 0

### :02d en f-strings
Rellena con ceros hasta 2 dígitos.
f"{5:02d}" → "05"

### KeyboardInterrupt
Captura Ctrl+C para cerrar limpiamente.
try:
    while True: ...
except KeyboardInterrupt:
    print("Programa cerrado")

### os.name
Detecta el sistema operativo.
"nt"    → Windows
"posix" → Mac / Linux

## Errores comunes
- sleep() congela TODO el programa → normal en consola
- Ctrl+C sin except → muestra error feo → usar KeyboardInterrupt
- :02d solo para enteros → para float usar :05.2f