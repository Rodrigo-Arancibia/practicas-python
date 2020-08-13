
# >>>> Ejercicio 5:

# Permita el usuario ingresar una palabra y muestre por pantalla la longitud de
# la palabra (nota: usar la función len() ). Cuando la palabra sea “salir” o
# “SALIR”, cortar la ejecución sin mostrar el numero 5
# (por la cantidad de letras que tiene "salir").

print("::: 5. Impresión en mayúsculas con opción de 'Salir' :::")
print(" ")


palabra = input("Ingrese una palabra: ")
palabra = palabra.upper()

while palabra != "SALIR":

    print(len(palabra))

    palabra = input("Ingrese una palabra: ")
    palabra = palabra.upper()