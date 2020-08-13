
# ::::::::  p2: CONJUNTOS  ::::::::

# >>>> Ejercicio 1:

# Definir un conjunto con los primeros diez enteros divisibles por cinco.
# 
# Definir un conjunto con los primeros quince enteros divisibles por siete.
# 
# Realizar las operaciones de unión, intersección y diferencia simétrica
# (en ambos sentidos) entre ambos conjuntos.

print("::: 1. Operaciones entre conjuntos :::")

# Observación: X es divisible por Y cuando al dividir el X entre Y el resto es cero.

lista_A = []    # Sirve para armar el "Conjunto A"
lista_B = []    # Sirve para armar el "Conjunto B"

# Armando el conjunto A:
cont = 0
for i in range(99):
    
    while cont < 10:    # Pide los primeros 10.
        if i % 5 == 0:
            lista_A.append(i)
            cont += 1
        break

conjunto_A = set(lista_A)   # Conjunto A, listo.

# Armando el conjunto B:
cont = 0
for i in range(99):
    
    while cont < 15:    # Pide los primeros 15.
        if i % 7 == 0:
            lista_B.append(i)
            cont += 1
        break

conjunto_B = set(lista_B)   # Conjunto B, listo.

# Imprimo los conjuntos terminados:
print("Conjunto A:", conjunto_A)
print("Conjunto B:", conjunto_B)

#       ****** OPERACIONES ENTRE CONJUNTOS ******

def union():
    print("")
    print(">> A unión B:")
    print(conjunto_A | conjunto_B)


def interseccion_A_con_B():
    print("")
    print(">> A intersección B:")
    print(conjunto_A & conjunto_B)


def interseccion_B_con_A():
    print("")
    print(">> B intersección A:")
    print(conjunto_B & conjunto_A)


def dif_A_B():
    print("")
    print(">> A diferencia B:")
    print(conjunto_A - conjunto_B)


def dif_B_A():
    print("")
    print(">> B diferencia A:")
    print(conjunto_B - conjunto_A)


def dif_simet_A_B():
    # Fórmula: (A - B) | (B - A)
    print("")
    print(">> A diferencia simétrica B:")
    A_menos_B = conjunto_A - conjunto_B
    B_menos_A = conjunto_B - conjunto_A
    print(A_menos_B | B_menos_A)


def dif_simet_B_A():
    # Fórmula: (B - A) | (A - B)
    print("")
    print(">> B diferencia simétrica A:")
    B_menos_A = conjunto_B - conjunto_A
    A_menos_B = conjunto_A - conjunto_B
    print(B_menos_A | A_menos_B)

#       ****** LLAMADAS ******
union()
interseccion_A_con_B()
interseccion_B_con_A()
dif_A_B()
dif_B_A()
dif_simet_A_B()
dif_simet_B_A()