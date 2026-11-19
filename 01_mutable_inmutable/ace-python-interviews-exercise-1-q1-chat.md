# Mutable vs. Immutable Types

_LernerPython practice transcript — 19/11/2026, 11:21:25_

## The exercise

Explain the difference between **mutable** and **immutable** types in Python — discuss with the tutor; use the editor to illustrate if you like.

In your answer, cover:
- What "mutable" and "immutable" mean
- Which built-in types fall into each category
- How mutability affects variable aliasing (two names pointing at the same object)
- Why mutability matters for things like dictionary keys

## Conversation

### You

Un tipo mutable se puede mofificar, por ejemplo un elemento de una lista o un diccionario. En cambio, un elemento inmutable como un string no es modificable, se puede guardar en otra variable pero esta variable apuntara al mismo espacio en memoria

### AI Tutor

¡Buen comienzo! Capturaste la idea central — los mutables se pueden cambiar en su lugar, los inmutables no.

Me quedo con una duda sobre la última parte: dijiste que si guardas un string en otra variable, "apuntará al mismo espacio en memoria". Eso es verdad *al principio*. Pero, ¿qué pasa después si haces algo como esto?

```python
s = "hola"
y = s
s += " mundo"
```

¿Qué crees que vale `y` al final — `"hola"` o `"hola mundo"`? ¿Y por qué?

### You

y vale "hola " igual que antes , mientras que s ahora "hola mundo". En este caso, lo que paso fue que se agregó al contenido de la variable s original ( "hola") , la palabra "mundo", es un literal, otro string. Es como decir s = s + "mundo" . Cuando hicimos y=s, le dijimos a python tanto y como s apuntan al mismo objeto, en este caso un string. No podemos modificar ese string pero si cambiar el contenido de la variable que lo contiene, en este caso la variable y

### AI Tutor

¡Casi perfecto! Entendiste lo más importante: `y` sigue valiendo `"hola"` porque `s += " mundo"` **crea un objeto nuevo** y redirige `s` hacia él — `y` sigue apuntando al objeto original.

Solo un pequeño ajuste: al final dijiste "cambiar el contenido de la variable `y`" — pero `y` no cambió en ningún momento del ejemplo. Lo que cambió fue a qué objeto **apunta `s`**. `y` sigue apuntando al mismo objeto de siempre.

Ahora la pregunta clave: ¿qué pasaría si en vez de un string usaras una **lista**?

```python
mylist = [10, 20, 30]
y = mylist
mylist[0] = 999
```

¿Qué vale `y[0]` al final — `10` o `999`? ¿Por qué sería diferente al caso del string?

### You

Si me equivoque de variables en la respuesta anterior, al final y[0] vale 999, porque la lista si se puede modificar, puedo reemplazar uno de los elementos de la lista y asignar en esa posición otro valor. En el caso del string no puedo hacerlo

### AI Tutor

¡Exacto! Y nota algo importante: `y[0]` vale `999` **sin que nadie haya tocado `y` directamente**. Solo modificamos `mylist`, pero como `y` y `mylist` apuntan al **mismo objeto**, el cambio es visible desde ambos nombres. Eso es el aliasing — y es una fuente clásica de bugs.

Ahora la última pieza: mencionaste listas y strings, pero hay otro contexto donde la mutabilidad importa mucho. ¿Podrías usar una lista como **clave de un diccionario**? Por ejemplo:

```python
d = {}
d[[1, 2, 3]] = "valor"
```

¿Qué crees que pasaría y por qué Python se comportaría así?

### You

Da un TypeError porque una lista es del tipo mutable y no se puede usar como key en un diccionario. Es "unhashable".?

### AI Tutor

¡Perfecto! Exactamente — `TypeError: unhashable type: 'list'`.

Y usaste la palabra clave: **hashable**. ¿Puedes explicar por qué Python exige que las claves sean hashables? Es decir, ¿qué problema concreto causaría permitir una lista como clave?

### You

Supongo que como la idea de un diccionario es relacionar una clave a un valor, python trata de evitar que modifiquemos esa relación, aunque si nos permite cambiar el valor en esa relación, la key en un diccionario se supone que no cambia, si el valor. Un ejemplo, para expresar la moneda estadounindense supongamos que usamos la clave "USD" que sería lo lógico, python nos permite que cambiemos cuanto vale, pero no que en determinado momento del programa la modiquemos y pase a ser "EUR"?

### AI Tutor

¡Vas por muy buen camino! La intuición es correcta — la clave no debe cambiar.

Pero vamos un nivel más profundo: ¿por qué técnicamente un diccionario se rompe si la clave cambia? 

Piénsalo así: cuando Python guarda una clave en un diccionario, calcula su **hash** (un número) para decidir en qué "cajón" guardarlo. ¿Qué pasaría si después de guardar la clave, la lista cambia y su hash cambia también? ¿Cómo encontraría Python el valor que guardaste?

### You

no tendría forma porque no encontraría el hash?

### AI Tutor

¡Exactamente! Python busca el valor usando el hash de la clave — si la clave mutó después de ser guardada, su hash cambió, y Python busca en el cajón equivocado. El valor se pierde efectivamente, aunque siga en memoria.

Por eso solo los tipos **inmutables** (cuyo hash nunca cambia) pueden ser claves: `int`, `str`, `tuple`, etc.

Hiciste un recorrido muy completo del tema. Para cerrar: ¿podrías resumir en dos o tres líneas la diferencia entre mutable e inmutable, mencionando los tres puntos — qué significa, ejemplos de cada tipo, y por qué importa para las claves de diccionario? Así consolidamos todo lo que discutimos.

### You

Mutables => List,dict y set

### AI Tutor

¡Bien! Y los inmutables — `int`, `float`, `str`, `tuple`, `bool`, `None`.

Creo que ya tienes todo el cuadro completo. ¿Quieres hacer un resumen final en tus propias palabras cubriendo los tres puntos — qué significa mutable/inmutable, ejemplos de cada uno, y por qué importa para las claves de diccionario? Así cerramos con todo consolidado.

### You

Con mis palabras sin ayuda de IA ni nada. Los mutables son tipos de datos que podemos modificar, como un elemento de una lista. Los inmutables son tipos de datos que no modificaremos, aunque podemos realizar reasignaciones. Elegimos uno u otro según la función que necesitemos que cumplan en nuestro programa y si necesitamos o queremos permitir que cambien su valor. Vale destacar que en otros lenguajes existen variables constantes, no así en python. En las claves de un diccionario python no permite un elemento mutable debido a que es un hash, como un id, si lo cambiamos desaparecería esa relación clave-valor produciendo un comportamiento no admitible para ese tipo de estructura de datos.

### AI Tutor

¡Excelente resumen, muy bien expresado y con tus propias palabras!

Una pequeña precisión: dijiste "tipos de datos que no modificaremos" — pero es más fuerte que eso. No es una decisión nuestra, es que Python **no permite** modificarlos. Si intentas hacer `s[0] = "x"` en un string, Python lanza un `TypeError`, sin importar si quieres hacerlo o no.

Todo lo demás está perfecto — especialmente la explicación del hash para las claves de diccionario, que es exactamente la razón técnica correcta. ¡Dominas el tema!


## Your code at time of download

```python
# (optional) illustrate your answer here
```
