"""
List vs Tuples
Las listas son mutables
Las tuplas son inmutables ('locked list')
Podrían no existir ambas, de hecho muchos lenguajes de programación no tienen dos estructuras similares sino
una o la otra.

La principal diferencia es que al tener las listas muchas mas posibilidades de procesamiento
tienen muchos metodos.

Las listas y las tuplas son lo mismo en lo siguiente:
- Iterables
- Contienen algo
- Usan 'in' para buscar
- Tienen index y count como métodos
- Index y slice con []

# Lo logico es usar:
- Listas para sequencias del mismo tipo
- Tuplas para secuencias de diferentes tipos

 Listas => archivos, integers, filenames, strings
 Tuplas => structs / records

 Las listas son menos eficientes
 Las tuplas son inmutables pero pueden contener tipos de datos mutables.

 """

my_list=[10,20,30,40]
t=(10,20,30,40,50)

d={'a':1,'b':2,'c':3}
print(list(d.items()))  # [('a', 1), ('b', 2), ('c', 3)] Las listas de tuplas son muy comunes

# Las tuplas son inmutables pero pueden contener tipos de datos mutables.
t=([10,20,30],[40,50,60])
print(t[0])
t[0].append(31)
print(t)
#print(t[0]=[1,2,3])

