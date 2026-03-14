# ================================
# Proyecto 01 - Calculadora de Propinas
# Autor: Juan David velez 
# ================================

# pedimos los datos al usuario
cuenta = float(input("Ingrese el monto de la cuenta: "))
# input() devuelve texto → float() lo convierte a número decimal
# Sin float(), no podrías hacer la multiplicación después
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar (ejemplo: 15 para 15%): "))
# Si la cuenta es $50 y el porcentaje es 15
# → 15 / 100 = 0.15
# → 50 * 0.15 = $7.50

# calculamos la propina
propina = cuenta * (porcentaje_propina / 100)
# calculamos el total a pagar
total = cuenta + propina

# mostramos los resultados al usuario
print("------------------------------")
print(f"Cuenta: ${cuenta:.2f}")# .2f → muestra el número con 2 decimales
print(f"Propina: ${propina:.2f}")# .2f → muestra el número con 2 decimales
print(f"Total a pagar: ${total:.2f}")# .2f → muestra el número con 2 decimales
print("------------------------------")

# f"..." es un f-string → permite meter variables dentro del texto
# :.2f → muestra exactamente 2 decimales (7.5 → 7.50)