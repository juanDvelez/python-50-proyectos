# ================================
# Proyecto 01 - Calculadora de Propinas
# Versión 2 - División entre personas
# Autor: Juan David velez
# ================================

#------Entrada de datos------
cuenta = float(input("Ingrese el monto de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar (ejemplo: 15 para 15%): "))
personas = int(input("Ingrese el número de personas que van a dividir la cuenta: "))


#------Cálculos------
propina = cuenta * (porcentaje_propina / 100)# calculamos la propina
total = cuenta + propina # calculamos el total a pagar
total_por_persona = total / personas # calculamos el total a pagar por persona
propina_por_persona = propina / personas # calculamos la propina por persona

#------Salida de datos------
print("\n============================")
print("      RESUMEN DE CUENTA     ")
print("============================")
print(f"Cuenta: ${cuenta:.2f}")
print(f"Propina: ${propina:.2f}")
print(f"Total a pagar: ${total:.2f}")
print("----------------------------")
print(f"Personas: {personas}")
print(f"Propina por persona: ${propina_por_persona:.2f}")
print(f"Total por persona: ${total_por_persona:.2f}")
print("============================")