"""
Modificación de los ejercicios 1, 2 y 3 de las partes 1, 2 y 3 de la Guía de ejercicios n° 1.

"""


# >>>> Ejercicio 1 - Parte 1:
# Permita ingresar dos números y mostrar el resultado de su suma.

print("::: 1. Suma de dos números :::")

# Primer número.

# Mientras lo ingresado no sea un número entero sigo preguntando por uno válido.
entrada_correcta = False
while not entrada_correcta:
    try:
        primer_numero = int(input("Ingrese el primer número (entero): "))
        print("Entrada correcta.")
        print(" ")
        entrada_correcta = True
    except ValueError: # Si lo ingresado no es un número entero salta hacia acá.
        print(" ")
        print(">>> ERROR. Debe ingresar un número.")
        print(" ")
        continue
    else:
        break


# Segundo número.

# Mientras lo ingresado no sea un número entero sigo preguntando por uno válido.
entrada_correcta = False
while not entrada_correcta:
    try:
        segundo_numero = int(input("Ingrese el segundo número (entero): "))
        print("Entrada correcta.")
        print(" ")
        entrada_correcta = True
    except ValueError: # Si lo ingresado no es un número entero salta hacia acá.
        print(" ")
        print(">>> ERROR. Debe ingresar un número.")
        print(" ")
        continue
    else:
        break

suma = primer_numero + segundo_numero
print(">>> La suma de los números ingresados es: " + str(suma))