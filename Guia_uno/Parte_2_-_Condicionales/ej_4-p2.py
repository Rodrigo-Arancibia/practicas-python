
# >>>> Ejercicio 4:

# Permita ingresar una hora e indique, con un mensaje por pantalla si es de
# MAÑANA, de TARDE, o de NOCHE, teniendo en cuenta que:
#       de 00 a 12 hs   MAÑANA
#       de 13 a 19 hs   TARDE
#       de 20 a 24 hs   NOCHE
# Si coloca una hora no existente, emitir el mensaje "HORA EQUIVOCADA".

print("::: 4. ¿'CUÁNDO' estamos? :::")

# ::: VALIDACIONES DE INGRESO DE DATOS :::

# Mientras el ingreso no sea válido sigo preguntando por uno válido.
entrada_correcta = False
while not entrada_correcta:
    try:
        hora_ingresada = int(input("Ingrese la hora en formato de 24 hs: "))    # Si no es entero, capturo el error y vuelvo a solicitar ingreso.
        if hora_ingresada % 2 == 0 or hora_ingresada % 2 == 1:  # Si la hora es número entero sigo evaluando.
            if hora_ingresada >= 0 and hora_ingresada <= 23:    # Si la hora está entre 0 y 23 doy el OK y salgo del bucle.
                print("Entrada correcta.")
                print(" ")
                entrada_correcta = True
            else:   # Mientras el ingreso de la hora no sea entre 0 y 23.
                print(" ")
                print(">>> ERROR. HORA EQUIVOCADA. Ingrese una hora comprendida entre 0 y 23.")
                print(" ")
                continue
    except: # Si el número no es entero salta a esta línea.
        print(" ")
        print(">>> ERROR. HORA EQUIVOCADA. Escriba un número entero.")
        print(" ")
        continue
    else:
        break

# ::: EVALUACIÓN Y RESOLUCIÓN DE LOS DATOS INGRESADOS :::

if hora_ingresada >= 0 and hora_ingresada <= 12:
    print("MAÑANA")
elif hora_ingresada >= 13 and hora_ingresada <= 19:
    print("TARDE")
elif hora_ingresada >= 20 and hora_ingresada <= 24:
    print("NOCHE")