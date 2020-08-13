
# >>>> Ejercicio 9:

# Permita ingresar las medidas de los tres lados de un triángulo y muestre a
# qué tipo de triángulo pertenecen: EQUILATERO, ISÓSCELES o ESCALENO.
#
# Por definición:
# * EQUILATERO: Tiene sus tres lados iguales.
# * ISÓSCELES: Tiene solo 2 lados iguales.
# * ESCALENO: Tiene sus tres lados desiguales.

print("::: 9. Categorizando triángulos :::")

lado_A = int(input("Ingrese una medida para el 'lado A': "))
lado_B = int(input("Ingrese una medida para el 'lado B': "))
lado_C = int(input("Ingrese una medida para el 'lado C': "))

if lado_A == lado_B and lado_B == lado_C:
    print("El triángulo es EQUILÁTERO.")
elif lado_A == lado_B or lado_A == lado_C or lado_B == lado_C:
    print("El triángulo es ISÓCELES.")
else:
    print("El triángulo es ESCALENO.")