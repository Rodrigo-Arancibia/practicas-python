
# ::::::::  p3: DICCIONARIOS  ::::::::

# >>>> Ejercicio 2:

# Escribir un programa que utilice el diccionario anterior y que le permita al
# usuario consultar por teclado la nota de una materia. Si la materia no existe,
# mostrar un mensaje indicando que aún no se rindió.

print("::: 2. Consultando materias y notas :::")

materias = {"Lógica y Estructura de Datos": 10,
"Ingeniería de Software 1": 10,
"Sistemas operativos": 10}

materia_consultada = input("Ingrese una materia: ")

print(materias.get(materia_consultada, "Aún no se rindió."))