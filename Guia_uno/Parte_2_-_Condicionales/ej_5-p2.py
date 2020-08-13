
# >>>> Ejercicio 5:

# Permita ingresar la hora y los minutos, y lo salude por pantalla de la
# siguiente manera:
#
#       "¡BUEN DIA!”        (6:00 a 12:30)
#       "¡BUENAS TARDES!"   (12:31 a 19:00)
#       "¡BUENAS NOCHES!"   (19:01 a 5:59)
#
# La hora y los minutos se ingresarán en dos variables, en caso de que alguno de los
# dos datos sean erróneos, mostrar un mensaje de error.

print("::: 5. Saludando :::")

hora = int(input("Indique la hora: "))
minutos = int(input("Indique los minutos: "))

mediodia = hora == 12 and minutos > 30

if hora >= 6 and (hora < 12 or hora == 12 and minutos <= 30):
    print("¡BUEN DÍA! Son las {}:{} hs.".format(hora, minutos))
elif (mediodia or hora >= 13) and (hora <= 18 or (hora == 19 and minutos == 0)):
    print("¡BUENAS TARDES! Son las {}:{} hs.".format(hora, minutos))
elif hora >= 19 and hora <= 23:
    print("¡BUENAS NOCHES! Son las {}:{} hs.".format(hora, minutos))
elif hora >= 0 and hora < 6:
    print("¡BUENAS NOCHES! Son las {}:{} hs.".format(hora, minutos))
else:
    print(">>> Hora incorrecta!!!")