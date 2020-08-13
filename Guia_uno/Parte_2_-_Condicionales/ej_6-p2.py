
# >>>> Ejercicio 6:

# Permita ingresar hora y minutos para calcular cuántos minutos faltan para la
# siguiente hora, y mostrarlos de la siguiente forma:
#
#       "DENTRO DE {minutos} MINUTOS SERÁ LA HORA {hora}"
#
# Ejemplo si la hora ingresada es 9 y los minutos, 15. Mostrar el mensaje:
#       "DENTRO DE 45 MINUTOS SERÁ LA HORA 10"
#
#  La hora se tomará de 0 a 23.
# 
# En caso que el operador ingrese algún dato erróneo, enviar un mensaje de error.

print("::: 6. ¿Cuánto falta? :::")

# ::: VALIDACIONES DE INGRESO DE DATOS :::

# Mientras el ingreso de la HORA no sea válido sigo preguntando por uno válido.
entrada_correcta = False
while not entrada_correcta:
    try:
        h = int(input("Ingrese la hora en formato de 24 hs: "))    # Si no es entero, capturo el error y vuelvo a solicitar ingreso.
        if h % 2 == 0 or h % 2 == 1:  # Si la hora es número entero sigo evaluando.
            if h >= 0 and h <= 23:    # Si la hora está entre 0 y 23 doy el OK y salgo del bucle.
                print("Entrada correcta.")
                print(" ")
                entrada_correcta = True
            else:   # Mientras el ingreso de la hora no sea entre 0 y 23.
                print(" ")
                print(">>> ERROR. Ingrese una hora comprendida entre 0 y 23.")
                print(" ")
                continue
    except: # Si el número no es entero salta a esta línea.
        print(" ")
        print(">>> ERROR. Escriba un número entero.")
        print(" ")
        continue
    else:
        break

# Mientras el ingreso del MINUTO no sea válido sigo preguntando por uno válido.
entrada_correcta = False
while not entrada_correcta:
    try:
        m = int(input("Ingrese minuto entre 0 y 59: "))    # Si no es entero, capturo el error y vuelvo a solicitar ingreso.
        if m % 2 == 0 or m % 2 == 1:  # Si el minuto es número entero sigo evaluando.
            if m >= 0 and m <= 59:    # Si el minuto está entre 0 y 59 doy el OK y salgo del bucle.
                print("Entrada correcta.")
                print(" ")
                entrada_correcta = True
            else:   # Mientras el ingreso del minuto no sea entre 0 y 59.
                print(" ")
                print(">>> ERROR. Ingrese un minuto comprendido entre 0 y 59.")
                print(" ")
                continue
    except: # Si el número no es entero salta a esta línea.
        print(" ")
        print(">>> ERROR. Escriba un número entero.")
        print(" ")
        continue
    else:
        break

# # Convierto los números ingresados a string para poder concatenarlos.
# horario = str(h) + str(m)
# # Convierto el string a número entero.
# horario = int(horario)

min_restantes = 60 - m

# Serie de evaluaciones.
if h + 1 > 23:
    h = 0
else:
    h += 1

if min_restantes > 1:
    info = " minutos"

print("Dentro de {}".format(min_restantes) + info + " será la hora {}.".format(h))