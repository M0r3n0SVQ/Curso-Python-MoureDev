# Definición de listas
# Las listas se crean usando corchetes [] o la función list()
my_list = list()  # Lista vacía
my_other_list = []  # Otra lista vacía

# Obteniendo la longitud de una lista
print(len(my_list))  # Imprime 0, ya que la lista está vacía

# Creando listas con elementos
my_list = [35, 24, 62, 52, 30, 30, 17]
my_other_list = [24, 1.77, "Alvaro", "Moreno"]

# Imprimiendo las listas y su longitud
print(my_list)  # Imprime todos los elementos de la lista
print(len(my_list))  # Imprime la cantidad de elementos

# Verificando el tipo de dato
print(type(my_list))  # Imprime <class 'list'>
print(type(my_other_list))  # Imprime <class 'list'>

# Accediendo a elementos de una lista
print(my_other_list[0])  # Imprime el primer elemento
print(my_other_list[1])  # Imprime el segundo elemento
print(my_other_list[-1])  # Imprime el último elemento
print(my_other_list[-4])  # Imprime el cuarto elemento desde el final
print(my_list.count(30))  # Cuenta cuántas veces aparece el número 30 en la lista
# print(my_other_list[4])  # Genera un error IndexError porque no existe el índice 4
# print(my_other_list[-5])  # Genera un error IndexError porque no existe el índice -5

# Encontrando el índice de un elemento
print(my_other_list.index("Alvaro"))  # Imprime el índice donde se encuentra "Alvaro"

# Desempaquetado de una lista
age, height, name, surname = my_other_list
print(name)  # Imprime "Alvaro"

# Desempaquetado con índices específicos
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)  # Imprime 24

# Concatenación de listas
print(my_list + my_other_list)  # Une las dos listas en una nueva lista

# Creación, inserción, actualización y eliminación de elementos
my_other_list.append("M0r3n0SVQ")  # Agrega un elemento al final
print(my_other_list)
my_other_list.insert(1, "Rojo")  # Inserta un elemento en la posición 1
print(my_other_list)
my_other_list[1] = "Azul"  # Modifica el elemento en la posición 1
print(my_other_list)
my_other_list.remove("Azul")  # Elimina el primer elemento con el valor "Azul"
print(my_other_list)
my_list.remove(30)  # Elimina el primer elemento con el valor 30
print(my_list)
print(my_list.pop())  # Elimina y devuelve el último elemento
print(my_list)
my_pop_element = my_list.pop(2)  # Elimina y devuelve el elemento en la posición 2
print(my_pop_element)
print(my_list)
del my_list[2]  # Elimina el elemento en la posición 2
print(my_list)

# Operaciones con listas
my_new_list = my_list.copy()  # Crea una copia de la lista
my_list.clear()  # Vacía la lista
print(my_list)
print(my_new_list)
my_new_list.reverse()  # Invierte el orden de los elementos
print(my_new_list)
my_new_list.sort()  # Ordena los elementos
print(my_new_list)

# Sublistas
print(my_new_list[1:3])  # Imprime una sublista desde el índice 1 hasta el 2 (exclusivo)

# Cambio de tipo (no se puede hacer directamente)
my_list = "Hola Python"  # Esto crea un string, no una lista
print(my_list)
print(type(my_list))
