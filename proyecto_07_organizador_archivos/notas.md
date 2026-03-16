# Proyecto 07 - Organizador de Archivos

## Conceptos aprendidos

### os.listdir()
Lista todos los archivos de una carpeta.
archivos = os.listdir("/ruta/carpeta")

### os.path.isfile()
Verifica si una ruta es un archivo (no carpeta).
os.path.isfile(ruta) → True / False

### os.path.splitext()
Separa nombre y extensión de un archivo.
"foto.jpg" → ("foto", ".jpg")

### os.makedirs()
Crea carpetas automáticamente.
os.makedirs(ruta, exist_ok=True)

### shutil.move()
Mueve un archivo de una ruta a otra.
shutil.move(origen, destino)

### diccionario.get(clave, default)
Obtiene valor sin error si la clave no existe.
resumen.get("Imágenes", 0)

## Errores comunes
- Ruta no existe → verificar con os.path.exists()
- Mezclar / y \ en rutas → usar os.path.join()
- Mover carpetas → filtrar con os.path.isfile()