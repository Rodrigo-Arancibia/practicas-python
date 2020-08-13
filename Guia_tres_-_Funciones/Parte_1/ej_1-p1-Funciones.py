# 1. Función que reciba un parámetro radio y lo use para calcular el área de un círculo.

def ejercicio_1():
    
    print(">>  Ejercicio 1:  <<")
    
    radio = float(input("Radio: "))
    area = 3.4 * radio ** 2
    print("El area de un círculo de radio", radio, "es", round(area, 2))