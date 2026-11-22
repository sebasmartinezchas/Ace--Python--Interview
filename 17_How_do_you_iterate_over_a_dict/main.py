"""
Apuntes de clase
A few things in this video need correcting, clarifying or updating. Times are in the video.

    2:19: d.items() returns a dict_items object; it’s an iterator, meaning each time we ask it for a new value it gives a new value
    d.items() returns a dict_items view object. It is iterable, but it is not an iterator. A for loop gets a fresh iterator from it with iter(). Calling next(d.items()) directly raises TypeError. The view reflects the dict’s current contents and can be iterated again and again.


El código funciona. Hay un comentario que contradice la propia errata que copiaste arriba.

Corrección: comentario de type(d.keys())
"El método devuelve otro dict" está mal. d.keys() devuelve un objeto view (dict_keys), no un dict: es lo mismo que la errata explica para d.items(). Una view no tiene copia propia de los datos, sino que muestra el contenido actual del diccionario. Si agregás una clave después de crearla, la view la refleja. Lo de que en Python 2 devolvía una lista es correcto (Dictionary view objects).

Precisión: comentario del primer loop
La documentación habla de orden de inserción, no de "como fueron definidas". Con un literal da lo mismo, pero si después agregás claves con d["e"] = 5, esas van al final (Mapping Types — dict).

Caso límite que vale la pena anotar
Si agregás o borrás claves mientras iterás sobre el dict o sobre una de sus views, podés recibir un RuntimeError (mismo link de las views).

Black
d={...}, las comillas simples y key,value sin espacio indican que no pasaste Black por este archivo. Si lo corrés, normaliza todo eso.

Typos y formato

"umpacking" → "unpacking".
"íncómodo" → "incómodo".
"""

# How can you iterate over a dictionary
d = {"a": 1, "b": 2, "c": 3, "d": 4}

for (
    one_item
) in (
    d
):  # Imprime las key, desde la versión 3.7 se imprimen en orden tal cual fueron definidas
    print(one_item)

# Otra forma que Lerner no recomienda por no ser necesaria. ¿ Para que invocar el metodo?
for one_item in d.keys():
    print(one_item)


print(
    type(d.keys())
)  # <class 'dict_keys'>, el metodo devuelve otro dict, en Python 2 obteniamos una lista

# Digamos que quiero imprimir tanto las keys como los values
for one_key in d:
    print(f"{one_key}: {d[one_key]}")

# Personalmente no le gusta esta forma sino la siguiente, no es una lista pero lo parece, es un iterable,cada valor que nos va dar este metodo
# por iteración se agrupará como tupla.
print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

for t in d.items():
    print(f"{t[0]}: {t[1]}")


# La forma mas usada y la preferida es hacer umpacking. Es mas simple, No tiene que salirse del loop para tomar los valores.
# Si esta adentro de una función es raro o íncómodo tener que nombrar explicitamente al diccionario sobre todo si no esta en el scope local
# sino en el global
for key, value in d.items():
    print(f"{key}:{value}")
