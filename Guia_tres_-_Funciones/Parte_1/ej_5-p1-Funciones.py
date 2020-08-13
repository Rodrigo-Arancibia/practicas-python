# 5. Función que reciba un número arbitrario de argumentos posicionales e imprima la longitud de
# cada uno.

def ejercicio_5(*args):
	for x in args:
		print(len(x))	# Imprimo la cantidad de argumentos.

ejercicio_5("4,5,6,7", "rodri", "ho,l,a")