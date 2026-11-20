"""
Ace Python Interview · Ej. 8 Q1 — array vs. lista (repaso)

Reglas:
- Antes de correr cada bloque, escribí tu PREDICCIÓN en el comentario.
- Después corré y anotá el RESULTADO. Si no coinciden, anotá POR QUÉ.
- Sin mirar la revisión anterior ni la solución de nadie.
- Requiere numpy:  pip install numpy

Corré un ejercicio a la vez (descomentá la llamada al final del archivo).
"""

import sys
from array import array

import numpy as np


# ---------------------------------------------------------------------------
# Ej. 1 — ¿array.array tiene longitud fija?
# Creá a = array('i', [1, 2, 3]).
# Aplicá, en este orden: append(4), extend([5, 6]), insert(0, 0), pop(),
# del a[1], a += array('i', [7, 8]).
# Después de cada operación imprimí len(a) y a.
# ---------------------------------------------------------------------------
# Predicción (len final y contenido final):
# Resultado:
# Por qué:
def ej1() -> None:
    ...


# ---------------------------------------------------------------------------
# Ej. 2 — Homogeneidad en array.array
# Con a = array('i', [1, 2, 3]) intentá, cada uno en su propio try/except:
#   a) a.append(3.5)
#   b) a.append('x')
#   c) a.append(2**40)
#   d) a.append(True)
# Imprimí el tipo de excepción (type(e).__name__) o el array si no falla.
# Hacé lo mismo con una lista y compará.
# ---------------------------------------------------------------------------
# Predicción (a, b, c, d):
# Resultado:
# Por qué (sobre todo c y d):
def ej2() -> None:
    ...


# ---------------------------------------------------------------------------
# Ej. 3 — Memoria: referencias vs. valores compactos
# Con n = 1_000_000:
#   lst = list(range(n))
#   arr = array('i', range(n))
# Imprimí sys.getsizeof(lst), sys.getsizeof(arr), arr.itemsize
# y arr.buffer_info()[1] * arr.itemsize.
# Pregunta extra: ¿getsizeof(lst) incluye el tamaño de los int que contiene?
# ---------------------------------------------------------------------------
# Predicción (cuál es más grande y por cuánto, aprox.):
# Resultado:
# Respuesta a la pregunta extra:
def ej3() -> None:
    ...


# ---------------------------------------------------------------------------
# Ej. 4 — numpy.ndarray: tamaño fijo y tipo fijo
# a = np.array([1, 2, 3])
#   a) b = np.append(a, 4) → imprimí a, b y (a is b)
#   b) a[0] = 3.7          → imprimí a y a.dtype
#   c) a[0] = 'hola'       → ¿qué pasa?
# ---------------------------------------------------------------------------
# Predicción (a, b, c):
# Resultado:
# Por qué (sobre todo b):
def ej4() -> None:
    ...


# ---------------------------------------------------------------------------
# Ej. 5 — Mismos operadores, distinta semántica
# Para lista, array('i', ...) y np.array, con los valores [1, 2] y [3, 4]:
#   x + y
#   x * 2
#   x + 10      (¿en cuáles funciona?)
# ---------------------------------------------------------------------------
# Predicción (tabla 3 tipos x 3 operaciones):
# Resultado:
# Por qué:
def ej5() -> None:
    ...


# ---------------------------------------------------------------------------
# Ej. 6 — Respuesta de entrevista, en blanco
# Sin mirar nada, escribí acá en 3-4 oraciones la diferencia entre
# list, array.array y numpy.ndarray. Tiene que cubrir: tipos, tamaño,
# memoria y para qué se usa cada uno en la práctica.
# ---------------------------------------------------------------------------
# Respuesta:
#


if __name__ == "__main__":
    ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
