
# ::::::::  p1: LISTAS Y TUPLAS  ::::::::

# >>>> Ejercicio 5:

# Escribir un programa que le pida al usuario por teclado las materias que ya
# rindió y la nota obtenida. Guardar la información en una estructura como en la
# del punto anterior y mostrar los mismos mensajes. Tip: usar while e input.

print("::: 5. Ingresando mis notas :::")

materias = []

materia = input("Materia: ")
nota = input("Nota: ")

par = (materia, nota)
print(par)
# Mientras no le de Enter cuando me pida el nombre de materia voy a poner tuplas
# en la lista. O sea que si doy enter es porque quiero dejar de ingresar tuplas con materia y nota.
while materia and nota:
    par = (materia, nota)
    materias.append(par)
    
    materia = input("Materia: ")
    nota = input("Nota: ")

else:
    for m in materias:
        print("Rendí " + m[0] + " con " + m[1])