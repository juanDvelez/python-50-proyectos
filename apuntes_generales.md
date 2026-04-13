# 📚 Apuntes Generales - Python

## Módulos usados
| Módulo | Para qué | Proyecto |
|--------|----------|----------|
| random | Números aleatorios | P02, P04 |
| string | Colección de caracteres | P03 |
| tkinter | Interfaces gráficas | P05 |
| datetime | Fechas y horas | P05 |
| requests | Peticiones a internet | P06 |
| os | Manejar archivos y carpetas del sistema | P07 |
| shutil | Mover y copiar archivos | P07 |
| collections | Estructuras de datos avanzadas | P08 

## Conceptos clave
| Concepto | Ejemplo | Proyecto |
|----------|---------|----------|
| f-strings | f"Hola {nombre}" | P01 |
| float() / int() | Convertir texto a número | P01 |
| while True + break | Bucle infinito | P02 |
| random.choice() | Elegir al azar de lista | P02 |
| "".join(lista) | Lista a texto | P03 |
| random.shuffle() | Mezclar lista | P03 |
| random.randint() | Número entero aleatorio | P04 |
| .isdigit() | Validar que sea número | P04 |
| tkinter Label | Texto en ventana gráfica | P05 |
| .after() | Repetir cada X milisegundos | P05 |
| requests.get() | Petición GET a una API | P06 |
| os.listdir() | Listar archivos de una carpeta | P07 |
| os.path.splitext() | Separar nombre y extensión | P07 |
| os.makedirs() | Crear carpetas automáticamente | P07 |
| shutil.move() | Mover archivos de lugar | P07 |
| dict.get(clave, 0) | Leer diccionario sin error | P07 |
| def funcion(): | Definir una función | P07 |
| collections | Estructuras de datos avanzadas | P08 
| Diccionarios anidados | Datos en múltiples niveles | P09 |
| .keys() | Obtener claves de diccionario | P09 |
| zip() | Unir dos listas en pares | P09 |
| Comparación encadenada | 0 <= x < total | P09 |


## Errores frecuentes y soluciones
| Error | Causa | Solución |
|-------|-------|----------|
| ValueError | float() con texto inválido | Validar con isdigit() |
| rejected push | GitHub tiene cambios locales no | git pull primero |
| ModuleNotFoundError | Librería no instalada | pip install nombre |
| FileNotFoundError | Ruta no existe | Verificar con os.path.exists() |
| KeyError | Clave no existe en diccionario | Usar dict.get(clave, default) |