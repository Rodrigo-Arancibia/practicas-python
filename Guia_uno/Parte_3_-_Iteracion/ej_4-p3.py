
# >>>> Ejercicio 4:

# Recorra las letras de una frase ingresada por teclado, imprima cada una en
# mayúsculas pero corte la ejecución al encontrar un espacio en blanco.

print("::: 4. Impresión en mayúsculas :::")
print(" ")


frase = input("Ingrese una frase: ")

frase = frase.upper()

print(frase)
espacio_encontrado = False
while not espacio_encontrado:
    for i in frase:
        if i == " ":
            espacio_encontrado = True
            break
        print(i)
print(">>> ESPACIO ENCONTRADO. Se interrumpió la ejecución del programa!!!")