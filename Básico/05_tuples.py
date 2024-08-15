# Definición

my_tuple = tuple()  # Crea una tupla vacía
my_other_tuple = ()  # Otra forma de crear una tupla vacía

# Crear tuplas con elementos
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

# Imprimir la tupla y su tipo
print(my_tuple)  # Imprime todos los elementos de la tupla
print(type(my_tuple))  # Imprime <class 'tuple'>

# Acceso a elementos

print(my_tuple[0])  # Imprime el primer elemento
print(my_tuple[-1])  # Imprime el último elemento
# print(my_tuple[4])  # Genera un error IndexError porque no existe el índice 4
# print(my_tuple[-6])  # Genera un error IndexError porque no existe el índice -6

# Contar elementos y buscar índice
print(my_tuple.count("Brais"))  # Cuenta cuántas veces aparece "Brais"
print(my_tuple.index("Moure"))  # Devuelve el índice de "Moure"
print(my_tuple.index("Brais"))  # Devuelve el primer índice de "Brais"

# Modificar elementos (no permitido)
# my_tuple[1] = 1.80  # Genera un error 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple  # Une las dos tuplas en una nueva
print(my_sum_tuple)

# Subtuplas

print(my_sum_tuple[3:6])  # Imprime una subtupla desde el índice 3 hasta el 5 (exclusivo)

# Convertir a lista para modificación

mutable_list = list(my_tuple)  # Convierte la tupla a una lista mutable
print(type(mutable_list))  # Imprime <class 'list'>

mutable_list[4] = "MoureDev"  # Modifica un elemento de la lista
mutable_list.insert(1, "Azul")  # Inserta un elemento en la lista

# Convertir la lista modificada de nuevo a tupla
my_tuple = tuple(mutable_list)
print(my_tuple)
print(type(my_tuple))  # Imprime <class 'tuple'>

# Eliminación (no se puede eliminar directamente)
# del my_tuple[2]  # Genera un error TypeError: 'tuple' object doesn't support item deletion

# Eliminar la tupla por completo
del my_tuple
# print(my_tuple)  # Genera un error NameError: name 'my_tuple' is not defined

# Diferencias entre tuplas y listas

# Tuplas: Inmutables, se utilizan para almacenar colecciones ordenadas que no se modificarán.
# Listas: Mutables, se utilizan para almacenar colecciones ordenadas que se pueden modificar.

# En resumen: Las tuplas son como listas fijas, mientras que las listas son dinámicas y permiten modificaciones.
