
# >>>> Ejercicio 11:

# Ingresar tres números y mostrarlos ordenados de mayor a menor.
# Ejemplo: si ingreso 5, 2, 4, mostrar como resultado 5 4 2.

print("::: 11. Ordenando de MAYOR a Menor :::")

print(">>> Resuelto utilizando   > exclusivamente <   condicionales <<<")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|
# OBSERVACIÓN: La resolución de este ejercicio se puede llevar a cabo de igual manera que el ejercicio anterior.   |
# Pero, aprovechando que el planteo de ambos es muy similar, puedo resolverlos de distinta manera para luego       |
# verificar que hay más de un método de resolución posible.                                                        |
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|

numero_A = int(input("Ingrese el primer número: "))
numero_B = int(input("Ingrese el segundo número: "))
numero_C = int(input("Ingrese el tercer número: "))

if numero_A > numero_B > numero_C:
    print(numero_A, numero_B, numero_C)
    print("Elejí el primer camino")     # Estas son ayudas para depurar el código.

elif numero_B > numero_A > numero_C:
    print(numero_B, numero_A, numero_C)
    print("Elejí el segundo camino")    # Estas son ayudas para depurar el código.

elif numero_C > numero_A > numero_B:
    print(numero_C, numero_A, numero_B)
    print("Elejí el tercer camino")

elif numero_C > numero_B > numero_A:
    print(numero_C, numero_B, numero_A)
    print("Elejí el cuarto camino")

else:
    print(">>> ERROR. Hay al menos dos números iguales!!")