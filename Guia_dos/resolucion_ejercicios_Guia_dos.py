
#---------- DECLARACIÓN DE FUNCIONES ----------#

# >>>> Ejercicio 1:
# Diseñar un algoritmo que permita realizar la suma de 2 números.

def ejercicio_1():
    numero_1 = int(input("Ingrese el primer número: "))
    numero_2 = int(input("Ingrese el segundo número: "))
    print("La suma de los números ingresados es:", numero_1 + numero_2)




# >>>> Ejercicio 2:
# Diseñar un algoritmo que permita sumar una lista de 11 números.

def ejercicio_2():
    lista = []
    for i in range(0, 11):
        print("Ingrese un número, para la posición", i, "de la lista: ")
        numero_ingresado = int(input())
        lista.append(numero_ingresado)

    var_aux = 0
    for i in range(0, len(lista)):
        var_aux += lista[i]

    print("La suma de los todos los números ingresados es:", var_aux)




# >>>> Ejercicio 3:
# Describir un algoritmo que permita leer 2 números e informe el mayor.

def ejercicio_3():
    numero_1 = int(input("Ingrese el primer número: "))
    numero_2 = int(input("Ingrese el segundo número: "))

    if numero_1 > numero_2:
        print("El número " + str(numero_1) + " es mayor.")
    elif numero_1 < numero_2:
        print("El número " + str(numero_2) + " es mayor." )




# >>>> Ejercicio 4:
# Describir un algoritmo que permita leer 4 números e informar el promedio.

def ejercicio_4():
    numero_1 = int(input("Ingrese el primer número: "))
    numero_2 = int(input("Ingrese el segundo número: "))
    numero_3 = int(input("Ingrese el tercer número: "))
    numero_4 = int(input("Ingrese el cuarto número: "))

    # Podemos poner una variable para poder modifiar fácilmente cuántos números
    # fueron ingresados (en este caso es obligatorio poner 4 números).
    cantidad_de_numeros = 4
    promedio = (numero_1 + numero_2 + numero_3 + numero_4) / cantidad_de_numeros

    print("El promedio de los números ingresados es: " + str(promedio))




# >>>> Ejercicio 5:
# Elaborar un algoritmo para leer 3 números y determinar si uno es la suma de los otros dos.
# Ejemplo:
# Si leo 3, 5 y 8 entonces informo que 8 = + 3
# Si leo 1, 4 y 12 entonces no informo ninguno.

def ejercicio_5():
    numero_1 = int(input("Ingrese el primer número: "))
    numero_2 = int(input("Ingrese el segundo número: "))
    numero_3 = int(input("Ingrese el tercer número: "))

    if numero_1 + numero_2 == numero_3:
        print("Correcto -> " + str(numero_1) + " + " + str(numero_2) + " = " + str(numero_3))
    else:
        print("Incorrecto.")




# >>>> Ejercicio 6:
# Construir un algoritmo que lea la categoría y el sueldo de un trabajador,
# calcule el aumento correspondiente teniendo en cuenta la siguiente tabla:

# Incrementos         Categoría Aumento
#     1                      15 %
#     2                      10 %
#     3                      8 %
#     4                      7 %

def ejercicio_6():

    cat = int(input("Ingrese categoría: "))
    sueldo = float(input("Ingrese sueldo: "))

    # Estas variables me ayudan a modificar fácilmente el porcentaje de aumento según la categoría.
    aumento_cat_1 = 15
    aumento_cat_2 = 10
    aumento_cat_3 = 8
    aumento_cat_4 = 7

    if cat == 1:
        sueldo += sueldo + aumento_cat_1 * 100
    elif cat == 2:
        sueldo += sueldo + aumento_cat_2 * 100
    elif cat == 3:
        sueldo += sueldo + aumento_cat_3 * 100
    elif cat == 4:
        sueldo += sueldo + aumento_cat_4 * 100

    print("Categoría: " + str(cat) + ". Actualización de sueldo: $" + str(sueldo))


#--------------------------------------#