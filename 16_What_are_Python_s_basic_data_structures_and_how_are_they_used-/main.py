"""
16_What_are_Python_s_basic_data_structures_and_how_are_they_used-

Apuntes de clase
# Simple
- None
  Es la ausencia de valor, se usa, por ejemplo, cuando una función termina pero no retorna un valor,también para valores por defecto,
  para inicializar un valor pero cuando no queremos darle aún un valor específico.


  - bool
  Muy importantes para bucles, en python la mayoría de los booleanos terminan siendo True, salvo algunos puntuales como None,
  cualquier cero,cualquier tipo de estructura vacia.


  - int , float

# Sequences -- all iterable, containers, can use 'in', all subscriptable [] -- with index or slice
searching in O(n)
 - stringsLos strings son secuencias inmutables de caracteres Unicode. Python no tiene un tipo específico para caracteres individuales:
 cada carácter se representa mediante un string de longitud 1.
 - lists
 Contienen cualquier tipo de estructura de datos y son mutables

 - tuples
 Contienen cualquier tipo de estructura de datos y son inmutables

# Hash-based collections
searching in O(1) -- No importa que tan grande sea, siempre tardará lo mismo en realizar una busqueda. No es 100% cierto pero es una apreciación
del instructor que tiene un sentido practico.
 - dicts
 Hash tables, name-value pairs, key-value pairs, se usan muchisimo en cualquier situacion donde tenemos que asociar una clave a un valor.

 - sets
 Bassically the keys of a dictionary

 Corrección: bool
"La mayoría de los booleanos terminan siendo True" está mal formulado. Booleanos hay solo dos, True y False. Lo que querés decir es que la mayoría de los objetos son verdaderos cuando se evalúan en un if o en un while. Esto aplica a cualquier condición, no solo a los loops. A tu lista de valores falsos le falta el propio False. La lista oficial es: None, False, el cero de cualquier tipo numérico y las secuencias y colecciones vacías (Truth Value Testing).

Precisiones

strings: la definición oficial dice que son secuencias inmutables de code points Unicode, no de "caracteres". Lo de que no existe un tipo carácter y que indexar devuelve un string de longitud 1 está textual en la documentación (Text Sequence Type — str).
tuples: la tupla es inmutable, pero los objetos que contiene pueden no serlo. Si metés una lista adentro, podés modificar esa lista (Tuples and Sequences).
O(1): el matiz de Lerner es correcto. O(1) es el caso promedio; el peor caso es O(n). La tabla está en la wiki oficial de Python, que no está en docs.python.org (TimeComplexity).
dicts: falta el requisito que explica por qué son hash-based: las claves tienen que ser hashables. Por eso una lista no puede ser clave y una tupla sí, siempre que no contenga objetos mutables (Mapping Types — dict).
sets: la analogía "son las claves de un dict" sirve para entender que los elementos son únicos y hashables, pero se rompe en el orden. Los dicts conservan el orden de inserción desde Python 3.7; los sets no tienen orden (Set Types).

"""
