"""
Modificación de los ejercicios 1, 2 y 3 de las partes 1, 2 y 3 de la Guía de ejercicios 1.

"""


# >>>> Ejercicio 3 - Parte 1:
# Permita ingresar dos números (A y B) e informar el resultado del producto
# (A*B), la suma (A + B) y la resta (A - B) .

print("::: 3. Producto, Suma y Diferencia :::")

# Primer número.

# Mientras lo ingresado no sea un número entero sigo preguntando por uno válido.
entrada_correcta = False
while not entrada_correcta:
    try:
        numero_A = int(input("Ingrese el primer número (entero) para 'A': "))
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
        numero_B = int(input("Ingrese el segundo número (entero) para 'B': "))
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

producto = numero_A * numero_B
suma = numero_A + numero_B
resta = numero_A - numero_B

print(">>> A x B: " + str(producto))
print(" ")
print(">>> A + B: " + str(suma))
print(" ")
print(">>> A - B: " + str(resta))