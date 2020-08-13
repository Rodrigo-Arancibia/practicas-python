"""
Modificación de los ejercicios 1, 2 y 3 de las partes 1, 2 y 3 de la Guía de ejercicios 1.

"""


# >>>> Ejercicio 1 - Parte 3:

# Imprima el cuadrado de los primeros diez números enteros.

# Esta función For itera 10 veces, solo que la funcion range(x) va de 0 a 'x-1'
# En este caso va de cero a 10.

print("::: 1. Cuadrado de los primeros 10 números :::")
print(" ")

for x in range(11):

    # El cero no lo quiero elevar al cuadrado porque da cero entonces lo salteo con 'continue'.
    if x == 0:
        continue
    
    print(x ** 2)