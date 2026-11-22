"""
14 . Break vs Continue

Apuntes de clase

Tanto break como continue nos permiten interrumpir el normal flujo de nuestro loop.
Lo normal es que se ejecute todo el cuerpo del bucle y pase al siguiente valor, break nos permite cortar el flujo.
Son mecanismos o herramientas que nos da el lenguaje para controlar el flujo de los bucles.
No funcionan afuera de un bucle, no existen para el lenguaje en ese caso y dan un error de sintaxis.

"""

print("* Start *")
for one_character in "abcde":
    if one_character == "c":
        break  # stop the foor loop right now, entonces el output será a,b
    print(one_character)
print("* End *")

# Esto también es válido para un while
x = 5
while x > 0:
    if x == 2:
        break
    print(x)
    x -= 1

while True:
    name = input("Enter your name:").strip()

    if not name:  # Meaning: did we get a black string?
        break
    print(f"Hello, {name}")


# ¿Y que es lo que pasa con continue?
print("* Start Loop 2 *")
for one_character in "abcde":
    if one_character == "c":
        continue  # No imprimirá 'c' porque continue interrumpe la iteración actual y pasa a la siguiente, sin terminar el bucle.
    print(one_character)
print("* End Loop 2 *")

# Esto se usa mucho en manejo de archivos por poner un ejemplo
for one_line in open("/etc/passwd"):
    if one_line.startswith("#"):
        continue  # meaning: go to onto the next line / iteration
    print(one_line.split(":")[0])  # print the username
