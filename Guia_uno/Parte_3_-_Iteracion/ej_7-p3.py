
# >>>> Ejercicio 7:

# Permita encontrar el menor número mayor que cero que es a la vez múltiplo
# de 7, 11 y 1008.

# Encontrar el segundo número que cumple la condición anterior.

print("::: 7. Menor número cumpliendo ciertas condiciones - Parte 2 :::")
print(" ")

cant = 0
j = 0
k = 0
for x in range(999999999999):
    if x > 0:
        while cant <= 1: 
            if x % 7 == 0 and x % 11 == 0 and x % 1008 == 0:           
                print(" ")
                # Condicionales opcionales. Solo para que quede más informativo.
                if cant == 0:
                    j = x
                    print("Primer número que cumple la condición dada:", j)
                if cant == 1:
                    k = x
                    print("Segundo número que cumple la condición dada:", k)
                cant += 1
            break