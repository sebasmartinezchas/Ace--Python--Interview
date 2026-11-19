# What are *args and **kwargs
def hello(name):
    return f"Hello, {name}"


print(hello("a"))

# print(
#     hello("a", "b")
# )  # TypeError: hello() takes 1 positional argument but 2 were given

# *args acepta cualquier cantidad de parametros posicionales y los devuelve en una tupla. Se puede llamar
# se cualquier manera aunque la convención es *args
# Nunca podremos acceder a la tupla devuelta mediante sus índices, normalmente se accede a sus elementos mediante un loop
# Solo se puede tener un solo *args, caso contrario tendremos un error de sintaxis


def hello2(*args):
    return f"Hello {args}"


print(hello2("a"))
print(hello2("a", "b"))


# *args siempre va último, si es que tenemos otros parametros
def hello3(a, *args):
    return f"a={a}, args={args}"


print(hello3(10, 20, 30, 40))  # a=10 ,args=(20,30,40)


def hello4(a, *args, b):
    return f"a={a}, args={args}, b={b}"


# print(hello4(10,20,30,40)) TypeError missing 1 required keyboard-only argument: 'b'
# caulquier argumento luego de *args será un keyboard argument
print(hello4(10, 20, 30, 40, b=50))  # Esto es valido => a=10, args=(20,30,40),b=50

# Los argumentos posicionales siempre van antes de los keyboard arguments-
# print(hello4(10,20,30,x=100)) Esto da TypeError got an unexpected keyboard argument 'x'


# **kwargs
def hello5(a, *args, **kwargs):  # args is a tuple, kwargs is a dict!!
    return f"a={a}, args={args},kwargs ={kwargs}"


print(hello5(10, 20, 30, 40, 50))  # output a=10,args=(20,30,40,50),kwargs={}

print(
    hello5(10, 20, 30, 40, x=100, y=200, z=300)
)  # output a=10, args=(20, 30, 40),kwargs ={'x': 100, 'y': 200, 'z': 300}
