
# >>>> Ejercicio 9:

# Permita ingresar números como en el ejemplo anterior, hasta ingresar el 99.
# Mostrar la suma de todos los números ingresados mayores a 25.

# Nota: el 99 no debe ser parte de la suma.

print("::: 9. Sumatoria de números (con posibilidad de salir) :::")
print(" ")

carga_terminada = False
sumatoria = 0

while not carga_terminada:  # Digitar 99 para terminar la carga.
    
    n = int(input("Número: (el 99 termina la carga de números)...  "))
    
    if n == 99:
        carga_terminada = True
        break
    
    if n > 25:
        sumatoria += n

# Cuando se apreta el 99 (carga terminada).
# Muestra la sumatoria solo de números MAYORES A 25.
print(" ")
print(sumatoria)