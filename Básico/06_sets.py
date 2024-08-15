# Conjuntos (Sets) en Python

# Creación de conjuntos
my_set = set()  # Crea un conjunto vacío
my_other_set = {}  # Inicialmente un diccionario vacío

print(type(my_set))  # Imprime el tipo de dato: <class 'set'>
print(type(my_other_set))  # Inicialmente es un diccionario: <class 'dict'>

# Corrección: Crear un conjunto correctamente
my_other_set = {"Alvaro", "Moreno", 24}
print(type(my_other_set))  # Ahora es un conjunto: <class 'set'>

# Obtener la cantidad de elementos
print(len(my_other_set))  # Imprime la cantidad de elementos en el conjunto

# Agregar un elemento al conjunto
my_other_set.add("m0r3nosvq")
print(my_other_set)  # Imprime el conjunto (los elementos no tienen un orden específico)

# Intentar agregar un elemento duplicado (no hace nada)
my_other_set.add("m0r3nosvq")
print(my_other_set)  # Imprime el conjunto sin duplicados

# Comprobar si un elemento está en el conjunto
print("Alvaro" in my_other_set)  # Imprime True
print("Albaro" in my_other_set)  # Imprime False

# Eliminar un elemento del conjunto
my_other_set.remove("Alvaro")
print(my_other_set)

# Eliminar todos los elementos del conjunto
my_other_set.clear()
print(len(my_other_set))  # Imprime 0

# Eliminar el conjunto de la memoria
del my_other_set

# Convertir un conjunto a una lista (para acceder a elementos por índice)
my_set = {"Alvaro", "Moreno", 24}
my_list = list(my_set)
print(my_list[0])  # Imprime el primer elemento de la lista (no del conjunto)

# Operaciones entre conjuntos
my_other_set = {"Kotlin", "Swift", "Python"}

# Unión de conjuntos (elementos que están en al menos uno de los conjuntos)
my_new_set = my_set.union(my_other_set)
print(my_new_set)

# Diferencia entre conjuntos (elementos que están en el primer conjunto pero no en el segundo)
print(my_new_set.difference(my_set))


