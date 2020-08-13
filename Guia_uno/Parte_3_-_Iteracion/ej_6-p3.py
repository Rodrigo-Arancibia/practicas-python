
# >>>> Ejercicio 6:

# Permita encontrar el menor número mayor que cero que es a la vez múltiplo
# de 7, 11 y 1008.

print("::: 6. Menor número cumpliendo ciertas condiciones :::")
print(" ")


for x in range(99999):
    if x > 0:
        if x % 7 == 0 and x % 11 == 0 and x % 1008 == 0:
            print(" ")
            print("Resultado:", x)
            break