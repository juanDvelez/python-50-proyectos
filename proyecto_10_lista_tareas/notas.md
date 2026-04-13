# Proyecto 10 - Lista de Tareas

## Conceptos aprendidos

### json.dump() y json.load()
Guardar y leer datos estructurados en archivos.
json.dump(datos, archivo, ensure_ascii=False, indent=4)
datos = json.load(archivo)

### Modos de open()
"r" → leer       (read)
"w" → escribir   (write) - borra contenido anterior
"a" → agregar    (append) - no borra

### next() con generator
Busca el primer elemento que cumple condición.
tarea = next((t for t in lista if t["id"] == id), None)

### Persistencia de datos
Los datos se guardan en tareas.json → no se pierden
al cerrar el programa.

### sum() con generator
Cuenta elementos que cumplen una condición.
sum(1 for t in tareas if t["completada"])

## Errores comunes
- JSONDecodeError → archivo JSON corrupto o vacío
- Usar "w" cuando querías "a" → borra datos
- ID no encontrado → siempre verificar con next()