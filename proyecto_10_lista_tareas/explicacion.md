import json
# JSON = JavaScript Object Notation
# Formato estándar para guardar datos estructurados
# Los diccionarios de Python se convierten a JSON
# perfectamente → {"clave": "valor"}

json.dump(tareas, f, ensure_ascii=False, indent=4)
# json.dump() → escribe datos Python en archivo JSON
# ensure_ascii=False → guarda tildes y ñ correctamente
# indent=4 → formato legible con sangría de 4 espacios

json.load(f)
# Lee el archivo JSON y lo convierte a
# diccionarios/listas de Python automáticamente

open(ARCHIVO, "w", encoding="utf-8")
# "r" → solo leer
# "w" → escribir (borra el contenido anterior)
# "a" → agregar al final sin borrar

tarea = next(
    (t for t in tareas if t["id"] == id_tarea), None
)
# next() con generator expression
# Busca el PRIMER elemento que cumpla la condición
# Si no encuentra ninguno devuelve None

sum(1 for t in tareas if t["completada"])
# Cuenta cuántas tareas tienen completada = True
# sum() suma todos los 1 que genera el generator