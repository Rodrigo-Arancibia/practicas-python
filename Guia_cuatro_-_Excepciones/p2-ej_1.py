"""
Modificación de los ejercicios 1, 2 y 3 de las partes 1, 2 y 3 de la Guía de ejercicios 1.

"""


# >>>> Ejercicio 1 - Parte 2:

# Permita ingresar dos números e informar cómo es el primero
# con respecto al segundo ingresado: MAYOR , MENOR o IGUAL.

print("::: 1. ¿Mayor, menor, iguales? :::")

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

if primer_numero > segundo_numero:
    print(">>> El número {}".format(primer_numero) + " es MAYOR a {}".format(segundo_numero))
elif primer_numero < segundo_numero:
        print(">>> El número " + str(primer_numero) + " es MENOR a " + str(segundo_numero))
else:
    print(">>> Los números ingresados son iguales!")