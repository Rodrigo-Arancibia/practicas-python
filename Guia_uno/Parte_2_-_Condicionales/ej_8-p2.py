
# >>>> Ejercicio 8:

# Declare una variable C y le asigne un valor de tipo entero. A continuación,
# muestre un mensaje indicando si el valor de C es positivo o negativo, si es
# par o impar, si es múltiplo de 5, si es múltiplo de 10 y si es mayor o menor
# que 100. Consideraremos el 0 como positivo.

print("::: 8. Analizando el número :::")

C = int(input("Ingrese un número entero: "))

print("El número ingresado es ...")
if C >= 0:
    print("POSITIVO.")
else:
    print("NEGATIVO.")

if C % 2 == 0:
    print("PAR.")
else:
    print("IMPAR.")

if C % 5 == 0:
    print("MÚLTIPLO DE 5.")
else:
    print("NO es múltiplo de 5.")

if C % 10 == 0:
    print("MÚLTIPLO DE 10.")
else:
    print("NO es múltiplo de 10.")

if C > 100:
    print("MAYOR a 100.")
elif C < 100:
    print("MENOR a 100.")
# Lo siguiente el enunciado no lo pide pero se necesita saber si el 100
# se consideraría (en el ejercicio) como mayor o menor que 100.
elif C == 100:
    print("El número no es ni mayor ni menor a 100.... O sea es 100.")