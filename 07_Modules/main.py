"""
Ideas centrales que  logré tomar de la clase

con palabras propias sin buscar en google ni pedir a la IA que me lo explique.

1 ) Concepto de DRY -- don't repeat yourself.

Basicamente si estas repitiendo código en distintas partes de tu programa, deberías agrupar este en
una estructura que realice ese proceso una vez y luego puedas acceder a dicho código mediante una instanciación
o un llamado ( como sería para las clases o funciones).
Esto es claro pero, ¿Que pasa cuando precisamos ese código en distintas partes del programa o incluso en otros programas?

Para atender a esa necesidad es que acudimos a librerías que importamos en nuestros programas para acceder a
algún tipo de funcionalidad.

Los modulos de Python son librerías incorporadas en el propio lenguaje, en el core.
Otra ventaja que tenemos con los modulos es que nos brinda lo que se llama "namespaces", que es un mapeo de nombres a objetos
, implementado internamente como un dict y se accede a sus metodos como atributo 'modulo.atributo'.

Ej Si tengo en mi codigo una variable "x" e importo determinados modulos, los nombres de sus metodos
pertenecen a su propio namespace global aislado y no colisionan con mis funciones/ variables.

modulo1.x !== modulo2.x!==x

Cuando importamos un modulo con la palabra import , python hace dos cosas: 1) Carga el archivo. 2) Define el nombre del modulo como variable

La importancia de los modulos es vital espcialmente en python dado que existen realmente una enorme cantidad,
es es conocido como la 'standard library'

os es "Python environment "system-specific parameters" | simplemente una interfaz estándar que te permite
interactuar con el intérprete y la máquina virtual que ya están en ejecución."
¿Qué hace realmente sys?

Expone variables y funciones internas del entorno de ejecución, como sys.path
(la lista de rutas donde Python busca los módulos cuando hacés un import),
sys.modules (el caché de módulos ya cargados en memoria) o sys.argv (los argumentos pasados por consola).

¿Por qué es distinto a otros módulos?

No tiene un archivo sys.py en el disco;
viene compilado directamente dentro del ejecutable de Python (built-in module).

"""

import os  #
import sys
import random

print(type(os))  # es un modulo del tipo class

print("os" in globals())  # output True

print(os.listdir("/"))

print(
    sys.version
)  # 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)]


print(random.randint(0, 100))

print(random.choice("abcde"))

print(sys.version)  # ok
# version is not defined
from sys import (
    version,
)  # Acá estamos deficiendo una variable global "version" con el valor de sys.version

print(
    version
)  # output 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)]

print('version' in globals()) #output True

