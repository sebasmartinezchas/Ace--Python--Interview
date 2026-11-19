# Mutable vs Inmutables types
# mutable ==can mutate / change
s='abcde'
print(s[0])
print(s[2])

# print([0])="!"
# SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?

y=s
print(y)
# Ambos apuntan al mismo espacio en memoria
s+='f'
# => abcdef
# Es lo mismo que decir
s=s+"f"
print(s)
# => abcdeff

# Mutable
mylist=[10,20,30,40,50]
#mylist:list[[0]]= "!"
print(mylist)

mylist=[10,20,30,40,50]
y=mylist
#mylist[0]='???'
print(mylist,y)

"""
Nota sobre mensaje de pylance => No overloads for "__setitem__" match the provided argument
Qué pasa:

mylist[0] = '???' no es magia. Python lo convierte en la llamada mylist.__setitem__(0, '???'). Ese es el método especial que se ejecuta al asignar con corchetes (Data model – __setitem__).
Pylance usa Pyright por debajo. Cuando ve [10, 20, 30, 40, 50] deduce que el tipo es list[int] (Pyright – Type inference, sección de list expressions).
En los stubs de tipos (typeshed), list.__setitem__ tiene dos overloads, es decir, dos firmas posibles:
(índice, int) para asignar un elemento.
(slice, Iterable[int]) para asignar una porción.

'???' es str, así que no encaja en ninguna de las dos. De ahí el mensaje “no overloads match” (typing – @overload).
"""

"""
-----Inmutable------
None
bool
float
int
str
tuple
------
-----Mutable------
list
dict
set

"""
d={}
d[mylist]=100
# TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
"""
Explain the difference between **mutable** and **immutable** types in Python — discuss with the tutor; use the editor to illustrate if you like.

In your answer, cover:
- What "mutable" and "immutable" mean
- Which built-in types fall into each category
- How mutability affects variable aliasing (two names pointing at the same object)
- Why mutability matters for things like dictionary keys
"""

s="hola"
y=s
s+=" mundo"

print(y,s)

mylist=[10,20,30]
y=mylist
mylist[0]=999
print(mylist)


d={}
d[[1,2,3]]="Valor"
print(d)
