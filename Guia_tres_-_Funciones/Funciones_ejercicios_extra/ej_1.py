# 1. Función que imprima la cantidad de argumentos con los que fue llamada.

def ran(*args):

    print(len(args))

ran()
ran("Hola", 28, "Rodrigo")
ran(1, 3.5, ["Hola", "Chau", 2020], {"Rodrigo": "Santa Fe"})