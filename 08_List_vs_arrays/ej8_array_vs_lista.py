"""
Ace Python Interview · Ej. 8 Q1 — array vs. lista (repaso corto)

Antes de correr, escribí tu predicción en el comentario.
"""

from array import array

# ---------------------------------------------------------------------------
# Ej. 1 — ¿array.array tiene longitud fija?
# Creá a = array('i', [1, 2, 3]).
# Hacé a.append(4) y después a.pop().
# Imprimí len(a) después de cada paso.
# ---------------------------------------------------------------------------
# Predicción: append agrega 4 y queda ['i],[1,2,3],4] y pop quita este último así que queda el último print como el array original
# Resultado: Mala intuición: append agrega 4 a la lista y y no como tercer elemento. Acerté con pop. 50% y 50%

a = array("i", [1, 2, 3])
a.append(4)
print(f"Luego de append: {a}")
a.pop()
print(f"Luego de pop: {a}")
print(a)
print(type(a))
# ---------------------------------------------------------------------------
# Ej. 2 — Un solo tipo
# Con el mismo array, intentá a.append('hola') y a la vez con una lista.
# ¿Qué pasa en cada caso? Da error, a los dos, tanto al string como a la lista no los puede interpretar como int que parece que es lo que espera, datos numericos.
# ---------------------------------------------------------------------------
# Predicción:
# Resultado:
# a.append("Hola")
# a.append([1,2,3])
print(a)

# ---------------------------------------------------------------------------
# Ej. 3 — Resumen en una oración
# ¿Cuál es la diferencia real entre una lista y un array.array?

# ---------------------------------------------------------------------------
# Respuesta:
# Una lista es un contenedor flexible y de proposito general, acepta cualquier tipo de datos, almacena "referencias a objetos", no directmaente sus
# valores. Más flexibilidad pero más costo de memoria.
# array.array almacena secuencias de valores numericos de un tipo determinado, en el ejemplo anterior 'i' indica que los
# elementos son enterior del tipo int de C.
# Almacena los valores directamente en un bloque contiguo de memoria, utilizando una representación binmaria de tamaño fijo. No
# Necesita mantener una referencia a un objeto de Python independiente por cada elemento seleccionado, esto permite ahorro de memoria.#
