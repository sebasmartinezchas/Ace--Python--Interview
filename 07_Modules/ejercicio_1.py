import saludo
import saludo

# Para mi se tiene que imprimir una vez sola , python lo encuenta y no lo carga dos veces
# https://docs.python.org/es/3.15/reference/import.html


# Efectivamente se imprimio una vez

"""
Se imprimió una sola vez. El primer import ejecutó el módulo y lo guardó en sys.modules. El segundo encontró el objeto en el caché y solo ligó el nombre.
Un módulo no es callable. Supongo que probaste saludo() después de import saludo y te dio TypeError: 'module' object is not callable. Ahí saludo es el módulo, y la función se llama con saludo.saludo().
Es la confusión de nombres que te comenté antes, y la descubriste vos, que vale más.
"""
