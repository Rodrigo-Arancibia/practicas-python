# 3. Función que reciba dos parámetros base y altura y los use para
# calcular la superficie de un rectángulo, pero uno de los parámetros tenga un
# valor por defecto. Llamarla una vez con dos argumentos y otra con uno.

def ejercicio_3(base=2, altura=4):
    
    print(">>  Ejercicio 3:  <<")

    resultado = base * altura

    print("Superficie del rectángulo: ", resultado)
    print("")

ejercicio_3()
ejercicio_3(6,8)