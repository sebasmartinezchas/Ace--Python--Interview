"""
Apuntes de clase



"""


# Count vowels in a file, given a filename - Forma facil y solo aceptable para archivos de pocos bytes
def vowel_count(filename):
    f = open(filename, "r")
    text = f.read()

    count = 0
    for one_character in text:
        if one_character in "aeiouAEIOU":
            count += 1
    return count


print(vowel_count("prueba.txt"))


# Forma más optima con loop adicional iterando sobre cada línea y no sobre todo el texto
def vowel_count_two(filename):
    count = 0

    f = open(filename, "r")

    for one_line in f:
        for one_character in one_line:
            if one_character in "aeiouAEIOU":
                count += 1

    return count


print(vowel_count_two("prueba.txt"))

# Se pueden hacer algunas mejoras, No escribir f


def vowel_count_three(filename):
    count = 0

    for one_line in open(filename, "r"):
        for one_character in one_line:
            if one_character in "aeiouAEIOU":
                count += 1
    return count


print(vowel_count_three("prueba.txt"))


# ¿Que pasa si el archivo no existe? Hagamos una versión 4
def vowel_count_four(filename):
    count = 0

    try:
        for one_line in open(filename, "r"):
            for one_character in one_line:
                if one_character in "aeiouAEIOU":
                    count += 1
    except FileNotFoundError as e:
        print(f"No such file {e}")

    return count


print(vowel_count_four("prueba.txt"))


# ¿Que pasaría si filename fuera un directorio. Hagamos la 5ta versión
def vowel_count_five(filename):
    count = 0

    try:
        for one_line in open(filename, "r"):
            for one_character in one_line:
                if one_character in "aeiouAEIOU":
                    count += 1
    except FileNotFoundError as e:
        print(f"No such file {filename}")
    except IsADirectoryError as e:
        print(f"{e} is a directory -use files!")

    return count


print(vowel_count_five("prueba.txt"))


# Versión 6

"""
Consigna: vowel_count_six(filename)

Abrí el archivo con with y encoding="utf-8".
Contá también las vocales acentuadas (á é í ó ú, en mayúscula y minúscula). Agregá la ü si querés.
Si el archivo no existe o es una carpeta, la función tiene que dejar claro que no pudo contar. No puede devolver un 0 que se confunda con "no hay vocales". El mecanismo lo elegís vos.
Atrapá el caso de la carpeta de forma que funcione tanto en Windows como en Linux o Mac.
Pasala por Black y Ruff antes de mostrármela.
"""


def vowel_count_six(filename):
    count = 0
    try:
        with open(filename, encoding="utf8") as f:
            for one_line in f:
                for one_character in one_line:
                    if one_character in "aeiouáéíóúAEIOUÁÉÍÓÚ":
                        count += 1
                        

    except FileNotFoundError as e:
        print(f"No such file {e}")
        return None
    except IsADirectoryError as e:
        print(f"{e} is a directory- use Files!")
        return None
    return count


print(vowel_count_six("prueba.txt"))
print(vowel_count_six("acentos.txt"))
print(vowel_count_six("no_existe.txt"))
print(vowel_count_six("."))
