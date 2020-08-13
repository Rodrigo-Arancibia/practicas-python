
# >>>> Ejercicio 12:

# Imprima todos los números enteros entre 0 y el número ingresado.
# Validar que el número ingresado sea mayor que cero.


# EJEMPLO:
# Si el número ingresado es 4, imprimir: 0, 1 , 2, 3, 4.
# Si el número ingresado es 100, imprimir: 1, 2... hasta el 100.

print("::: 12. Mostrando todos los números anteriores :::")
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
while var_aux <= n:
    
    print(var_aux)
    var_aux += 1