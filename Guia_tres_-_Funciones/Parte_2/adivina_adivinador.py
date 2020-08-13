# Modificar el programa para que use funciones:
#
# ● Crear una función para la pista de si el secreto es par o impar.
# ● Crear una función para el while principal del juego cuyo parámetro sea el valor
# máximo de intentos.
# ● Finalmente mover todo el código a una función main(). Importarla desde otro archivo
# y llamarla.

import random


def main():
    mensaje = 'Diga un n° del 0 al 50: '
    secreto = random.randint(0,50)
    print(par_impar(secreto))
    intentos(mensaje, secreto)


def par_impar(secreto):
    par = (secreto % 2) == 0
    if par:
        result = "El número es par"
    else:
        result = "El número es impar"
    return result

def intentos(mensaje, secreto, max_intentos=5):
    cant_intentos = 0
    mensaje = "Diga un n° del 0 al 50: "
    secreto = random.randint(0,50)
    intento = int(input(mensaje))
    while intento != secreto:
        if cant_intentos >= max_intentos-1:
            print("Perdiste! El número que pensé fue el:", secreto)
            partida_ganada = False
            seguir_jugando(partida_ganada)
            break
        else:
            print(mayor_menor(intento, secreto))
            cant_intentos += 1
        intento = int(input(mensaje))
    else:
        print('Adivinaste!')
    

def mayor_menor(intento, secreto):
    if intento > secreto:
        result = "Más chico!"
    elif intento < secreto:
        result = "Más grande!"
    return result


def seguir_jugando(partida_ganada):
    eleccion = input("¿Desea seguir jugando? :   S / N")
    eleccion = eleccion.upper()

    if eleccion == "S":
        partida_ganada == False
        