"""
Modificación de los ejercicios 1, 2 y 3 de las partes 1, 2 y 3 de la Guía de ejercicios 1.

"""


# >>>> Ejercicio 2 - Parte 2:

# Permita ingresar dos números y muestre el mayor. Siempre serán diferentes.

print("::: 2. Obteniendo el MAYOR :::")

# Primer número.

# Mientras lo ingresado no sea un número entero sigo preguntando por uno válido.
entrada_correcta = False
while not entrada_correcta:
    try:
        primer_numero = float(input("Ingrese el primer número: "))
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
        segundo_numero = float(input("Ingrese el segundo número: "))
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
    print("El mayor es el primer número (" + str(primer_numero) + ").")
elif primer_numero < segundo_numero:
    print("El mayor es el segundo número ({})".format(segundo_numero))
else:
    print(">>> Los números son iguales.")

# -------------------------------------------------------------------------------
# Esta resolución solo sirve si estrictamente el usuario ingresa dos valores     |
# que sean distintos porque siguiendo la lógica de la resolución, si se          |
# ingresa el mismo número dos veces entonces el flujo de ejecución del           |
# programa seguiría el camino del else e imprimiría  "El mayor es el             |
# segundo número ...) cosa que no debe suceder.                                  |
# -------------------------------------------------------------------------------