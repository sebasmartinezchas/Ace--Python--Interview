"""
Ideas centrales que  logré tomar de la clase

con palabras propias

Principales Puntos:
- En Python los y/o aplicaciones de usos de los arrays y las listas es similar.
- Ambos son containers de una dimensión
Pero:
    _ La longitud del array es conocida y es establecida al crearlo.
    _ Los arrays contienen un solo tipo de dato.

Si bien existen otras, esas dos serían las diferencias principales.

Te


"""

mylist=[10,20,30]
print(len(mylist)) # 3

mylist.append(40)
print(len(mylist))  # 4

mylist+=[50,60,70] # 7 => porque las listas son mutables
print(len(mylist))


x=[10,20,30]

y=x # x e y aputan al mismo objeto

x.append(40)
x.append(50)
print(y) # output [10,20,30,40,50] |  x e y son la misma lista

mylist_2=[10,'abc',len,int,str,5,'aaa']
print(
    mylist_2
)  # output [10, 'abc', <built-in function len>, <class 'int'>, <class 'str'>, 5, 'aaa']
