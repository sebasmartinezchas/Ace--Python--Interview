"""
Ideas centrales que  logré tomar de la clase

con palabras propias sin buscar en google ni pedir a la IA que me lo explique.

ES uno de los topicos mas importantes del scoping llamado en python LEGB.

"""

x = "abcde"  # Global variable, puedo acceder desde cualquier parte del programa, no esta definida adentro de una función / clase.

for i in range(5):
    y = (
        i * 10
    )  #  y / i también son variables globales,  y ese loop no genera scope, si no hay función no hay variable local

def five():
    global x  # ahora  si es global y x toma el valor local  para todo el programa ( luego de que ejecute la función)
    x=5  # Vale 5 solo dentro de la función, afuera de ella sigue siendo
#'abcde', además es otra variable, no es la misma aunque tenga el mismo nombre


five()


print(x)  # abcde

def whatever():
    a=12345

whatever()

#print(a)  # NameError name 'a' is not defined

def hello(name):  # ¿Que pasa con un parametro? Es una variable local también pero especial, recibe el valor desde el llamado de la función.
    return f'Hello, {name}'


print(hello('world'))

