
# >>>> Ejercicio 13:

# Imprima todos los números enteros entre 0 y el número ingresado.
# Validar que el número ingresado sea mayor que cero.

# Si el punto anterior lo hizo con while, hacerlo con for.
# Si lo hizo con for, hacerlo con while.


# EJEMPLO:
# Si el número ingresado es 4, imprimir: 0, 1 , 2, 3, 4.
# Si el número ingresado es 100, imprimir: 1, 2... hasta el 100.

print("::: 13. Menor número cumpliendo ciertas condiciones :::")
print(" ")

print("Solo se aceptan números ENTEROS y POSITIVOS !!!")

entrada_correcta = False
while not entrada_correcta:
    try:
        n = int(input("Número: "))    # Si no es entero, capturo el error y vuelvo a solicitar ingreso.
        if n % 2 == 0 or n % 2 == 1:  # Si es entero sigo evaluando.
            if n > 0:    # Si es mayor que cero doy el OK y salgo del bucle.
                print("Entrada correcta.")
                entrada_correcta = True
            else:   # Mientras el ingreso sea un número menor o igual que cero.
                print(" ")
                print(">>> ERROR. Ingrese un número mayor que cero.")
                print(" ")
                continue
    except: # Si el número no es entero salta a esta línea.
        print(" ")
        print(">>> ERROR. Escriba un número entero.")
        print(" ")
        continue
    else:
        break

var_aux = 0     # Variable que me permite hacer la sumatoria de los números.

for i in range(n+1):  # Función range(n) va de '0' a 'n-1' por eso le sumo 1. 
    
    print(var_aux)
    var_aux += 1