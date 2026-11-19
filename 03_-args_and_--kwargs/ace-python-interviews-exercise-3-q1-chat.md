# Explain *args and **kwargs

_LernerPython practice transcript — 19/11/2026, 02:08:05_

## The exercise

Explain what `*args` and `**kwargs` are in Python function definitions — discuss with the tutor; use the editor to illustrate if you like.

Cover:
- What types do `args` and `kwargs` take on inside the function?
- How do positional-only, `*args`, keyword-only, and `**kwargs` parameters interact?
- When would you actually reach for each one?

## Conversation

### You

1) args toma todos los argumentos posicionales cualquiera sea su cantidad y los devuelve en una tupla, mientras que kwargs toma todos los argumentos por palabra clave. 2) Si tengo un argumento posicional ej (b,*args,**kwargs), estos van a interactuar de la siguiente manera: el primer argumento será b, el o siguientes que no sean enviados por palabra clave serán recibidos por args y devueltos en una tupla. Los que sea enviados por palabra clave serán recibidos por kwargs y devueltos como un dicccionario. 3) Recurriría a ellos siempre que no sepa que tipo y cantidad de argumentos me van a enviar, para poder recibirlos y evaluar el tratamiento de la data recibida.

### AI Tutor

¡Muy buena base! Tienes los conceptos centrales bien claros. Quiero explorar un par de puntos más finos:

Sobre el punto 2: dijiste que `*args` recibe los que "no sean enviados por palabra clave". Eso es correcto. Pero ahora piensa en esto: ¿qué pasa con los parámetros que declares *después* de `*args`? Por ejemplo:

```python
def f(b, *args, c):
    ...
```

¿Cómo tendrías que pasar `c` al llamar esta función? ¿Podrías pasarlo como argumento posicional?

### You

no se puede, me da un TypeError, luego de args no puede haber mas argumentos posicionales

### AI Tutor

¡Exacto! Pero hay un matiz importante: no es que no pueda haber más parámetros después de `*args` — sí puede haberlos. Lo que no pueden es ser pasados *posicionalmente*.

¿Cómo se llaman los parámetros que sólo pueden recibirse por nombre (como `c` en ese ejemplo)? ¿Conoces el término técnico?

### You

yo dije que luego de args no puede haber mas argumentos posicionales, nunca dije que no pudieran existir mas argumentos. Los argumentos que solo pueden llamarse por nombre son "keyboard arguments"

### AI Tutor

¡Tienes razón, me adelanté! Leí mal lo que escribiste — la distinción que hiciste es correcta.

Y casi: el término es **keyword-only arguments** (argumentos sólo por palabra clave). Un detalle de nomenclatura, nada más.

Ahora, una pregunta para ir más profundo: mencionaste en el punto 3 que usarías `*args` y `**kwargs` "cuando no sepas qué argumentos te van a enviar". Eso es válido, pero en la práctica hay casos de uso más específicos y comunes. ¿Se te ocurre algún ejemplo concreto de código donde `*args` o `**kwargs` sean casi *indispensables* — algo que sería muy difícil de escribir sin ellos?

### You

se me ocurre por ejemplo cuando quiero que los argumentos que me pasen no sean mutables los recibiría con *args para que se transformen en una tupla

### AI Tutor

Interesante idea, pero hay un problema con ese razonamiento: `*args` no *convierte* los argumentos en inmutables — si alguien te pasa una lista, esa lista sigue siendo mutable dentro de la tupla. La tupla solo significa que no puedes *agregar ni quitar* elementos de `args` en sí, pero los objetos que contiene conservan su naturaleza original.

El caso de uso clásico e indispensable para `*args` es otro: piensa en **decoradores** o en funciones que *envuelven* a otras funciones. Si quieres escribir un wrapper que llame a cualquier función sin saber de antemano cuántos argumentos acepta, ¿cómo lo harías sin `*args` y `**kwargs`?

### You

si, me imagino que es un uso clasico, dado que los decoradores son muy útiles para trabajar sobre funciones sin moficarlas pero respecto a mi respuesta anterior, creo que exprese mal la idea de mutabilidad, y tenes razón en marcarlo. Sin ir a temas un poco mas de python intermedio como decoradores para un nivel inicial me parece que lo mas útil es pensar que con args recibo cualquier cantidad de argumentos posicionales, no conozco la cantidad de antemano pero no quiero que sea un problema

### AI Tutor

¡Perfecto, esa es exactamente la idea central y está bien expresada!

Una última pregunta para cerrar el tema: mencionaste al principio que `*args` "devuelve" una tupla. ¿Qué palabra usarías en lugar de "devuelve" para ser más preciso sobre lo que hace `*args` con esos argumentos?

### You

retorna

### AI Tutor

Casi — "retornar" en Python está muy asociado a `return`, es decir, al valor que una función le da de vuelta a quien la llamó.

Lo que hace `*args` es *recolectar* o *agrupar* esos argumentos en una tupla. ¿Ves la diferencia? `return` es una salida de la función; lo que hace `*args` ocurre en la *entrada*, cuando Python recibe los argumentos.

Con eso en mente, ¿cómo reformularías tu definición original del punto 1?

### You

recibe todos los argumentos posicionales, sean la cantidad que sean y los agrupa en una estructura de  datos del tipo tupla, no retorna, agrupa, convierte

### AI Tutor

¡Exacto! "Agrupa" es la palabra correcta. 

Solo un pequeño matiz: no los *convierte* en tupla — simplemente los *colecta* en una tupla desde el principio. No hay transformación, Python los empaqueta directamente.

Con eso, tienes una comprensión sólida de `*args` y `**kwargs`. Para resumir lo que cubriste bien:
- `*args` agrupa argumentos posicionales extras en una **tupla**
- `**kwargs` agrupa argumentos por palabra clave extras en un **diccionario**
- Los parámetros después de `*args` son **keyword-only**
- El nombre `args`/`kwargs` es convención — la magia está en el `*` y `**`

¿Hay algún punto que quieras profundizar más, o algo que todavía te genere dudas?

### You

no, esta bien, con lo de agrupa me queda claro, vale lo mismo para el dicccionario, correcto?

### AI Tutor

¡Sí, exactamente! `**kwargs` también *agrupa* — colecta los argumentos por palabra clave extras directamente en un diccionario, sin conversión.

¡Muy buen trabajo! Tienes una comprensión clara y precisa de ambos. 🎉


## Your code at time of download

```python
# (optional) illustrate your answer here
```
