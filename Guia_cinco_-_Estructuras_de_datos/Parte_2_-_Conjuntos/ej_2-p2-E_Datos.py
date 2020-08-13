
# ::::::::  p2: CONJUNTOS  ::::::::

# >>>> Ejercicio 2:

# Dadas la listas:
# autores_argentinos = ["Borges", "Saer", "Cortazar", "Piglia", "Kohan", "Fogwill", "Casas"]
#
# autores_extranjeros = ["Joyce", "Poe", "Child", "Carver", "Chandler", "Coetze", "Auster"]
#
# autores_vivos = ["Casas", "Kohan", "Child", "Coetze", "Auster"]
#
# Encontrar la lista autores argentinos vivos. ¿Qué operación usó?
# Encontrar la lista de autores muertos. ¿Qué operación usó?

print("::: 2. Autores de libros :::")

autores_argentinos = ["Borges", "Saer", "Cortazar", "Piglia", "Kohan", "Fogwill", "Casas"]

autores_extranjeros = ["Joyce", "Poe", "Child", "Carver", "Chandler", "Coetze", "Auster"]

autores_vivos = ["Casas", "Kohan", "Child", "Coetze", "Auster"]

conj_autores_argentinos = set(autores_argentinos)
conj_autores_extranjeros = set(autores_extranjeros)
conj_autores_vivos = set(autores_vivos)

# 1. Encontrar la lista autores argentinos vivos. ¿Qué operación usó?
    # Usamos la operación de INTERSECCIÓN entre conjuntos.
conj_autores_argentinos_vivos = conj_autores_argentinos & conj_autores_vivos

# Me pide una 'lista' entonces tengo que convertir el conjunto en una lista,
# usando la función 'list(nombre_del_conj)'
lista_autores_argentinos_vivos = list(conj_autores_argentinos_vivos)
print("Autores argentinos vivos:", lista_autores_argentinos_vivos)

# 2. Encontrar la lista de autores muertos. ¿Qué operación usó?
conj_autores_muertos = (conj_autores_argentinos | conj_autores_extranjeros) - conj_autores_vivos

# Me pide una 'lista' entonces tengo que convertir el conjunto en una lista,
# usando la función 'list(nombre_del_conj)'
lista_autores_muertos = list(conj_autores_muertos)
print("Autores muertos:", lista_autores_muertos)