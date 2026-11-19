2026-11-19 · Ace Python Interview, Q3 (*args / **kwargs) · no cubrí los parámetros positional-only (/); nombre "keyword-only"; caso de uso concreto (pensé que *args daba inmutabilidad) · pendiente: escribir en blanco def f(a, /, b, *args, c, **kwargs) y predecir qué llamadas fallan antes de correrlas


def f(a, /, b, *args, c, **kwargs): ...
#     │     │   │      │   └─ var-keyword: dict con lo que sobra por nombre
#     │     │   │      └─ keyword-only: solo por nombre
#     │     │   └─ var-positional: tupla con lo que sobra por posición
#     │     └─ normal: por posición o por nombre
#     └─ positional-only: solo por posición

Hay una interacción que vale la pena entender. Como a es positional-only, su nombre queda libre, y una llamada como f(1, 2, c=3, a=4) es válida. Ese a=4 no choca con el parámetro a: termina en kwargs. Sin la /, la misma llamada da TypeError por valor duplicado. Este es uno de los motivos que da el PEP 570 para introducir la sintaxis.

Dos precisiones que el tutor no hizo:

*args no recibe “todos” los posicionales, solo los que sobran después de llenar los parámetros con nombre. En tu punto 2 lo explicaste bien, pero en la definición del punto 1 quedó impreciso. La referencia del lenguaje dice que *identifier se inicializa con una tupla que recibe los posicionales en exceso, y **identifier con un mapeo nuevo que recibe los keyword en exceso (Function definitions).
Para tener keyword-only no hace falta *args. Alcanza con un * solo: def f(a, *, c) (Special parameters).

¿Es idiomático? No hubo código. El caso de uso más claro de la biblioteca estándar es print, cuya firma es print(*objects, sep=' ', end='\n', file=None, flush=False) (built-ins: print). Es un *args seguido de keyword-only. Ahí se ve por qué sep tiene que pasarse por nombre: si no, print lo trataría como un objeto más para imprimir.

¿Fluido o te trabaste? En lo conceptual fue fluido. Te trabaste en tres cosas:

el nombre técnico (“keyword-only”)
un caso de uso concreto: la idea de inmutabilidad no era correcta
la parte de positional-only, que no salió

Ninguna de las tres es de sintaxis. Justamente por eso conviene fijarlas escribiendo código.

Para el repaso

Lo anoté como pendiente. Abrí un archivo vacío y escribí de memoria def f(a, /, b, *args, c, **kwargs), con un print de cada parámetro. Después pensá cinco llamadas y, antes de correrlas, anotá cuáles fallan y por qué. Que te salgan las predicciones es la prueba de que lo entendiste.
