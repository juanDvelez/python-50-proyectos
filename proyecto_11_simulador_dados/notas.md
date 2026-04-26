# Proyecto 11 - Simulador de Dados

## Conceptos aprendidos

### range(n)
Repite un bloque N veces exactas.
for _ in range(1000):  # repite 1000 veces

### _ como variable
Indica que la variable no se usa.
for _ in range(n): → solo nos importa repetir

### max() con key=
Encuentra el máximo evaluando una función.
max(diccionario, key=diccionario.get)
→ clave con el valor más alto

### sorted()
Ordena cualquier iterable.
sorted([3,1,2]) → [1,2,3]
sorted(diccionario.keys()) → claves ordenadas

### Gráfica ASCII
Escalar valores a un máximo de barras:
barras = int((valor / maximo) * max_barras)

## Errores comunes
- _ no es error → es convención para variable no usada
- max() en dict vacío → verificar que tenga datos
- División por cero en porcentaje → verificar veces > 0



for _ in range(veces):
# range(n) genera números del 0 al n-1
# _ significa que no usamos la variable
# solo queremos repetir N veces

sum(random.randint(1, caras) for _ in range(cantidad))
# Generator dentro de sum()
# Lanza el dado 'cantidad' veces y suma todo
# 3 dados de 6: randint(1,6) + randint(1,6) + randint(1,6)

moda = max(frecuencia, key=frecuencia.get)
# max() con key= → evalúa cada elemento con esa función
# busca la clave cuyo VALOR en frecuencia es mayor
# el resultado más repetido

sorted(frecuencia.keys())
# sorted() → ordena cualquier iterable
# Devuelve una lista ordenada de menor a mayor

barras = int((frec / max_frec) * max_barras)
# Regla de tres para escalar la barra
# si frec=max_frec → barra completa (30 bloques)
# si frec=mitad    → barra de 15 bloques


==============================
  SIMULADOR DE DADOS          
==============================

  Tipo de dado:
    1. d4  (4 caras)
    2. d6  (6 caras)
    ...

  Opción: 2
  ¿Cuántos d6 lanzar a la vez? 2
  ¿Cuántas veces lanzar?: 1000

  🎲 Lanzando 2xd6 un total de 1000 veces...

  📈 Estadísticas:
  Lanzamientos : 1000
  Media        : 6.97
  Más frecuente: 7
  Mínimo real  : 2 (posible: 2)
  Máximo real  : 12 (posible: 12)

  📊 Distribución de resultados:
  ─────────────────────────────────────────────
     2 | ██                              28x   2.8%
     3 | ████                            54x   5.4%
     4 | ██████                          82x   8.2%
     5 | ████████                       112x  11.2%
     6 | ██████████                     138x  13.8%
     7 | ██████████████████████████████ 172x  17.2%
     8 | █████████████████              126x  12.6%
  ─────────────────────────────────────────────