
# >>>> Ejercicio 1:

# Permita ingresar dos números e informar cómo es el primero
# con respecto al segundo ingresado: MAYOR , MENOR o IGUAL.

print("::: 1. ¿Mayor, menor, iguales? :::")

primer_numero = int(input("Ingrese el primer número (entero): "))
segundo_numero = int(input("Ingrese el segundo número (entero): "))

if primer_numero > segundo_numero:
    print(">>> El número {}".format(primer_numero) + " es MAYOR a {}".format(segundo_numero))
elif primer_numero < segundo_numero:
        print(">>> El número " + str(primer_numero) + " es MENOR a " + str(segundo_numero))
else:
    print(">>> Los números ingresados son iguales!")