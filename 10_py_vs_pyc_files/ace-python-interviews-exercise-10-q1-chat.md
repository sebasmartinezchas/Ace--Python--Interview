# Difference Between .py and .pyc

_LernerPython practice transcript — 21/11/2026, 04:07:30_

## The exercise

Explain the difference between `.py` and `.pyc` files in Python — discuss with the tutor; use the editor to illustrate if you like.

## Conversation

### You

Python (CPython) compila código fuente a bytecode y lo ejecuta mediante una máquina virtual.
Los archivos .pyc son una caché del bytecode, no una condición necesaria para ejecutar Python.
La principal ventaja de .pyc es evitar recompilaciones durante las importaciones, no acelerar la ejecución del código.

### AI Tutor

¡Muy buen punto de partida! Captás la esencia correctamente — los `.pyc` son caché de bytecode y su beneficio principal está en la *importación*, no en la velocidad de ejecución del bytecode en sí.

Dos preguntas para profundizar:

1. **¿Cuándo exactamente** genera Python un `.pyc`? ¿Pasa siempre que ejecutás un script, o solo en ciertas situaciones?

2. **¿Dónde** se guardan los `.pyc` en Python 3, y cómo se llaman esos archivos?

### You

1 ) No pasa siempre, en CPython lo habitual es que se genere cuando importas un módulo por primera vez y no existe una caché valida. si hago python programa.py, se compila el códogo a bytecode y se ejecuta pero no se genera una archivo .pyc. 2) Se guardan en __pycache__ , se llaman archivo.cpython-version de python( ej 3.7 será 37).pyc

### AI Tutor

¡Exacto en ambas respuestas! Especialmente el detalle clave: `python programa.py` **no** genera `.pyc` — solo la importación lo hace. Eso es algo que mucha gente no sabe.

Una pregunta de seguimiento interesante: si ya existe un `.pyc` válido en `__pycache__/` y luego **modificás** el `.py` original, ¿qué hace Python? ¿Cómo sabe que el `.pyc` ya no es válido?

### You

por la fecha y el tamaño de las últimas modificaciones del .py

### AI Tutor

¡Correcto! Python compara el **timestamp** (fecha de última modificación) del `.py` con el que está registrado dentro del `.pyc` — si no coinciden, el `.pyc` se descarta y se recompila.

Una última pregunta para redondear el tema: si quisieras **distribuir tu código sin incluir los `.py`** (solo los `.pyc`), ¿qué limitación importante tendrías que considerar?

### You

las versiones de python  y la ubicación de los archivos

### AI Tutor

Exacto — dos limitaciones importantes:

1. **Versión de Python**: el `.pyc` incluye la versión en el nombre (`cpython-311.pyc`) y solo funciona con esa versión exacta. Si el usuario tiene Python 3.10 y vos distribuís `.pyc` compilados con 3.11, no sirven.

2. **Ubicación**: los `.pyc` viven en `__pycache__/`, que es un subdirectorio. Si reorganizás la estructura de carpetas, Python puede no encontrarlos.

Y hay una tercera limitación que vale la pena mencionar — ¿se te ocurre alguna razón por la que distribuir solo `.pyc` **no** es una buena estrategia para proteger tu código fuente?

### You

porque es posible reconstruir el código con un descompilador

### AI Tutor

¡Exactamente! Los `.pyc` se pueden descompilar con herramientas como `uncompyle6` o `decompile3` y recuperar código fuente muy similar al original. No es protección real.

---

Creo que tenés una comprensión muy sólida del tema. Para resumir lo que cubriste:

- `.py` = código fuente, `.pyc` = bytecode cacheado
- Se genera al **importar**, no al ejecutar directamente
- Se guarda en `__pycache__/` con el nombre de versión embebido
- Python valida la caché por **timestamp**
- Distribución sin `.py`: limitaciones de versión, estructura, y **seguridad prácticamente nula**

¿Hay algún aspecto que quieras profundizar — por ejemplo, cómo inspeccionar el bytecode con `dis.dis()`?

### You

no es necesario, gracias

### AI Tutor

¡Perfecto! Muy buen trabajo — dominás el tema con claridad. 👍

Revisión de Claude

Ejercicio muy bien resuelto, y esta vez acertaste en un punto donde el tutor te corrigió de más.

¿Es correcta? Sí, toda tu parte. Tres detalles:

Fecha y tamaño: acertaste vos, no el tutor. Dijiste "por la fecha y el tamaño", y el tutor lo achicó a "solo el timestamp". En el modo por defecto, the .pyc file includes the timestamp and size of the source file, which Python will compare against the metadata of the source file at runtime to determine if the .pyc file needs to be regenerated. Hay además un modo alternativo que compara un hash del contenido, pero no es el que se usa por defecto. 
googlesource

La "ubicación" al distribuir: la idea era buena, pero el tutor la explicó mal. El problema no es reorganizar carpetas. Si borrás el .py, Python ignora el .pyc que está dentro de __pycache__: If the py source file is missing, the pyc file inside pycache will be ignored. Para distribuir solo .pyc, el archivo tiene que estar in the directory where the py file would have been, i.e. not in the pycache directory, con el nombre sin la versión (modulo.pyc). 
python

Correcto: el .pyc se genera al importar y no al correr python programa.py, el nombre lleva la versión (archivo.cpython-37.pyc), y el beneficio está en la importación, no en ejecutar más rápido.

¿Qué caso límite falta? Nada importante para tus objetivos.

¿Salió fluido? Sí, sin trabas y con respuestas cortas y precisas. El editor volvió a quedar vacío. Si querés verlo con tus ojos, alcanza con crear un saludo.py, importarlo desde otro archivo y mirar qué aparece en __pycache__. Encima eso te sirve para el repaso pendiente del Ej. 7 (módulos). No lo agrego al registro.


## Your code at time of download

```python
# (optional) illustrate your answer here
```
