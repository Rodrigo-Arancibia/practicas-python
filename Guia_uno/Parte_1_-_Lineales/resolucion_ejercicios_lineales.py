
# Módulos built-in
import math

#---------- DECLARACIÓN DE FUNCIONES ----------#

# >>>> Ejercicio 1:
# Permita ingresar dos números y mostrar el resultado de su suma.

def ejercicio_1():
    print("::: 1. Suma de dos números :::")
    primer_numero = int(input("Ingrese el primer número (entero): "))
    segundo_numero = int(input("Ingrese el segundo número (entero): "))
    suma = primer_numero + segundo_numero
    print(">>> La suma de los números ingresados es: " + str(suma))




# >>>> Ejercicio 2:
# Permita ingresar un número y mostrar su cuadrado.

def ejercicio_2():
    print("::: 2. Cuadrado de un número :::")
    numero_ingresado = int(input("Ingrese un número entero: "))
    cuadrado = numero_ingresado ** 2
    print(">>> El cuadrado del número ingresado es: " + str(cuadrado))




# >>>> Ejercicio 3:
# Permita ingresar dos números (A y B) e informar el resultado del producto
# (A*B), la suma (A + B) y la resta (A - B).

def ejercicio_3():
    print("::: 3. Producto, Suma y Diferencia :::")
    numero_A = int(input("Ingrese el primer número (entero) para 'A': "))
    numero_B = int(input("Ingrese el segundo número (entero) para 'B': "))
    
    producto = numero_A * numero_B
    suma = numero_A + numero_B
    resta = numero_A - numero_B

    print(">>> A x B: " + str(producto))
    print(" ")
    print(">>> A + B: " + str(suma))
    print(" ")
    print(">>> A - B: " + str(resta))




# >>>> Ejercicio 4:
# Ingresar dos números y mostrar el resultado del cociente utilizando al primero
# como numerador y al segundo como denominador.

def ejercicio_4():
    print("::: 4. Cociente de dos números :::")
    numerador = int(input("Ingrese el primer número (entero) como numerador: "))
    denominador = int(input("Ingrese el segundo número (entero) como denominador: "))

    cociente = numerador/denominador
    
    # Redondeo de decimales -> método round(valor, cant_decimales)
    print(">>> Cociente: " + str(round(cociente, 2)))




# >>>> Ejercicio 5:
# Inicialice las variables N con un valor entero, A con un valor float y C y J con
# cadenas de texto. Y muestre por pantalla: el valor de cada variable, la suma
# de N + A, la diferencia de A - N y la suma (concatenación) de C + J.

def ejercicio_5():
    print("::: 5. Valores númericos y concatenación de textos :::")
    N = 6
    A = 3.5
    C, J = "Hola", "Chau"

    print("Valor de 'N': " + str(N))
    print("Valor de 'A': " + str(A))
    print("Valor de 'J': " + J)
    print("Valor de 'C': " + C)

    suma_N_y_A = N + A
    resta_A_y_N = A - N
    concat_C_y_J = C + J

    print(">>> N + A = " + str(suma_N_y_A))
    print(">>> A - N = " + str(resta_A_y_N))
    print(">>> Concatenación de C y J: " + concat_C_y_J)




# >>>> Ejercicio 6:
# Inicialice las variables X e Y con valores enteros y las variables N y M con
# valores float. Y muestre por pantalla el valor de: (X + Y) - N, (X*Y) / (N + M),
# X 2 + Y 3.

def ejercicio_6():
    print("::: 6. Mostrando operaciones con N, M, X, Y :::")
    X, Y = 3, 9
    N, M = 3.9, 9.3

    primera_op = (X + Y) - N
    segunda_op = (X + Y) / (N + M)
    tercera_op = X** 2 + Y ** 2

    print(">>> (X + Y) - N = " + str(primera_op))
    print(">>> (X + Y) / (N + M) = " + str(round(segunda_op, 2)))
    print(">>> X ^ 2  +  Y ^ 2 = " + str(tercera_op))




# >>>> Ejercicio 7:
# Declare la variable N con un valor entero. A continuación, incremente N en
# 77, decremente N en 3 y duplique su valor.

def ejercicio_7():
    print("::: 7. Mostrando N modificado :::")
    N = 99
    N = (N + 77 - 3) * 2

    print(">>> Resultado: " + str(N))




# >>>> Ejercicio 8:
# Declare cuatro variables A, B, C y D y le asigne un valor entero a cada una. A
# continuación, realiza las instrucciones necesarias para que: B tome el valor
# de C, C tome el valor de A, A tome el valor de D, D tome el valor de B.

def ejercicio_8():
    print("::: 8. Intercambiando números :::")
    A, B, C, D = 1, 2, 3, 4
    
    var_aux_A = A
    var_aux_B = B
    
    A = D
    B = C
    C = var_aux_A
    D = var_aux_B

    print("'A' = " + str(A))
    print("'B' = " + str(B))
    print("'C' = " + str(C))
    print("'D' = " + str(D))




# >>>> Ejercicio 9:
# Lea un nombre por teclado y muestre por pantalla:
# “Buen día {nombre_ingresado}”.

def ejercicio_9():
    print("::: 9. Imprimiendo tu nombre :::")
    nombre_ingresado = input("Ingrese su nombre: ")
    print("Buen día, {}".format(nombre_ingresado))




# >>>> Ejercicio 10:
# Lea un número entero por teclado y obtenga y muestre por pantalla el doble y
# el triple de ese número.

def ejercicio_10():
    print("::: 10. Mostrando doble y triple del número :::")
    numero_ingresado = int(input("Ingrese un número entero: "))

    doble = numero_ingresado * 2
    triple = numero_ingresado * 3

    print("El doble de " + str(numero_ingresado) + " es: " + str(doble))
    print("El triple de " + str(numero_ingresado) + " es: " + str(triple))




# >>>> Ejercicio 11:
# Lea una cantidad de grados centígrados y la pase a grados Fahrenheit. La
# fórmula correspondiente es: F = 32 + (9 * C / 5).

def ejercicio_11():
    print("::: 11. Mostrando la temperatura en °F :::")
    # Grados Centrigrados ("C"):
    C = float(input("Ingrese la temperatura en grados centígrados: "))

    # Conversión a grados Fahrenheit:
    F = 32 + (9 * C / 5)

    print("Temperatura: " + str(F) + " grados Fahrenheit")




# >>>> Ejercicio 12:
# Lea por teclado el valor del radio de una circunferencia y calcule y muestre
# por pantalla la longitud del perímetro y el área de la circunferencia.
# Perímetro: 2 * PI * radio. Área: PI * radio 2

# OBSERVACIÓN: Para ejecutar este ejercicio hay que importar el módulo
# "math" (código: import math).

# math.pow(r, 2) = r ** 2. Redondeo de decimales -> método round(valor, cant_decimales)

def ejercicio_12():
    print("::: 12. Perímetro y Área de un círculo :::")
    r = float(input("Ingrese el radio de la circunferencia: "))
    p = 2 * math.pi * r
    a = math.pi * math.pow(r, 2)

    print(" ")
    print("Perímetro: " + str(round(p, 3)))
    print("Área: " + str(round(a, 3)))




# >>>> Ejercicio 13:
# Pase una velocidad en Km/h a m/s. La velocidad se lee por teclado.

def ejercicio_13():
    print("::: 13. Convirtiendo velocidad a m/s :::")
    vel_k_h = float(input("Ingrese la velocidad (en Km/h): "))

    vel_m_s = vel_k_h * (1000/3600)

    print("Velocidad en m/s: " + str(round(vel_m_s, 3)))




# >>>> Ejercicio 14:
# Lea la longitud de los catetos de un triángulo rectángulo y calcule la longitud
# de la hipotenusa según el teorema de Pitágoras.

def ejercicio_14():
    print("::: 14. Hallando la hipotenusa :::")
    cateto_A = float(input("Ingrese la longitud del cateto 'A': "))
    cateto_B = float(input("Ingrese la longitud del cateto 'B': "))
    
    # Una forma: hipotenusa = (cateto_A ** 2 + cateto_B ** 2) ** (1/2)
    # Otra forma: También se puede utilizando el metodo "sqrt()" ("square root") del módulo math de Python, así:
    hipotenusa = math.sqrt(cateto_A ** 2 + cateto_B ** 2)
    
    print(">>> Hipotenusa: " + str(round(hipotenusa, 3)))


#--------------------------------------#