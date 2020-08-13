
# >>>> Ejercicio 2:

# Permita ingresar dos números y muestre el mayor. Siempre serán diferentes.

print("::: 2. Obteniendo el MAYOR :::")

primer_numero = float(input("Ingrese el primer número: "))
segundo_numero = float(input("Ingrese el segundo número: "))

if primer_numero > segundo_numero:
    print("El mayor es el primer número (" + str(primer_numero) + ").")
elif primer_numero < segundo_numero:
    print("El mayor es el segundo número ({})".format(segundo_numero))
else:
    print(">>> Los números son iguales.")

# -----------------------------------------------------------------------------------
# Esta resolución solo sirve si estrictamente el usuario ingresa dos valores         |
# que sean distintos porque siguiendo la lógica de la resolución, si se              |
# ingresa el mismo número dos veces entonces el flujo de ejecución del               |
# programa seguiría el camino del else e imprimiría: "El mayor es el                 |
# segundo número ...) cosa que no debe suceder. Esto se soluciona de distintas       |
# formas, pero yo lo solucioné con un Try-Catch (en diferentes archivo y carpeta)    |
# ----------------------------------------------------------------------------------