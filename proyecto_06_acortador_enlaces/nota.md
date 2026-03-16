# Proyecto 06 - Acortador de Enlaces

## Conceptos aprendidos

### pip install
Instala librerías externas que no vienen con Python.
pip install pyshorteners

### try / except
Maneja errores sin que el programa se cierre.
try:
    codigo_riesgoso()
except Exception as error:
    print(f"Error: {error}")

### startswith()
Verifica cómo empieza un texto.
"https://google.com".startswith("https://") → True

### append()
Agrega un elemento al final de una lista.
lista.append({"clave": "valor"})

### enumerate()
Da índice y valor al recorrer una lista.
for i, item in enumerate(lista, 1):

## Lista de diccionarios
Estructura muy usada para guardar datos relacionados.
historial = [{"original": url, "corta": url_corta}]

## Errores comunes
- URL sin http:// → validar con startswith()
- Sin internet → capturar con try/except
- ModuleNotFoundError → pip install pyshorteners