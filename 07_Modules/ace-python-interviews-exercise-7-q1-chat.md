# What Are Python Modules?

_LernerPython practice transcript — 20/11/2026, 04:29:27_

## The exercise

Explain what Python modules are and why they exist. In your answer, cover:

- The problem modules solve (DRY / code organisation)
- What physically happens when you write `import os`
- The role of **namespaces** (why `os.listdir` rather than just `listdir`)
- The difference between `import os` and `from os import listdir`
- What the **standard library** is, and name at least three common modules

Discuss with the tutor; use the editor to illustrate your answer if you like.

## Conversation

### You

1) The problem modules solve (DRY / code organisation):  Concepto de DRY -- don't repeat yourself.

Basicamente si estas repitiendo código en distintas partes de tu programa, deberías agrupar este en
una estructura que realice ese proceso una vez y luego puedas acceder a dicho código mediante una instanciación
o un llamado ( como sería para las clases o funciones).
Esto es claro pero, ¿Que pasa cuando precisamos ese código en distintas partes del programa o incluso en otros programas?

Para atender a esa necesidad es que acudimos a librerías que importamos en nuestros programas para acceder a
algún tipo de funcionalidad.

Los modulos de Python son librerías incorporadas en el propio lenguaje, en el core.
2) What physically happens when you write import os: Cuando importamos un modulo con la palabra import , python hace dos cosas: 1) Carga el archivo. 2) Define el nombre del modulo como variable 3. ) The role of namespaces (why os.listdir rather than just listdir?
Otra ventaja que tenemos con los modulos es que nos brinda lo que se llama "namespaces", que es un mapeo de nombres a objetos
, implementado internamente como un dict y se accede a sus metodos como atributo 'modulo.atributo'.

Ej Si tengo en mi codigo una variable "x" e importo determinados modulos, los nombres de sus metodos
pertenecen a su propio namespace global aislado y no colisionan con mis funciones/ variables.

modulo1.x !== modulo2.x!==x 4) The difference between import os and from os import listdir , el segundo caso es el correcto dado que estamos definiendo una variable global "listdir" con el valor de os.listdir 5) What the standard library is, and name at least three common modules :
La importancia de los modulos es vital espcialmente en python dado que existen realmente una enorme cantidad,
es es conocido como la 'standard library' y hay para muchos propositos distintos, nombremos cuatro en lugar de tres para documentar un ejemplo según las categorías mas comúnes => Tests: unittest | Utilidades: math| Datos y/ formatos:json | Sistema de archivos: sys


### AI Tutor

¡Muy buena respuesta general! Cubriste los puntos principales con claridad. Quiero profundizar en dos cosas:

**Sobre el punto 4 — ¿cuál es el "correcto"?**

Dijiste que `from os import listdir` es "el correcto". Pero `import os` también es perfectamente válido — no es incorrecto. La pregunta más interesante es: ¿cuándo preferirías uno sobre el otro? Pensá en esto: si usás `from os import listdir`, ¿qué pasa si ya tenés en tu código una función propia llamada `listdir`?

**Sobre el punto 2 — las dos cosas que hace `import`**

Mencionaste "carga el archivo" y "define el nombre como variable". Exacto. ¿Podés ser más preciso sobre la segunda parte? Cuando Python "define el nombre `os` como variable", ¿en qué namespace queda esa variable? ¿Y de qué tipo es el objeto al que apunta?

### You

valoro tu correción sobre el punto 4, son correcta las dos formas. Te cuento lo que me paso :al ver la pregunta pensé en el ejemplo cuando Reuven ejecuta version cuando lo correcto era sys.version y luego explica que para ejecutar directamente 'version' debiamos hacer => from sys import version, en este caso estamos definiendo una variable global que se llama version con el valor de sys.version. ¿ cuando prefiero uno u otro? En la practica preferiría importar el modulo completo, sería la opción por defecto y evita colisiones de nombres, es mas limpio. La segunda opción  de importar la variable listdir podría ser válida si se va a usar muchas veces y/o cuando el nombre es explicativo. Si ya tengo una función listdir y uso from os import listdir se van a pisar y el valor resultante de la misma será el último que se ejecute de arriba hacia abajo. Sobre el punto 2 lo define como variable global . ¿De que tipo es el objeto? Es un modulo, un print de type te dice class, pero a no engañarse porque en Python todo es un objeto => 5 es un objeto cuya clase es int | 'hola' es un objeto cuya clase es str | os es un objeto cuya clase es module

### AI Tutor

¡Perfecto! Razonaste exactamente bien en todos los puntos — especialmente el detalle sobre las colisiones: el último `import` gana, de arriba hacia abajo.

Y la observación sobre `type(os)` es exactamente la respuesta que buscaba: `<class 'module'>`. Todo es un objeto en Python — incluidos los módulos mismos.

Una sola pregunta para cerrar el tema del namespace y asegurarnos de que el modelo mental es sólido:

Cuando hacés `import os`, Python ejecuta el archivo `os.py` y crea ese objeto de tipo `module`. Ese objeto tiene su propio namespace interno. ¿Cómo accede Python a ese namespace cuando escribís `os.listdir`? Es decir, ¿qué mecanismo está usando el punto (`.`) ahí?

### You

es el operador de acceso a atributos

### AI Tutor

Exacto. Y eso conecta directamente con algo que mencionaste antes: "en Python todo es un objeto".

El módulo `os` es un objeto, y `listdir` es un **atributo** de ese objeto — igual que `nombre` podría ser un atributo de cualquier instancia de una clase tuya.

Con eso, cubriste los cinco puntos de la pregunta de forma sólida. Si tuvieras que resumir en una sola oración *por qué* existen los módulos — no el mecanismo, sino el propósito — ¿cómo lo dirías?

### You

para facilitar tareas, aportar utilidades, manejar archivos, para muchas cosas existen los modulos y uno mismo puede crear sus propios modulos para aislar determinadas funcionalidades e importarlos en otra parte del programa o en otro programa. Lo que se llama o se conoce normalmente como librería en cualquier lenguaje de programación es un modulo

### AI Tutor

Muy bien resumido. Y el punto sobre crear tus propios módulos es importante — no solo los de la standard library, sino cualquier archivo `.py` que vos mismo escribas puede ser importado como módulo.

Una pequeña precisión para afinar el modelo mental: mencionás que "lo que se conoce como librería es un módulo". Eso es mayormente cierto, pero ¿notás alguna diferencia entre la **standard library** (que es una *colección* de módulos) y un módulo individual como `os` o `math`? ¿Cómo llamarías a esa distinción?

### You

os y math son parte de la standard library, podrías reformular la pregunta? No llegó a comprender que necesitas que fije en mi modelo mental...

### AI Tutor

Tenés razón, me expresé mal. Reformulo:

Dijiste "lo que se conoce como librería es un módulo". Pero la **standard library** no es un solo módulo — es una colección enorme de módulos. Entonces, ¿cuál sería la unidad básica: el módulo individual (`os`, `math`, `json`) o la colección entera ("standard library")?

Es solo una distinción de vocabulario — quiero asegurarme de que cuando decís "librería" y "módulo" los estás usando como conceptos distintos.

### You

ah, la librería son todos, el conjunto os es un modulo, ahora veo adonde apuntabas

### AI Tutor

Exacto. La distinción es:

- **Módulo**: un archivo individual (`os.py`, `math.py`)
- **Standard library**: el conjunto completo de módulos que vienen con Python

Con eso, tu modelo mental está completo. Respondiste los cinco puntos de la pregunta de forma sólida — namespaces, el operador de atributos, colisiones de nombres, `type(os)`, y ahora la distinción librería/módulo. ¡Bien hecho!

### You

genial que te parece si mi planteamos algún ejercicio para practicar este concepto? Se puede hacer?

### AI Tutor

¡Me alegra el entusiasmo! Pero mi rol acá es ayudarte con los ejercicios del curso — no puedo generar ejercicios nuevos fuera de los que están definidos.

Lo que sí podés hacer: avanzar al siguiente ejercicio del curso, donde seguramente vas a aplicar estos conceptos de forma práctica. ¿Querés seguir con el próximo?

### You

excelente, gracias, veo de armar algo por mi cuenta para practicar y nos vemos en chat de la próxima clase

### AI Tutor

¡Perfecto! Practicar por tu cuenta es exactamente la actitud correcta. Nos vemos en la próxima. 🙌


## Your code at time of download

Revisión breve de claude

¿Es correcta? En lo central sí. Lo mejor de la sesión fue que razonaste solo las colisiones de nombres y lo de type(os). Hay cuatro cosas que el tutor dejó pasar:

sys no es el módulo del sistema de archivos. Es el error más concreto. sys da acceso a variables y funciones del intérprete, como sys.version, sys.argv o sys.path (sys). Los archivos y directorios se manejan con os, pathlib o shutil.
El mecanismo de import quedó incompleto. Dijiste “carga el archivo y define el nombre”. Faltan dos pasos, y son los que pedía la palabra “físicamente”:
Python primero busca el módulo. Antes de ir a disco, se fija si ya está cargado en sys.modules. Si está, no lo vuelve a ejecutar y reutiliza el mismo objeto (sys.modules, The import system). Esto es lo que habrías visto con el experimento del print importado dos veces.
El nombre no queda siempre como global: se liga en el namespace actual. Si hacés el import dentro de una función, queda local (The import statement).
“Métodos” no es la palabra. os.listdir es una función que es atributo de un objeto módulo. Los métodos son funciones definidas en una clase. Es el mismo tipo de imprecisión que “devuelve” en la Q3: la idea es correcta y el término no. Lo que sí estuvo bien es decir que el namespace de un módulo es un dict: existe y lo podés ver con os.__dict__ (Data model: modules).
!== no existe en Python. Eso viene de JavaScript. En Python la comparación por valor es != y la de identidad es is not.

Un error del tutor: puso math.py como ejemplo de módulo, pero math está escrito en C y no es un .py. Probá print(os.__file__) y print(math.__file__) y comparalos. Además, la jerarquía tiene un nivel más que no apareció en la charla: entre el módulo y la biblioteca está el paquete, que es un módulo que contiene submódulos (Glosario: package).

¿Es idiomático? El editor quedó vacío otra vez, así que no hay código para revisar.

¿Fluido o te trabaste? Fluido en el razonamiento. Te trabaste en vocabulario (método vs. función, biblioteca vs. módulo) y en el mecanismo. Pediste un ejercicio, que estuvo muy bien, y el tutor se negó. Eso ya nos dice que el ejercicio de fijación lo tenemos que poner nosotros.

Ejercicio de fijación

Es el que te propuse antes de la clase, y ahora lo hacés solo:

Creá saludo.py con una función y un print("cargando saludo") suelto arriba de todo. Desde otro archivo, importalo dos veces. Antes de correrlo, escribí qué esperás ver.
En un archivo, hacé import os y print(dir()). En otro, hacé from os import listdir y lo mismo. Explicá la diferencia en una línea.

```python
# (optional) illustrate your answer here
```
