
# >>>> Ejercicio 10:

# Sume los números del 11 al 1099 incluyendo ambos extremos.

print("::: 10. Sumando números del 11 al 1099 :::")
print(" ")

carga_terminada = False
sumatoria = 0

while not carga_terminada:  # Digitar 0 para terminar la carga.
    
    n = int(input("Número: (el cero termina la carga de números)...  "))
    
    if n == 0:
        carga_terminada = True
        break
    
    if n >= 11 and n <= 1099:
        sumatoria += n

# Cuando se apreta el 0 (carga terminada).
# Muestra la sumatoria solo de números MAYORES A 25.
print(" ")
print(sumatoria)