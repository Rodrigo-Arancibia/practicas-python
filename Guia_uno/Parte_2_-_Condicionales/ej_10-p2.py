
# >>>> Ejercicio 10:

# Ingresar tres números y mostrarlos ordenados de menor a mayor.
# Ejemplo: si ingreso 5, 2, 4, mostrar como resultado 2 4 5.

print("::: 10. Ordenando de MENOR a Mayor :::")

print(">>> Resuelto sin condicionales, utilizando sólo un poco de aritmética y las funciones min() y max() <<<")

numero_A = int(input("Ingrese el primer número: "))
numero_B = int(input("Ingrese el segundo número: "))
numero_C = int(input("Ingrese el tercer número: "))

# Obtengo el MENOR número:
numero_menor = min(numero_A, numero_B, numero_C)

# Obtengo el MAYOR número:
numero_mayor = max(numero_A, numero_B, numero_C)

# Calculo el número intermedio (entre Menor y Mayor):
numero_inter = (numero_A + numero_B + numero_C) - numero_menor - numero_mayor

# EJEMPLO:
# Si ingresamos: numero_A, numero_B, numero_C = 3, 2, 1
# numero_menor = 1
# numero_mayor = 3
# numero_inter = (3 + 2 + 1) - 1 - 3 => 2

print("Los números ordenados de menor a mayor son: {} {} {}".format(numero_menor, numero_inter, numero_mayor))