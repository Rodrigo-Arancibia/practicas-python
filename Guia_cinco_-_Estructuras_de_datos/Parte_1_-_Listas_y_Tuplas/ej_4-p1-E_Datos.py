
# ::::::::  p1: LISTAS Y TUPLAS  ::::::::

# >>>> Ejercicio 4:

# En el programa anterior definir la variable nombre y usando for imprimir
# tantos mensajes como materias haya en la lista: “Mi nombre es <nombre> y
# aprobé <materia> con <nota>”.

print("::: 4. Mi nombre y mis notas :::")

nombre = input("Ingrese su nombre: ")

rendidas = [("Lógica y Estructura de Datos", 10),
("Ingeniería de Software 1", 10),
("Sistemas operativos", 10)]

for x in rendidas:
    print("Mi nombre es " + nombre + " y aprobé " + x[0] + " con", str(x[1]))