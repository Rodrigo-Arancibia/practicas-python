
# ::::::::  p1: LISTAS Y TUPLAS  ::::::::

# >>>> Ejercicio 5:

# Escribir un programa que le pida al usuario por teclado las materias que ya
# rindió y la nota obtenida. Guardar la información en una estructura como en la
# del punto anterior y mostrar los mismos mensajes. Tip: usar while e input.

print("::: 5. Ingresando mis notas :::")

materia = input("Materia: ")

rendidas = []

# Mientras no le de enter cuando me pida el nombre de materia voy a poner tuplas
# en la lista. O sea que si doy enter es porque quiero dejar de ingresar tuplas con materia y nota.
while materia is not "":
    nota = int(input("Nota: "))
    tupla = tuple([materia, nota])
    rendidas.append(tupla)
    materia = input("Materia: ")

    for x in rendidas:
        print("Materia:", x[0], ". Nota:", x[1])