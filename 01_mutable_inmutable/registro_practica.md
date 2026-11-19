Registro de práctica — Python
Alertas de Pylance

Formato: fecha · fuente/ejercicio · mensaje · qué significa · qué aprendí · fuente

2026-11-19 · Ace Python Interview (Lerner) · alias de listas
Código: mylist = [10, 20, 30, 40, 50] → mylist[0] = '???'
Mensaje: No overloads for "__setitem__" match the provided arguments
Qué significa: Pylance infiere list[int] del literal. mylist[0] = x llama a mylist.__setitem__(0, x), que tiene dos overloads: (índice, int) y (slice, Iterable[int]). Un str no encaja en ninguno.
¿Error real? No. Python no chequea tipos en ejecución, así que el código corre bien.
Qué aprendí: la sintaxis obj[i] = v es azúcar para __setitem__. Mezclar tipos en una lista suele ser mala señal en código real. Si es intencional: mylist: list[int | str].
Fuentes: datamodel __setitem__ · typing @overload · Pyright type inference
Ejercicios donde me trabé (para repaso)

Formato: fecha · fuente/ejercicio · en qué me trabé · ¿rehecho? (fecha)

2026-11-19 · Ace Python Interview, Q1 (mutable vs. inmutable) · por qué una clave de dict tiene que ser hashable (lo intuí, no lo razoné solo); confundí "variable" con "objeto" · pendiente
