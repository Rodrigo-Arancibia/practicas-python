# 6. Función que reciba un número arbitrario de argumentos nombrados e
# imprima el nombre y el valor de cada uno.

def ejercicio_6(**kwargs):
    for k,v in kwargs.items():
        print(k, v)

ejercicio_6(nombre_1 = 0, nombre_2 = "hola")