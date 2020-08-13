"""
Modificación de los ejercicios 1, 2 y 3 de las partes 1, 2 y 3 de la Guía de ejercicios 1.

"""


# >>>> Ejercicio 2 - Parte 3:

# *** APLICAN LOS MISMOS CONCEPTOS QUE EL ANTERIOR PERO ESTE SUMA QUE LOS NUM. DEBEN SER PARES ***

# Imprima el cuadrado de los primeros diez números enteros pares.

print("::: 2. Cuadrado de los primeros 10 números pares :::")
print(" ")

for x in range(11):
    
    if x == 0:
        continue

    if x % 2 == 0:  # Todo número par dividido 2 da como resto cero.
        print(x ** 2)