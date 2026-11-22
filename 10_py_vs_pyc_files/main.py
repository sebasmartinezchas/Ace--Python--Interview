"""

# 10. Archivos .py vs. .pyc

**Ideas centrales que logré tomar de la clase.**

Apuntes con palabras propias, no necesariamente con terminología estrictamente técnica.

## ¿Cuál es la diferencia entre los archivos .py y los .pyc?

Para responder esta pregunta tenemos que dar un paso hacia atrás.

### Lenguajes compilados e interpretados

Existen dos grandes formas de ejecutar programas (haciendo una generalización muy simple):

1. Mediante compilación.
2. Mediante interpretación.

En realidad, no son dos categorías rígidas de lenguajes, sino diferentes estrategias de implementación y ejecución. Incluso pueden combinarse.

Salvo excepciones de programadores que trabajan con lenguajes de muy bajo nivel, normalmente escribimos código en un lenguaje de alto nivel.

Ese código necesita transformarse o procesarse de alguna manera para que finalmente el procesador pueda ejecutar instrucciones de máquina.

**Compilación**

Un compilador traduce código de un lenguaje a otro. En muchos lenguajes tradicionales, como C, el proceso permite generar código máquina que luego puede ejecutarse sin necesidad de volver a compilar cada vez.

El compilador no ejecuta el programa: transforma el código. La ejecución es otro proceso.

La compilación puede ser muy compleja. Es útil como ejemplo el de las películas traducidas: entre el material original y el resultado final pueden existir muchas transformaciones.

En el caso de los compiladores, estas transformaciones pueden incluir optimizaciones, reorganización de instrucciones y otras operaciones.

Esto puede complicar la depuración de ciertos problemas, porque la correspondencia entre el código fuente y las instrucciones ejecutadas no siempre es directa.

Sin embargo, existen herramientas de depuración que permiten trabajar con programas compilados.

Una característica de la compilación anticipada es que, si modificamos el código fuente, normalmente necesitamos volver a compilarlo para incorporar los cambios al ejecutable.

Los compiladores pueden realizar numerosas optimizaciones, tanto de velocidad como de utilización de memoria. Esta es una de las razones por las que los programas compilados directamente a código máquina suelen ofrecer un rendimiento elevado.

**Interpretación**

Aquí entra el concepto de intérprete.

En términos generales, un intérprete ejecuta instrucciones de un programa durante su funcionamiento.

A diferencia de la compilación anticipada a código máquina, no necesita generar previamente un ejecutable nativo completo.

Una aclaración importante: interpretar no significa necesariamente traducir el código fuente línea por línea a código máquina.

Un intérprete puede trabajar sobre representaciones intermedias del programa.

En muchos casos, la interpretación implica un trabajo adicional durante la ejecución, lo que puede afectar el rendimiento.

Sin embargo, no podemos afirmar que todos los lenguajes compilados sean más rápidos o más difíciles de utilizar que los interpretados.

La velocidad depende de muchos factores: implementación, optimizaciones, algoritmos, estructuras de datos, etc.

### Una tercera posibilidad: compilación a bytecode

Aquí aparece una combinación interesante de ambas estrategias.

El código fuente primero se compila a una representación intermedia llamada **bytecode**.

El bytecode es un conjunto de instrucciones de menor nivel que el código fuente, diseñado para ser ejecutado por una máquina virtual.

No es código máquina nativo.

Este enfoque permite separar la compilación del código fuente de su ejecución.

Algunos ejemplos conocidos son Java, C# (.NET) y Python, aunque sus implementaciones y mecanismos de ejecución tienen diferencias importantes.

### ¿Cómo funciona Python?

En este caso estamos hablando específicamente de **CPython**, la implementación más utilizada de Python.

El proceso general es:

**Código fuente (.py) → Compilación → Bytecode → Máquina virtual de CPython → Ejecución**

Cuando ejecutamos un programa, CPython necesita convertir el código fuente a bytecode.

Luego, su máquina virtual ejecuta las instrucciones correspondientes.

Una característica importante es que Python no necesita guardar ese bytecode en un archivo para poder ejecutarlo.

Puede compilarlo y utilizarlo directamente en memoria.

El compilador de CPython realiza algunas optimizaciones, pero no intenta transformar nuestro código en una versión completamente optimizada.

Por lo tanto, si escribimos un algoritmo ineficiente, no debemos esperar que Python solucione automáticamente ese problema.

Las versiones modernas de CPython también incorporan mecanismos de optimización durante la ejecución.

---

## ¿Qué son los archivos .pyc?

Los archivos `.pyc` contienen bytecode compilado de Python.

La extensión puede interpretarse como *Python compiled*.

Su finalidad principal es **evitar tener que volver a compilar determinados módulos cada vez que se importan**.

Por ejemplo:

Tenemos un programa que importa un módulo.

Cuando Python importa ese módulo, comprueba si existe una versión de bytecode previamente compilada y válida.

Si no existe, compila el módulo y normalmente guarda el resultado en un archivo `.pyc`.

La próxima vez que importemos ese módulo, Python podrá reutilizar el bytecode almacenado y evitar repetir la compilación.

Esto mejora el tiempo necesario para importar módulos.

**Importante:** utilizar un `.pyc` no significa que el código se ejecute más rápido. La ventaja consiste en ahorrar el trabajo de compilación.

### ¿Cuándo genera Python un archivo .pyc?

No siempre se genera un archivo `.pyc`.

Por ejemplo, cuando ejecutamos directamente:

`python main.py`

Python compila el código de `main.py` a bytecode y lo ejecuta, pero normalmente no genera un archivo `.pyc` para ese script principal.

En cambio, si `main.py` importa otro módulo:

`import calculos`

Python normalmente generará un archivo `.pyc` para `calculos.py`, siempre que no exista una caché válida.

Existen excepciones:

- Si ya existe un `.pyc` válido, Python puede reutilizarlo.
- Si no tiene permisos de escritura, puede ejecutar el módulo sin guardar el archivo.
- Si utilizamos `python -B`, se desactiva la escritura de archivos `.pyc`.
- También podemos desactivarla mediante la variable de entorno `PYTHONDONTWRITEBYTECODE`.

Por lo tanto, debemos distinguir dos conceptos:

**Compilar a bytecode no es lo mismo que guardar bytecode en un archivo `.pyc`.**

---

## ¿Dónde se guardan los archivos .pyc?

Normalmente se almacenan en una carpeta llamada:

`__pycache__`

Esta carpeta se crea en el directorio donde se encuentra el módulo importado.

Ejemplo:

```text
proyecto/
    main.py
    calculos.py
    __pycache__/
        calculos.cpython-314.pyc
```

El nombre del archivo contiene información importante:

- `calculos`: nombre del módulo.
- `cpython`: implementación de Python.
- `314`: versión de Python, en este caso 3.14.
- `.pyc`: extensión del archivo de bytecode.

¿Por qué se incluye la versión?

Porque el bytecode puede cambiar entre versiones de Python.

Esto permite que distintas versiones de CPython mantengan archivos de caché separados para un mismo módulo.

---

## ¿Cómo sabe Python si un .pyc sigue siendo válido?

Python necesita comprobar que el bytecode almacenado corresponde al código fuente actual.

Para eso existen principalmente dos mecanismos.

### A. Fecha de modificación y tamaño del archivo

Es el mecanismo habitual.

Cuando Python genera el `.pyc`, guarda en su encabezado información del archivo `.py` original:

1. Fecha y hora de la última modificación (*timestamp*).
2. Tamaño del archivo en bytes.

La próxima vez que importamos el módulo, Python compara esa información con los datos actuales del archivo fuente.

Si coinciden, considera válida la caché.

Si no coinciden, vuelve a compilar el módulo y normalmente reemplaza el `.pyc` anterior.

Una aclaración: Python no se limita a comprobar si el `.pyc` es más nuevo que el `.py`.

Compara los metadatos almacenados dentro del `.pyc` con los del archivo fuente.

Este mecanismo tiene una pequeña limitación: si modificamos el contenido de un archivo, pero conservamos exactamente el tamaño y el timestamp registrado, Python podría no detectar el cambio.

### B. Validación mediante hash

Existe otro mecanismo que utiliza un hash del contenido del código fuente.

En este caso, el archivo `.pyc` almacena un hash calculado a partir del `.py`.

Cuando corresponde validar la caché, Python puede calcular nuevamente el hash del archivo fuente y compararlo con el almacenado.

Si son diferentes, vuelve a compilar.

Este mecanismo permite detectar cambios en el contenido aunque se mantengan la fecha y el tamaño del archivo.

También existe una modalidad en la que el hash se almacena, pero Python no lo comprueba automáticamente durante la importación.

El mecanismo habitual de CPython sigue siendo el basado en timestamp y tamaño.

---

## ¿Qué sucede al importar un módulo?

Podemos encontrar varias situaciones.

**A) Existe el archivo .py, pero no existe el .pyc.**

Python compila el módulo a bytecode, lo ejecuta y normalmente guarda una copia en `__pycache__`.

**B) Existe el archivo .pyc, pero no existe el .py.**

Aquí debemos distinguir dos situaciones.

Si el `.pyc` está dentro de `__pycache__`, Python normalmente no lo utilizará para importar el módulo cuando falta el archivo fuente correspondiente.

Pero si el archivo compilado se encuentra directamente en el lugar donde Python buscaría el módulo y tiene un nombre como `calculos.pyc`, puede importarse sin necesidad del `.py`.

Por lo tanto, es posible distribuir módulos que contienen únicamente bytecode, aunque existen limitaciones.

**C) Existen el .py y el .pyc, y la caché es válida.**

Python reutiliza el bytecode almacenado.

No necesita volver a compilar el código fuente.

**D) Existen el .py y el .pyc, pero la caché ya no es válida.**

Python vuelve a compilar el archivo fuente y normalmente actualiza el `.pyc`.

**Una aclaración importante:** reutilizar el bytecode no significa evitar la ejecución del módulo.

En un nuevo proceso de Python, el módulo vuelve a ejecutarse durante su primera importación.

Lo que se evita es repetir la compilación.

Dentro de un mismo proceso, las importaciones posteriores de un módulo ya cargado normalmente reutilizan el objeto almacenado en `sys.modules`, sin volver a ejecutar su código.

---

## ¿Puedo distribuir mis programas utilizando solamente archivos .pyc?

Sí, pero existen limitaciones importantes.

### 1. Compatibilidad entre versiones

El bytecode de CPython no garantiza compatibilidad entre versiones.

Un archivo generado con Python 3.14 no necesariamente funcionará con Python 3.13 o 3.15.

Por lo tanto, el destinatario necesita una versión compatible de CPython.

### 2. Ubicación de los archivos

Si distribuimos solamente bytecode, debemos respetar la estructura de importación correspondiente.

Por ejemplo, podemos distribuir un módulo como:

`calculos.pyc`

Sin necesidad de incluir `calculos.py`.

No alcanza con entregar únicamente la carpeta `__pycache__` que Python generó durante las importaciones.

### 3. Seguridad del código fuente

Muchas veces se piensa que, como el código está compilado, podemos distribuirlo sin preocuparnos por que alguien acceda a nuestra implementación.

Esto no es correcto.

Los archivos `.pyc` pueden analizarse y, en muchos casos, descompilarse para reconstruir buena parte del código fuente.

No necesariamente podremos recuperar exactamente el archivo original, porque se pierden elementos como los comentarios y determinados detalles de formato.

Sin embargo, la lógica del programa puede quedar expuesta.

Por lo tanto, **distribuir archivos `.pyc` no constituye una medida confiable para proteger nuestro código fuente**.

### 4. Dependencia de Python

Un archivo `.pyc` no es un ejecutable independiente.

El destinatario necesita una implementación y versión compatible de Python, además de las dependencias utilizadas por el programa.

Existen herramientas para empaquetar aplicaciones Python y facilitar su distribución, pero ese es otro tema.

---

## Conclusiones

La diferencia principal entre un archivo `.py` y un `.pyc` es que:

- **`.py`** contiene el código fuente que escribimos.
- **`.pyc`** contiene una representación compilada de ese código, en forma de bytecode.

En CPython, el código fuente se compila a bytecode antes de ejecutarse.

Sin embargo, no es obligatorio guardar ese bytecode en un archivo `.pyc`.

Los archivos `.pyc` funcionan principalmente como un mecanismo de caché.

Su ventaja es evitar compilaciones repetidas durante la importación de módulos.

Esto puede mejorar el tiempo de inicio o carga de una aplicación, especialmente cuando importa numerosos módulos.

Pero no hace que las instrucciones del programa se ejecuten más rápido.

Tampoco convierte nuestro código en un ejecutable independiente ni lo protege de manera confiable contra la ingeniería inversa.

**La idea central que me llevo de la clase: Python compila a bytecode para ejecutar el código; los archivos `.pyc` permiten guardar y
 reutilizar ese bytecode cuando importamos módulos.**
"""
