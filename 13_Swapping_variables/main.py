"""
13 . Swapping Variables

Apuntes de clase

Es algo que se usa poco en la practica pero se pregunta en forma habitual

"""

# x=10 and y=20 I want to swap these values. How? And Why does this work?
# En la mayoría de los lenguajes se suele hacer lo siguente:
x = 10
y = 20

temp = x
x = y  # Acá x pasa a tener el valor de y, o sea 20
y = temp  # y toma el valor que originalmente era de x y lo asignamos a la variable temporal, es decír 10

print(f"x={x} y={y}")

# En Python no es necesario hacer el procedimiento arriba descripto
a = 30
b = 40
a, b = b, a

print(f"a={a}, b={b}")

"""
**1. You can define a tuple with commas**

¿Por qué funciona `a, b = b, a`?

En realidad, están ocurriendo dos cosas diferentes:

- **Lado derecho (`b, a`):** Python evalúa primero las expresiones y construye una tupla con los valores originales de ambas variables. 
Las comas permiten crear una tupla sin necesidad de utilizar paréntesis.

- **Lado izquierdo (`a, b`):** Python desempaqueta los valores de esa tupla y los asigna a las variables correspondientes. 
Acá no estamos creando una tupla, sino indicando cómo distribuir los valores.

Como el lado derecho se evalúa antes de realizar las asignaciones, no necesitamos una variable temporal para conservar los valores originales.


2. Unpacking lets us assing from a sequence to multiple variables

La cantidad de variables deben ser igual a la cantidad de elementos a desempaquetar, caso contrario tendremos un ValueError

3 . In assignment, the right side is  evalueted first.
"""
t = (1, 2, 3)
print(type(t))  # <class 'tuple'>

t_2 = 3, 4, 5

print(type(t_2))  # <class 'tuple'>

my_list = [10, 20, 30]
x, y, z = my_list

print(f"List unpacked: x={x}, y={y}, z={z}  ")


h = len("abcd")
print(h)

h = h + 1
print(h)
h += 1
print(h)
