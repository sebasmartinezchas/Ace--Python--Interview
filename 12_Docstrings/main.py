"""
Apuntes de Clase

docstring==Documentarion string

La buena documentación (docstrings) debería cubrir tres aspectos:
1 . Expects
2 . Modifies
3 . Return

Es importante destacar que los docstrings no son lo mismo que los comentarios, apuntan a distinto publico:
 a . Comentario: a quien va a mantener la función o programa, darle soporte, mantenimiento
 b . Docstring: a quien va a usar la función o el programa. A esa persona no le interesa saber como funciona internamente o como esta
     construida, por ejemplo la documentación de una API es un buen ejemplo de un docstring.

"""

# Supongamos que quiero obtener informacíón sobre funciones o metodos nativos del lenguaje con help, lo que voy a recibir
# sera la documentación, información sobre la función o método.

print(help(len))
"""
Help on built-in function len in module builtins:                                                                                                                                             

len(obj, /)
    Return the number of items in a container.

None =>  De dond sale este none? De print
"""

print(help(str.upper))

"""
Help on method descriptor upper:                                                                                                                                                              

upper(self, /) unbound builtins.str method
    Return a copy of the string converted to uppercase.

None ?

"""


def hello(first, last=""):
    return f"Hello, {first} {last}"


print(hello("Sebas"))


print(hello("out", "there"))

print(help(hello))

"""
Help on function hello in module __main__:                                                                                                                                                    

hello(first, last='')

None

"""


def hello_two(first, last=""):
    """
    This is the the world's best function!
    It's so great, it gets a two-line docstring!
    """
    return f"Hello, {first}{last}"


print(help(hello_two))

"""
Help on function hello_two in module __main__:                                                                                                                                                

hello_two(first, last='')
    This is the the world's best function!
    It's so great, it gets a two-line docstring!

None
"""
# Si la primera linea de la función es un strings, Python la mete adentro de la función

print(
    hello_two.__doc__
)  # This is the the world's best function! It's so great, it gets a two-line docstring!


def hello_three(first, last=""):
    """
    Expects: One or two strings representing first + last names
    Modifies: Nothing
    Return: a friendly greeting using the person's name

    """
    return f"Hello, {first} {last}"


print(help(hello_three))

"""
hello_three(first, last='')
    Expects: Onne or two strings representing first + last names
    Modifies: Nothing
    Return: a friendly greeting using the person's name
"""

# También son muy usadas en las clases y los modulos


class Person:
    """
    Person Class
    Represents a person, or creature trying to
    pretend to be a person.


    """

    population = 0

    def __init__(self, name) -> None:
        """
        Initializes a new person.
        Expects: to get a string for the person's name.
        Modifies:the 'self' object
        Returns: None

        """
        self.name = name

    def greet(self):
        """Returns a friendly greeting"""
        return f"Hello, {self.name}"


print(help(Person))

""""
 |  __init__(self, name) -> None                                                                                                                                                              
 |      Initializes a new person.                                                                                                                                                             
 |      Expects: to get a string for the person's name.                                                                                                                                       
 |      Modifies:the 'self' object                                                                                                                                                            
 |      Returns: None                                                                                                                                                                         
 |                                                                                                                                                                                            
 |  greet(self)                                                                                                                                                                               
 |      Returns a friendly greeting                                                                                                                                                           
 |                                                                                                                                                                                            
 |  ----------------------------------------------------------------------                                                                                                                    
 |  Data descriptors defined here:                                                                                                                                                            
 |                                                                                                                                                                                            
 |  __dict__                                                                                                                                                                                  
 |      dictionary for instance variables                                                                                                                                                     
 |                                                                                                                                                                                            
 |  __weakref__                                   
         list of weak references to the object    
"""

# Luego de agregar population
print(help(Person))
help(Person)

"""
 Person(name) -> None
 |
 |  Person Class
 |  Represents a person, or creature trying to
 |  pretend to be a person.
 |
 |  Methods defined here:
 |
 |  __init__(self, name) -> None
 |      Initializes a new person.
 |      Expects: to get a string for the person's name.
 |      Modifies:the 'self' object
 |      Returns: None
 |
 |  greet(self)
 |      Returns a friendly greeting                                                                                                                                                           
 |                                                                                                                                                                                            
 |  ----------------------------------------------------------------------                                                                                                                    
 |  Data descriptors defined here:                                                                                                                                                            
 |                                                                                                                                                                                            
 |  __dict__                                                                                                                                                                                  
 |      dictionary for instance variables                                                                                                                                                     
 |                                                                                                                                                                                            
 |  __weakref__                                                                                                                                                                               
 |      list of weak references to the object                                                                                                                                                 
 |                                                                                                                                                                                            
 |  ----------------------------------------------------------------------                                                                                                                    
 |  Data and other attributes defined here:                                                                                                                                                   
 |                                                                                                                                                                                            
 |  population = 0       

"""
