"""
Modificación de los ejercicios 1, 2 y 3 de las partes 1, 2 y 3 de la Guía de ejercicios 1.

"""


# >>>> Ejercicio 2 - Parte 1:
# Permita ingresar un número y mostrar su cuadrado.

print("::: 2. Cuadrado de un número :::")

# Mientras lo ingresado no sea un número entero sigo preguntando por uno válido.
entrada_correcta = False
while not entrada_correcta:
    try:
        numero_ingresado = int(input("Ingrese un número entero: "))
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

cuadrado = numero_ingresado ** 2
print(">>> El cuadrado del número ingresado es: " + str(cuadrado))