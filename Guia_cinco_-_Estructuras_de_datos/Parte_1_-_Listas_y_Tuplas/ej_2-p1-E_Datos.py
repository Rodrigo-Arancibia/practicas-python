
# ::::::::  p1: LISTAS Y TUPLAS  ::::::::

# >>>> Ejercicio 2:

# En el programa anterior definir la variable nombre y usando for imprimir
# tantos mensajes como materias haya en la lista: “Mi nombre es <nombre> y
# curso <materia>”.

print("::: 2. Nombre y materia :::")

nombre = input("Ingrese su nombre: ")

materias = ["Comunicación",
"UDI 1",
"Inglés técnico 1",
"Matemática",
"Administración",
"Tecnología de la Información",
"Lógica y Estructura de Datos",
"Ingeniería de Software 1",
"Sistemas operativos"]

for x in materias:
    print("Mi nombre es {}".format(nombre) + " y curso", x)