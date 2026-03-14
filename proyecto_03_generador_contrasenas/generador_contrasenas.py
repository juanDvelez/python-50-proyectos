# ================================
# Proyecto 03 - Generador de Contraseñas
# Autor: tu nombre
# ================================

import random # Importamos el módulo random para generar números aleatorios
import string # Importamos el módulo string para acceder a caracteres predefinidos


print("====================================")
print("   GENERADOR DE CONTRASEÑAS SEGURAS  ")
print("====================================")

# --- Configuración de la contraseña ---
longitud = int(input("Ingrese la longitud deseada para la contraseña (mínimo 8 caracteres): "))

if longitud < 8:
    print(" 🚨 La longitud mínima recomendada es de 8 caracteres. Se establecerá la longitud en 8.")
    longitud = 8

incluir_mayusculas = input("¿Desea incluir letras mayúsculas? (s/n): ").lower() == 's' # Preguntamos al usuario si desea incluir letras mayúsculas y convertimos la respuesta a minúscula para facilitar la comparación
incluir_minusculas = input("¿Desea incluir letras minúsculas? (s/n): ").lower() == 's' # Preguntamos al usuario si desea incluir letras minúsculas y convertimos la respuesta a minúscula para facilitar la comparación
incluir_numeros = input("¿Desea incluir números? (s/n): ").lower() == 's' # Preguntamos al usuario si desea incluir números y convertimos la respuesta a minúscula para facilitar la comparación
incluir_simbolos = input("¿Desea incluir símbolos especiales? (s/n): ").lower() == 's' # Preguntamos al usuario si desea incluir símbolos especiales y convertimos la respuesta a minúscula para facilitar la comparación

# --- construir la lista de caracteres permitidos ---
banco = list(string.ascii_lowercase) # Iniciamos el banco de caracteres con las letras minúsculas

if incluir_mayusculas:
    banco.extend(string.ascii_uppercase) # Si el usuario desea incluir mayúsculas, las agregamos al banco de caracteres
if incluir_numeros:
    banco.extend(string.digits) # Si el usuario desea incluir números, los agregamos al banco de caracteres
if incluir_simbolos:
    banco.extend(string.punctuation) # Si el usuario desea incluir símbolos, los agregamos al banco de caracteres

    # ---- Garantizar al menos 1 de cada tipo elegido ---
contraseña = []

contraseña.append(random.choice(string.ascii_lowercase)) # Agregamos al menos una letra minúscula

if incluir_mayusculas:
    contraseña.append(random.choice(string.ascii_uppercase)) # Si el usuario desea incluir mayúsculas, agregamos al menos una letra mayúscula
if incluir_numeros:
    contraseña.append(random.choice(string.digits)) # Si el usuario desea incluir números, agregamos al menos un número
if incluir_simbolos:
    contraseña.append(random.choice(string.punctuation)) # Si el usuario desea incluir símbolos, agregamos al menos un símbolo

# --- Completar la contraseña con caracteres aleatorios del banco ---
restante = longitud - len(contraseña) # Calculamos cuántos caracteres faltan para completar la longitud deseada
contraseña += random.choices(banco, k=restante) # Agregamos caracteres aleatorios del banco para completar la contraseña

# --- Mezclar la contraseña para evitar patrones predecibles ---
random.shuffle(contraseña) # Mezclamos los caracteres de la contraseña para que no sigan un orden predecible

# --- convertir la lista en texto ---
contraseña_final = ''.join(contraseña) # Convertimos la lista de caracteres en una cadena de texto

print("\n====================================")
print(f"  Contraseña: {contraseña_final}")
print(f"  Longitud:   {len(contraseña_final)} caracteres")
print("====================================")

# --- Indicadores de seguridad ---
if longitud >= 12 and incluir_simbolos and incluir_numeros and incluir_mayusculas:
    nivel = "🟢 MUY FUERTE"
elif longitud >= 10 and (incluir_simbolos or incluir_numeros):
    nivel = "🟡 FUERTE"
elif longitud >= 8:
    nivel = "🟠 MEDIA"
else:
    nivel = "🔴 DÉBIL"

print(f"  Nivel de seguridad: {nivel}")
print("====================================")
    
