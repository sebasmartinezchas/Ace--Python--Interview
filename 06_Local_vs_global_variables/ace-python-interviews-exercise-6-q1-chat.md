# Local vs. Global Variables

_LernerPython practice transcript — 19/11/2026, 06:08:06_

## The exercise

Explain the difference between local and global variables in Python. Cover:
- How Python decides whether a variable is local or global inside a function
- What happens when a function assigns to a name that also exists in the global scope
- How the `global` keyword changes that behaviour
- The **LEGB** rule (Local → Enclosing → Global → Built-in) for name lookup

Discuss with the tutor; use the editor to illustrate your answer if you like.

## Conversation

### You

Haré referencia a otro lenguaje porque creo que enriquece la conversación. Una variable definida afuera de una función tiene alcance global. Pasa en otros lenguajes como JS que algunas estructuras como un loop crean un scope para variables declaradas con const y let ( hoy sería siempre dado que var ya no se usa). En Python eso no pasa, si no hay función no hay variable local.  x = "abcde"  # Global variable, puedo acceder desde cualquier parte del programa, no esta definida adentro de una función / clase.

for i in range(5):
    y = (
        i * 10
    )  #  y / i también son variables globales,  y ese loop no genera scope, si no hay función no hay variable local

def five():
    global x  # ahora  si es global y x toma el valor local  para todo el programa ( luego de que ejecute la función)
    x=5  # Vale 5 solo dentro de la función, afuera de ella sigue siendo
#'abcde', además es otra variable, no es la misma aunque tenga el mismo nombre  five()


print(x)  # abcde . No vale 5 afuera de la función, la única excepción es que declaremos especialmente que será una variable global con la palabra reservada "global" Creo que con esto están respondidas las 3 primeras preguntas. Es interesante tambien ver ¿Que pasa con un parametro? Es una variable local también pero especial, recibe el valor desde el llamado de la función (invoke.) LA regla LEGB son los 4 scopes, que veremos mas adelante, local o sea adentro de una función. La E es de enclosing, en el caso de python, y aquí toma valor la referencia que hice a otros lenguajes, sería solo para una funcion adentro de otra (closure) , Global es el ambito principal del programa, desde donde se tiene acceso de cualquier lugar.  La B corresponde a los Built-in del lenguaje como pirnt, len.

### AI Tutor

¡Muy buena respuesta! Tienes los conceptos centrales bien claros. Me gusta especialmente la comparación con JS — es exactamente el tipo de contraste que ayuda a entender por qué Python sorprende a los que vienen de otros lenguajes.

Pero fijate en algo: en tu explicación del `global` hay una contradicción interesante. Escribiste dos cosas:

1. `global x` hace que `x = 5` tome efecto en todo el programa
2. "Vale 5 solo dentro de la función, afuera de ella sigue siendo `'abcde'`"

Ambas no pueden ser ciertas al mismo tiempo. ¿Cuál de las dos es la correcta cuando *sí* usás `global x`?

### You

son dos anotaciones distintas, es cierto que  quizas a otro lo confunda, cuando vimos al final de la clase la palabra reservada global y se asigno en la línea siguiente ahí paso a valer x = 5, aunque si python funciona como otros lenguajes ese valor lo tomaría luego de que la función es invocada

### AI Tutor

Exacto, eso es correcto. `global x` hace que la asignación `x = 5` modifique la variable global — pero ese cambio ocurre en el momento en que la función es *invocada*, no cuando es definida.

Entonces después de llamar `five()`, ¿qué imprimiría `print(x)`? ¿`'abcde'` o `5`?

### You

5

### AI Tutor

¡Correcto! Después de invocar `five()`, `x` vale `5` globalmente.

Ahora la pregunta más interesante: ¿qué pasaría si *no* hubieras escrito `global x` dentro de `five()`, pero igualmente hicieras `x = 5` y luego llamaras `five()`? ¿Qué imprimiría `print(x)` en ese caso?

### You

'abcde'

### AI Tutor

¡Perfecto! Sin `global x`, Python crea una variable *local* `x` dentro de `five()`, completamente separada de la global. La global `'abcde'` queda intacta.

Ahora, hay un caso sutil que suele sorprender. ¿Qué crees que pasaría con este código?

```python
x = 'abcde'

def five():
    print(x)  # intenta leer x ANTES de asignarla
    x = 5
```

¿Imprimiría `'abcde'`, `5`, o algo completamente diferente?

### You

ahí no imprime nada porque no ejecutas la función, decime si lo vas a hacer y entonces te respondo

### AI Tutor

¡Buena observación! Sí, imaginá que la llamás:

```python
x = 'abcde'

def five():
    print(x)
    x = 5

five()
```

¿Qué creés que pasa?

### You

da un error  UnboundLocalError  porque no podemos mandar a imprimir algo que no existe en ese ambito (local) , en otros lenguajes como javascript existe el hoisting y te imprimiría 'abcde'

### AI Tutor

¡Exactamente! Y tu explicación del *por qué* es muy precisa: en el momento en que Python ve `x = 5` en cualquier parte del cuerpo de la función, decide que `x` es local para **toda** la función — incluso las líneas anteriores a la asignación. Entonces el `print(x)` intenta leer una variable local que todavía no tiene valor. `UnboundLocalError`.

La comparación con hoisting de JS es muy buena. Python no hace eso — la decisión de si una variable es local o global se toma en tiempo de compilación, no de ejecución.

Con esto tenés cubiertos los cuatro puntos de la pregunta. Solo te pregunto: en la regla LEGB, ¿en qué orden exacto busca Python? ¿Y qué pasa si encuentra el nombre en el primer scope — sigue buscando en los demás?

### You

 1. Local (L) → 2. Enclosing (E) → 3. Global (G) → 4. Built-in (B), se detiene en cuanto hace match, no sigue buscando

### AI Tutor

¡Perfecto! Orden correcto y la regla de "se detiene al primer match" es exactamente así.

Una última pregunta para cerrar: si definís una función llamada `len` dentro de tu código, ¿qué le pasa al `len` built-in de Python? ¿Podés seguir usándolo?

### You

sin hacer nada va a llamar a la función propia, tendrías que importar builtints y llamar a len como método de el, vale decir que usar como nombre de función la misma palabra que un método en python esta considerada una mala practica (shadowing)

### AI Tutor

¡Exacto! Eso es *shadowing* — tu `len` local "tapa" al built-in en ese scope, y Python lo encuentra primero en L o G antes de llegar a B. Para recuperar el built-in tendrías que usar `__builtins__` o el módulo `builtins`.

Y sí, es una muy mala práctica — no solo con `len`, sino con cualquier built-in: `list`, `dict`, `input`, `print`...

Diría que has cubierto todos los puntos de la pregunta de manera sólida: la diferencia local/global, el comportamiento de la asignación dentro de funciones, `global`, el `UnboundLocalError`, y LEGB completo. ¿Querés profundizar en algún punto, o pasamos a otra pregunta?

### You

pasamos, nos vemos en la pròxima clase, gracias

### AI Tutor

¡Hasta la próxima! Fue una muy buena conversación — se nota que tenés una base sólida y que pensar en otros lenguajes te ayuda a entender Python más profundo. 👋


## Your code at time of download

Revisión del ejercicio por claude

• ¿Es correcta? ¿Qué caso límite falta?

Tu razonamiento es correcto y cubriste los cuatro puntos con ejemplos claros.

Casos límite y precisiones técnicas para sumar a tu Markdown:
	1. Tiempo de compilación vs. ejecución: El detalle clave que preguntó la consigna ("Cómo decide Python si es local o global") ocurre en tiempo de compilación (cuando Python lee la definición def). Si existe cualquier asignación (=) a ese nombre en el cuerpo de la función, Python lo marca como local para toda la función (salvo que declaremos global o nonlocal).
	2. Mutación vs. Reasignación: Si x es una lista global (x = [1, 2]), hacer x.append(3) dentro de una función no requiere la palabra clave global y modifica la lista original. Esto pasa porque no estás reasignando el nombre x, solo estás mutando el objeto al que apunta.
	3. Comprehensions (excepción al "si no hay función no hay scope"): Aunque los bucles for tradicionales no crean scope propio, en Python 3 las list/dict/set comprehensions y generator expressions sí crean su propio scope local para la variable de iteración ([i for i in range(5)] no deja la variable i dando vueltas en el scope global).

• ¿Es Python idiomático? Una mejora concreta

Tus respuestas fueron precisas y manejaste bien el vocabulario técnico (shadowing, UnboundLocalError, builtins).
Mejora concreta: Al mencionar el módulo builtins, ojo con el tipeo (builtints en tu chat, el nombre real es builtins, sin la segunda "t"). Además, para la palabra clave nonlocal (que actúa sobre el scope Enclosing de LEGB), recordá que funciona igual que global, pero en lugar de apuntar al módulo principal, apunta a la función contenedora más cercana.

• ¿Salió fluido o te trabaste? ¿En qué?
Salió muy fluido. Solo hubo una pequeña superposición en tu primer bloque de código al mezclar el comentario de un ejemplo sin global con el código que sí tenía global x, pero lo aclaraste enseguida cuando el tutor te lo marcó.


```python
# (optional) illustrate your answer here
```
