
# >>>> Ejercicio 14:

# Imprima el siguiente patrón:

# ++++++++++
# ++++++++
# ++++++
# ++++
# ++

# Función range(x, y, z):
# 
# x = punto de comienzo
# 
# y = punto de finalización. Siempre este punto es y-1
# (una unidad antes de lo especificado en el parámetro 'y').
# 
# z = Tamaño del paso de la secuencia.
# 
for x in range(10, 0, -2):
    print("+" * x)