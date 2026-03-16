# ================================
# Proyecto 07 - Organizador de Archivos
# Autor: Juan David  Velez
# Descripción: Organiza automáticamente los archivos de una carpeta en subcarpetas según su tipo (imágenes, videos, documentos, etc.).
# ================================

import os # Para manejar rutas y archivos
import shutil # Para mover archivos entre carpetas

# --- Tipos de archivos por categoría ---
CATEGORIAS = {
    "Imágenes"    : [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos"      : [".mp4", ".avi", ".mov", ".mkv", ".wmv"],
    "Documentos"  : [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Música"      : [".mp3", ".wav", ".flac", ".aac"],
    "Código"      : [".py", ".js", ".html", ".css", ".java", ".cpp"],
    "Comprimidos" : [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Otros"       : []
}

def obtener_categoria(extension):
    """Devuelve la categoría según la extensión del archivo."""
    for categoria, extensiones in CATEGORIAS.items():
        if extension.lower() in extensiones:
            return categoria
    return "Otros"

def organizar_carpeta(ruta):
    """Organiza todos los archivos de una carpeta."""

    # Verificar que la carpeta existe
    if not os.path.exists(ruta):
        print(f"❌ La carpeta '{ruta}' no existe.")
        return

    archivos      = os.listdir(ruta)
    organizados   = 0
    omitidos      = 0
    resumen       = {}

    print(f"\n📂 Organizando: {ruta}")
    print("─" * 45)

    for archivo in archivos:
        ruta_completa = os.path.join(ruta, archivo)

        # Solo procesar archivos, no carpetas
        if not os.path.isfile(ruta_completa):
            omitidos += 1
            continue

        # Obtener extensión
        _, extension = os.path.splitext(archivo)

        if not extension:
            omitidos += 1
            continue

        # Determinar categoría
        categoria = obtener_categoria(extension)

        # Crear carpeta destino si no existe
        destino = os.path.join(ruta, categoria)
        os.makedirs(destino, exist_ok=True)

        # Mover archivo
        shutil.move(ruta_completa, os.path.join(destino, archivo))

        # Contar por categoría
        resumen[categoria] = resumen.get(categoria, 0) + 1
        organizados += 1
        print(f"  ✅ {archivo} → {categoria}/")

    # Mostrar resumen
    print("\n============================")
    print("         RESUMEN            ")
    print("============================")
    for categoria, cantidad in resumen.items():
        print(f"  {categoria:<15} {cantidad} archivo(s)")
    print("─" * 30)
    print(f"  Organizados: {organizados}")
    print(f"  Omitidos:    {omitidos}")
    print("============================")

# --- Programa principal ---
print("============================")
print("   ORGANIZADOR DE ARCHIVOS  ")
print("============================")
print("\n¿Qué carpeta deseas organizar?")
print("  1. Mis Descargas")
print("  2. Escribir ruta manualmente")

opcion = input("\nOpción: ")

if opcion == "1":
    ruta = os.path.join(os.path.expanduser("~"), "Downloads")
elif opcion == "2":
    ruta = input("Escribe la ruta completa: ").strip()
else:
    print("⚠️ Opción inválida.")
    exit()

confirmar = input(f"\n⚠️  ¿Organizar '{ruta}'? (s/n): ").lower()

if confirmar == "s":
    organizar_carpeta(ruta)
else:
    print("❌ Operación cancelada.")