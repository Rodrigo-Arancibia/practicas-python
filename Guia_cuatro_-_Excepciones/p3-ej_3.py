"""
Modificación de los ejercicios 1, 2 y 3 de las partes 1, 2 y 3 de la Guía de ejercicios 1.

"""


# >>>> Ejercicio 3 - Parte 3:

# Imprima el siguiente patrón:

#
# #
# # #
# # # #
# # # # #

# (notar que los cardinales están separados por espacios)
def con_While():
    print("::: 3. Patrón de cardinales :::")
    print(" ")
    print("Resolución con While")
    
    n = 1
    while n < 6:
        print(n * "# ")
        n += 1


def con_For():
    print("::: 3. Patrón de cardinales :::")
    print(" ")
    print("Resolución con For")

    for x in range(6):
        if x == 0:
            continue

        print(x * "# ")

# con_While()
con_For()