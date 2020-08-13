
# >>>> Ejercicio 8:

# Permita al usuario ingresar una serie de números (tipea un número,
# ENTER, tipea otro, ENTER). Luego de que el usuario termine la
# carga de números, el programa deberá mostrar en pantalla
# la suma de los números ingresados.
#
# Ayuda: usar input , while y una variable resultado en la
# que se vayan sumando los números a medida que se ingresan.

print("::: 8. Sumatoria de números :::")
print(" ")

carga_terminada = False
sumatoria = 0

while not carga_terminada:  # Digitar 0 para terminar la carga.
    
    n = int(input("Número: (el cero termina la carga de números)...  "))
    
    if n == 0:
        carga_terminada = True
        break
    
    sumatoria += n

# Cuando se apreta el cero (carga terminada).
# Muestra la sumatoria de TODOS los números ingresados.
print(" ")
print(sumatoria)