"""
Ideas centrales que  logré tomar de la clase
con palabras propias, no necesariamente estricta y oficialmente técnicas.

¿Que es __init__?¿

Lo primero que debemos decir es que el doble gion bajo es una convención que usa el lenguaje
para acceder a métodos/recursos internos y/o de funcionamiento del mismo lenguaje. Son los conocidos como "dunders", que significan
"couble underscore".

¿Pero cual es la idea de estos dunders methods?

Bien, en el mundo de la programacióm orientada a objetos, existen ciertas cosas, campos, atributos
que vamos a querer tenerlos definidos desde el principio en nuestros objetos.
En lenguajes como Java, C++ o C# esto es parte de la definicion de la clase.
Esto no existe en python, las asignaciones se realizand en tiempo real de ejecución.

En python cuando creamos una clase, se realiza a través del dunder method __new__ , este crea el objeto y llama a __init__.

Entonces si definis __init__ en tu clase será llamado, sino lo haces será llamado pero por object.__init__
Alguien definió estos métodos como callbacks.

Mucha gente llama al __init__ como el constructor pero en realidad no es correcto.



"""


class Person:
    def __init__(self, name):
        self.name = name  # Aca asignamos el valor de name a self.name


p = Person("Sebas")
print(p.name)


class MiClase:
    pass


# MiClase()
# MiClase(5)
