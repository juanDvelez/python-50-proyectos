# Proyecto 08 - Contador de Palabras

## Conceptos aprendidos

### open() y with
Abre archivos de forma segura.
with open(ruta, "r", encoding="utf-8") as f:
    texto = f.read()

### collections.Counter
Cuenta elementos de una lista automáticamente.
from collections import Counter
conteo = Counter(["a","a","b"]) → {"a":2, "b":1}

### .most_common(n)
Devuelve los n elementos más frecuentes.
conteo.most_common(10)

### List comprehension
Forma corta de crear listas con condición.
[p for p in palabras if len(p) > 1]

### Alineación en f-strings
:>n  → alinea a la derecha n espacios
:<n  → alinea a la izquierda n espacios

## Errores comunes
- UnicodeDecodeError → agregar encoding="utf-8"
- División por cero  → verificar if palabras antes
- Archivo no existe  → usar os.path.exists()

## ================================================================ ##

from collections import Counter
# Counter es una clase especial que cuenta
# elementos de una lista automáticamente
# Counter(["hola","hola","mundo"]) 
# → {"hola": 2, "mundo": 1}

conteo.most_common(10)
# Devuelve los 10 elementos más frecuentes
# ordenados de mayor a menor
# [("hola", 5), ("mundo", 3), ...]

palabras_filtradas = [
    p for p in palabras
    if p not in PALABRAS_IGNORAR and len(p) > 1
]
# Esto es una LIST COMPREHENSION
# Forma corta de crear una lista con condición
# equivale a:
# for p in palabras:
#     if p not in PALABRAS_IGNORAR:
#         palabras_filtradas.append(p)

with open(ruta, "r", encoding="utf-8") as archivo:
    texto = archivo.read()
# with → abre y cierra el archivo automáticamente
# "r"  → modo lectura (read)
# encoding="utf-8" → para leer tildes y ñ
# .read() → lee todo el contenido como texto

sum(len(p) for p in palabras)
# Generator expression → como list comprehension
# pero más eficiente en memoria
# Suma la longitud de cada palabra

f"  {i:>2}. {palabra:<20} {cantidad:>3}x"
# :>2  → alinea a la DERECHA en 2 espacios
# :<20 → alinea a la IZQUIERDA en 20 espacios
# :>3  → alinea a la DERECHA en 3 espacios
```

---

### 4️⃣ Prueba esperada
```
============================
     CONTADOR DE PALABRAS   
============================

¿Qué deseas analizar?
  1. Escribir texto directo
  2. Analizar un archivo .txt

Opción: 1

Escribe o pega tu texto.
Cuando termines escribe FIN en una línea aparte.
Python es un lenguaje de programación poderoso.
Python es fácil de aprender y muy usado en el mundo.
FIN

============================
       ANÁLISIS DE TEXTO    
============================
  Total caracteres : 98
  Total palabras   : 18
  Palabras únicas  : 12
  Promedio letras  : 4.5

  Top 10 palabras más usadas:
  ────────────────────────────
   1. python               2x  ██
   2. poderoso             1x  █
   3. lenguaje             1x  █
   4. programación         1x  █
   5. fácil                1x  █
============================