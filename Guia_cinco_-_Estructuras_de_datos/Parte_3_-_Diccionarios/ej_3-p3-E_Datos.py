
# ::::::::  p3: DICCIONARIOS  ::::::::

# >>>> Ejercicio 3:

# Modificar el programa anterior para que al inicio le pregunte al usuario qué
# desea hacer, si consultar notas o cargar notas. Si elije consultar, el programa
# debe funcionar como en el punto anterior. Si elige cargar, debe permitirle al
# usuario ingresar una materia y a continuación una nota. Permitir que el
# usuario cargue notas para tantas materias como quiera hasta que ingrese
# una cadena vacía como nombre de materia. Si el usuario ingresa una materia
# que ya existe en el diccionario, la nota se debe actualizar.

print("::: 3. Consultando materias y notas :::")


materias = {"Lógica y Estructura de Datos": 10, "Ingeniería de Software 1": 8, "Sistemas operativos": 6}

# Llamo a esta función si el usuario elige la opción "S"
def cargar_nota():
    print(">> Ud eligió cargar una nota.")
    
    materia = input("Materia: ")

    while materia != "":
    # El métogo "get()":
    # Recibe cómo parámetro la clave a buscar en el diccionario.
    # Devuelve: A). "None" si la clave buscada no existe.  B). Si existe, devuelve el valor asociado a esa clave.
        if materias.get(materia) is None:
            materias[materia]
        else:
            print(">> La materia ya existe. La nota se actualizará.")
            nota = input("Nota: ")
            materias[materia] = nota
            print(materia, "ahora tiene la nota:", materias[materia])
        
        print(materias) # Imprimo cómo queda el diccionario después de modificarlo.
        materia = input("Materia: ")
        

opcion = input("¿Qué operación desea realizar? -> C: Consultar notas;   S: Cargar materias con notas. ... ")

opcion = opcion.upper()
if opcion == "C":
    print(">> Ud eligió consultar una materia.")
    materia_consultada = input("Ingrese una materia: ")
    print(materias.get(materia_consultada, "Aún no se rindió."))
elif opcion == "S":
    cargar_nota()   # Llamo a la función para desacoplar más el código para que se entienda mejor.