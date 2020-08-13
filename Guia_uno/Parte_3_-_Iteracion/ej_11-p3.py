
# >>>> Ejercicio 11:

# Permita ingresar números como en 8 y 9 hasta que el usuario ingrese el 0.
# Mostrar el promedio de los números ingresados. Ayuda: será necesario una
# variable en la cual llevar la cuenta de la cantidad de números ingresados.

carga_terminada = False
sumatoria = 0
conteo_numeros_ingresados = 0

while not carga_terminada:  # Digitar 0 para terminar la carga.
    
    n = float(input("Número: (el cero termina la carga de números)...  "))

    if n == 0:
        carga_terminada = True
        break
    
    conteo_numeros_ingresados += 1

    sumatoria += n

# Cuando se apreta el 0 (carga terminada).
# Muestra el promedio de los n° ingresados.

print("::: 11. Seguimos sumando más números :::")
print(" ")

promedio = sumatoria / conteo_numeros_ingresados
print(" ")
print("Cantidad de números:", conteo_numeros_ingresados)
print(" ")
print(round(promedio, 2))