# ================================
# Proyecto 10 - Lista de Tareas
# Autor: tu nombre
# ================================

import json # Para manejar el almacenamiento de tareas en formato JSON
import os # Para verificar si el archivo de tareas existe
from datetime import datetime #

# --- Archivo donde se guardan las tareas ---
ARCHIVO = "tareas.json"

def cargar_tareas():
    """Carga las tareas desde el archivo JSON."""
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_tareas(tareas):
    """Guarda las tareas en el archivo JSON."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=4)

def agregar_tarea(tareas):
    """Agrega una nueva tarea."""
    titulo = input("\n  Nombre de la tarea: ").strip()
    if not titulo:
        print("⚠️  El nombre no puede estar vacío.")
        return

    prioridad = input("  Prioridad (alta/media/baja): ").lower()
    if prioridad not in ["alta", "media", "baja"]:
        prioridad = "media"

    tarea = {
        "id"        : len(tareas) + 1,
        "titulo"    : titulo,
        "prioridad" : prioridad,
        "completada": False,
        "fecha"     : datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    tareas.append(tarea)
    guardar_tareas(tareas)
    print(f"  ✅ Tarea '{titulo}' agregada.")

def listar_tareas(tareas):
    """Muestra todas las tareas."""
    if not tareas:
        print("\n  📭 No hay tareas pendientes.")
        return

    print("\n" + "=" * 50)
    print(f"  {'#':<4} {'TAREA':<25} {'PRIOR':<8} {'ESTADO'}")
    print("=" * 50)

    iconos_prioridad = {
        "alta"  : "🔴",
        "media" : "🟡",
        "baja"  : "🟢"
    }

    for tarea in tareas:
        estado  = "✅ hecha " if tarea["completada"] else "⏳ pendiente"
        icono   = iconos_prioridad.get(tarea["prioridad"], "⚪")
        print(
            f"  {tarea['id']:<4}"
            f" {tarea['titulo']:<25}"
            f" {icono} {tarea['prioridad']:<6}"
            f" {estado}"
        )

    total      = len(tareas)
    completadas = sum(1 for t in tareas if t["completada"])
    print("=" * 50)
    print(f"  Total: {total} | "
          f"Hechas: {completadas} | "
          f"Pendientes: {total - completadas}")

def completar_tarea(tareas):
    """Marca una tarea como completada."""
    listar_tareas(tareas)
    if not tareas:
        return

    try:
        id_tarea = int(input("\n  ID de la tarea completada: "))
        tarea = next(
            (t for t in tareas if t["id"] == id_tarea), None
        )

        if not tarea:
            print("⚠️  Tarea no encontrada.")
            return

        if tarea["completada"]:
            print("⚠️  Esa tarea ya estaba completada.")
            return

        tarea["completada"] = True
        guardar_tareas(tareas)
        print(f"  ✅ '{tarea['titulo']}' marcada como completada.")

    except ValueError:
        print("⚠️  Ingresa un número válido.")

def eliminar_tarea(tareas):
    """Elimina una tarea por ID."""
    listar_tareas(tareas)
    if not tareas:
        return

    try:
        id_tarea = int(input("\n  ID de la tarea a eliminar: "))
        tarea = next(
            (t for t in tareas if t["id"] == id_tarea), None
        )

        if not tarea:
            print("⚠️  Tarea no encontrada.")
            return

        confirmar = input(
            f"  ¿Eliminar '{tarea['titulo']}'? (s/n): "
        ).lower()

        if confirmar == "s":
            tareas.remove(tarea)
            # Reordenar IDs
            for i, t in enumerate(tareas, 1):
                t["id"] = i
            guardar_tareas(tareas)
            print("  🗑️  Tarea eliminada.")

    except ValueError:
        print("⚠️  Ingresa un número válido.")

def filtrar_tareas(tareas):
    """Filtra tareas por estado o prioridad."""
    print("\n  Filtrar por:")
    print("  1. Pendientes")
    print("  2. Completadas")
    print("  3. Prioridad alta")

    opcion = input("\n  Opción: ")

    if opcion == "1":
        filtradas = [t for t in tareas if not t["completada"]]
        titulo    = "TAREAS PENDIENTES"
    elif opcion == "2":
        filtradas = [t for t in tareas if t["completada"]]
        titulo    = "TAREAS COMPLETADAS"
    elif opcion == "3":
        filtradas = [t for t in tareas if t["prioridad"] == "alta"]
        titulo    = "TAREAS DE PRIORIDAD ALTA"
    else:
        print("⚠️  Opción inválida.")
        return

    print(f"\n  📋 {titulo} ({len(filtradas)})")
    listar_tareas(filtradas)

# --- Programa principal ---
print("============================")
print("    LISTA DE TAREAS (TODO)  ")
print("============================")

tareas = cargar_tareas()
print(f"  📂 {len(tareas)} tarea(s) cargada(s).")

while True:
    print("\n¿Qué deseas hacer?")
    print("  1. Ver todas las tareas")
    print("  2. Agregar tarea")
    print("  3. Completar tarea")
    print("  4. Eliminar tarea")
    print("  5. Filtrar tareas")
    print("  0. Salir")

    opcion = input("\nOpción: ")

    if opcion == "0":
        print("\n👋 ¡Hasta luego!")
        break
    elif opcion == "1":
        listar_tareas(tareas)
    elif opcion == "2":
        agregar_tarea(tareas)
    elif opcion == "3":
        completar_tarea(tareas)
    elif opcion == "4":
        eliminar_tarea(tareas)
    elif opcion == "5":
        filtrar_tareas(tareas)
    else:
        print("⚠️  Opción inválida.")