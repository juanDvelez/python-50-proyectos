# Proyecto 09 - Convertidor de Unidades

## Conceptos aprendidos

### Diccionarios anidados
Diccionario dentro de diccionario.
datos = {"Longitud": {"unidades": [...], "a_base": [...]}}
acceso: datos["Longitud"]["unidades"]

### .keys()
Devuelve todas las claves de un diccionario.
list(diccionario.keys()) → lista de claves

### zip()
Une dos listas en pares.
zip(["a","b"], [1,2]) → [("a",1), ("b",2)]

### Comparaciones encadenadas
Python permite: 0 <= valor < total
equivale a: valor >= 0 AND valor < total

### Truco unidad base
Para convertir entre N unidades solo necesitas
los factores hacia una unidad base:
origen → base → destino

## Errores comunes
- Índice fuera de rango → validar con 0 <= idx < total
- ValueError en float() → usar try/except
- División por cero → no aplica si factores > 0