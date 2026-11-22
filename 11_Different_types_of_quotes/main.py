"""
11 ) Different types of quotes

Mis apuntes de la clase:

Lerner dice que le preguntan bastante acerca de este tema:
¿Cual es la diferencia entre "" , '', y """ """""?

Dice que estas preguntas normalmente vienen originadas por el uso de terminales donde las diferencias entre
estas son mas importantes que en un archivo .py.
La gente que viene de programar en Ruby o Perl también realiza preguntas al respecto.

Puntos centrales

1) No hay ninguna diferencia entre comillas simples y dobles en Python.

Podemos utilizar tanto comillas simples como dobles. La elección depende de nuestras preferencias o de las convenciones del proyecto.
Para los docstrings, la convención es utilizar triples comillas dobles.


El uso combinado más común es cuando tenemos un string donde necesitamos usar una comilla interna, debe ser distinta a la
externa que engloba todo el string, caso contrario tendríanmos un SyntaxError( A menos que usemos un '\' para evitarlo).



"""
# Ejemplos de \
s = "He's up to no good"
print(s)

a = "He's up to no good"
print(a)

d = 'She says, "Hello".'
print(d)

# Lo mismo cuando necesitamos hacer un salto de linea
h = "Hello out there.\nHow are you today?"
print(h)

# Triples comillas => Muy útiles cuando tienes una cadena de texto larga, pueden ser tanto simples como dobles.
g = """
Esto es un texto
        de prueba
    Con triples comillas
"""
print(g)
