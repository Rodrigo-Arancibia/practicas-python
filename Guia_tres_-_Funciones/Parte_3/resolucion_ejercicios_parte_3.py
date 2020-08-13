# Modificar las funciones (solo el cuerpo de las funciones) para que ejecuten correctamente:

# A continuación la resolución de los ejercicios:

def ejercicio_1():
    
    print(">>  Ejercicio 1:  <<")
    
    def circulo():
        radio = float(input("Radio: "))
        area = 3.4 * radio ** 2
        print("El area de un círculo de radio", radio, "es", round(area, 2))
        print("")

    circulo()



def ejercicio_2():
    
    print(">>  Ejercicio 2:  <<")

    def get_alumnos():
        return ["Rodrigo", "Maia", "Leandro", "Mariano"]

    def saludar(nombre):
        return "Hola " + nombre

    def saludar_a_todos():
        for x in get_alumnos():
            print(saludar(x))
        print("")
    
    print(saludar("Lucas"))
    saludar_a_todos()



def ejercicio_3():

    print(">>  Ejercicio 3:  <<")

    def nombre_producto(bicho):
        return "mata-" + bicho

    print(nombre_producto("hormigas"))
    print(nombre_producto("cucarachas"))
    print(nombre_producto("moscas"))
    print("")



def ejercicio_4():

    print(">>  Ejercicio 4:  <<")
    
    def remedio_natural(enfermedad):
        if enfermedad == "resfrio":
            return "té con limón"
        elif enfermedad == "dolor de garganta":
            return "té con miel"
        elif enfermedad == "dolor de panza":
            return "té de hojas de durazno"
        else:
            return "no tengo remedio para eso."

    print(remedio_natural("resfrio"))
    print(remedio_natural("dolor de garganta"))
    print(remedio_natural("dolor de panza"))
    print(remedio_natural("dolor de muela"))    # Retorna: "No tengo remedio para eso."