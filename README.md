# Prácticas Python

Este repositorio contiene prácticas hechas por mi tanto como tareas del instituto, como también desarrollos por cuenta propia.


## Organización del repositorio:

Cada directorio puede contar o no con subdirectorios que a su vez estos contienen los módulos Python (archivos.py).

Se organizan de la siguiente manera:



### Directorio: "Guia_uno":

Por favor, para más información referirse al archivo "Requerimientos_Guia_uno.pdf".

Este directorio cuenta con tres subdirectorios de acuerdo a las secciones de ejercicios planteados en el archivo "Requerimientos_Guia_uno.pdf":


#### Sub-directorio "Parte_1_-_Lineales":
Resolución de los ejercicios sin bucles ni condicionales.

#### Sub-directorio "Parte_2_-_Condicionales":
Resolución de los ejercicios con bloques if / else / elif.

#### Sub-directorio "Parte_3_-_Iteracion":
Resolución de los ejercicios con combinación de conocimientos adquiridos en 'Parte 1' y 'Parte 2' más el agregado de bucles for y while.



### Directorio: "Guia_dos".

Por favor, para más información referirse al archivo "Requerimientos_Guia_dos.pdf".

Este directorio cuenta principalmente con dos archivos ".py" para poder desacoplar, por un lado la resolución de los ejercicios mediante la declaración de una función por ejercicio, y por otro lado las llamadas a las funciones que contienen los ejercicios resueltos.

En el archivo "resolucion_ejercicios.py" se encuentra la resolución de todos los ejercicios divididos en funciones.
En el archivo "llamadas_a_funciones.py" se encuentran las llamadas a las funciones.



### Directorio "Guia_tres_-_Funciones:

Este directorio cuenta con tres subdirectorios de acuerdo a distintos tipos de ejercicios planteados, como ser:

#### Sub-directorio "Parte_1":
Por favor, para más información referirse al archivo "Requerimientos_Parte_1_-_Funciones.pdf".

Cuenta con tantos módulos Python como ejercicios hay planteados en el PDF.


#### Sub-directorio "Parte_2":

Por favor, para más información referirse al archivo "Requerimientos_Parte_2_-_Funciones.pdf".

Contiene un juego por niveles, desarrollado en "Python puro", que se juega a través de la línea de comandos sin implementación de ninguna biblioteca al ser un juego muy fácil de resolver con el uso de la mente y debbuging.

Cuenta con dos módulos Python: uno llamado "adivina_adivinador.py" que contiene el programa completo (con la función "main()"). Y el otro módulo llamado "call_adivina_adivinador.py" contiene la llamada a la función "main()" del módulo anteriormente descripto.

- Comentario: Le agregué valor al implementar features adicionales a los requerimientos preestablecidos, como ser:

* **Desacople de funcionalidades**, divididas en funciones para una mejor lectura del código y futuro debbuging e implementaciones adicionales.

* **Jugar por niveles**:
    Posibilidad de incrementar la dificultad del juego automáticamente luego de haber acertado el 'número secreto'. Previamente se le pregunta al usuario si desea seguir jugando. Caso afirmativo, se continúa el juego en el nivel inmediato superior. Caso negativo, se termina la ejecución del programa.
    
    Si el usuario pierde la partida (no adivina el 'número secreto' dentro del número de intentos posibles), se le pregunta si desea seguir jugando. Caso afirmativo, se reinicia el juego en el nivel 1. Caso negativo, se termina la ejecución del programa.
    
    
    
#### Sub-directorio "Parte_3":

Por favor, para más información referirse al archivo "Requerimientos_Parte_3_-_Funciones.py"


#### Sub-directorio "Funciones_ejercicios_extra":

Contiene ejercicios extra para afianzar los conocimientos adquiridos.


#### Sub-directorio "Funciones_recursivas".



### Directorio "Guia_cuatro_-_Excepciones:

Por favor, para más información referirse al archivo "Requerimientos_Guia_cuatro.txt".

Como su nombre lo indica, son ejercicios resueltos aplicando el manejo de excepciones (Try-Catch-Finally) solo a los primeros tres ejercicios de las tres partes del directorio "Guia_uno".


* Es decir:

- Parte 1: Lineales (ejercicios 1 al 3).

- Parte 2: Condicionales (ejercicios 1 al 3).

- Parte 3: Iteracion (ejercicios 1 al 3).

**Por ejemplo**:

**"p1-ej_1.py"**: Parte 1 - ejercicio 1. 
**"p1-ej_2.py"**: Parte 1 - ejercicio 2.
**"p1-ej_3.py"**: Parte 1 - ejercicio 3.

**"p2-ej_1.py"**: Parte 2 - ejercicio 1.
**"p2-ej_1.py"**: Parte 2 - ejercicio 2.

Y así con el resto de archivos de esta carpeta.


### Directorio: "Guia_cinco_-_Estructuras_de_datos":

Por favor, para más información referirse al archivo "Requerimientos_Guia_cinco.pdf".

Como su nombre lo indica, son ejercicios referidos a estructuras de datos en Python, como ser:

- Listas.

- Tuplas.

- Conjuntos.

- Diccionarios.