"""
Modificación de los ejercicios 1, 2 y 3 de las partes 1, 2 y 3 de la Guía de ejercicios 1.

"""


# >>>> Ejercicio 3 - Parte 2:

# Permita ingresar dos números. Si ambos son iguales, imprimir el mensaje
# "DE IGUAL VALOR", en caso contrario imprimir "HAY DESIGUALDAD EN EL MUNDO".

print("::: 3. Comprobando números :::")

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


if primer_numero == segundo_numero:
    print("DE IGUAL VALOR")
else:
    print("HAY DESIGUALDAD EN EL MUNDO")