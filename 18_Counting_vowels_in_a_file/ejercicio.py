"""Consigna: vowel_count_six(filename)

Abrí el archivo con with y encoding="utf-8".
Contá también las vocales acentuadas (á é í ó ú, en mayúscula y minúscula). Agregá la ü si querés.
Si el archivo no existe o es una carpeta, la función tiene que dejar claro que no pudo contar. No puede devolver un 0 que se confunda con 
"no hay vocales". El mecanismo lo elegís vos.
Atrapá el caso de la carpeta de forma que funcione tanto en Windows como en Linux o Mac.
Pasala por Black y Ruff antes de mostrármela.
"""


def vowel_count_six(filename):
    count = 0
    try:
        with open(filename, encoding="utf-8") as f:
            for one_line in f:
                for one_character in one_line:
                    if one_character in "aeiouáéíóúAEIOUÁÉÍÓÚ":
                        count += 1
    except (
        PermissionError,
        IsADirectoryError,
        FileNotFoundError
    ) as e:
        print(e)
        return None
    return count


print(vowel_count_six("prueba.txt"))
print(vowel_count_six("acentos.txt"))
print(vowel_count_six("no_existe.txt"))
print(vowel_count_six("."))
