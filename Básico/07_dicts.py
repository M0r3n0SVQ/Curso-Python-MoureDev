# Creación de un diccionario vacío utilizando la función dict()
my_dict = dict()

# Creación de un diccionario vacío utilizando llaves {}
my_other_dict = {}

# Imprime el tipo de dato de my_dict, que es un diccionario (dict)
print(type(my_dict))  # <class 'dict'>

# Imprime el tipo de dato de my_other_dict, que también es un diccionario (dict)
print(type(my_other_dict))  # <class 'dict'>

# Asignación de valores a my_other_dict. Se está creando un diccionario con varias claves y valores.
my_other_dict = {"Nombre":"Alvaro", "Apellido":"Moreno", "Edad":24, 1:"Python"}

# Creación de un nuevo diccionario my_dict con varios tipos de valores, incluyendo un conjunto (set) y un número.
my_dict = {
    "Nombre":"Alvaro",             # Clave "Nombre" con valor "Alvaro"
    "Apellido":"Moreno",           # Clave "Apellido" con valor "Moreno"
    "Edad":24,                     # Clave "Edad" con valor 24
    "Lenguaje":{"Python", "Swift", "Kotlin"},  # Clave "Lenguaje" con valor un conjunto de lenguajes
    1:1.77                         # Clave 1 con valor 1.77
    }

# Imprime el diccionario my_dict con todas sus claves y valores
print(my_dict)

# Imprime el diccionario my_other_dict con todas sus claves y valores
print(my_other_dict)

# Imprime el valor asociado con la clave "Nombre" en my_dict, que en este caso es "Alvaro"
print(my_dict["Nombre"])  # Alvaro

# Cambia el valor asociado con la clave "Nombre" a "Pedro"
my_dict["Nombre"] = "Pedro"

# Imprime el nuevo valor de la clave "Nombre", que ahora es "Pedro"
print(my_dict["Nombre"])  # Pedro

# Imprime el valor asociado con la clave 1 en my_dict, que es 1.77
print(my_dict[1])  # 1.77

# Agrega una nueva clave "Calle" con el valor "Calle Alberche" a my_dict
my_dict["Calle"] = "Calle Alberche"

# Imprime el diccionario my_dict con la nueva clave "Calle" añadida
print(my_dict)

# Elimina la clave "Calle" del diccionario my_dict
del my_dict["Calle"]

# Imprime el diccionario my_dict después de eliminar la clave "Calle"
print(my_dict)

# Verifica si la clave "Nombre" existe en my_dict. Devuelve True si existe, False si no.
print("Nombre" in my_dict)  # True

# Imprime todos los pares clave-valor de my_dict como una vista de elementos
print(my_dict.items())

# Imprime todas las claves de my_dict como una vista de claves
print(my_dict.keys())

# Imprime todos los valores de my_dict como una vista de valores
print(my_dict.values())

# Creación de una lista llamada my_list con diferentes tipos de elementos
my_list = ["Nombre", 1, "Piso"]

# Crea un nuevo diccionario my_new_dict con las claves de my_list y valores None
my_new_dict = dict.fromkeys(my_list)

# Imprime el nuevo diccionario, todas las claves tienen el valor None
print(my_new_dict)

# Crea un nuevo diccionario my_new_dict usando una tupla como claves, con valores None
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))

# Imprime el nuevo diccionario, todas las claves tienen el valor None
print((my_new_dict))

# Crea un nuevo diccionario my_new_dict con las mismas claves que my_dict, pero con valores None
my_new_dict = dict.fromkeys(my_dict)

# Imprime el nuevo diccionario, todas las claves de my_dict están en my_new_dict con valores None
print(my_new_dict)

# Crea un nuevo diccionario my_new_dict con las claves de my_dict y el mismo valor "AlvaroMoreno"
my_new_dict = dict.fromkeys(my_dict, "AlvaroMoreno")

# Obtiene una vista de los valores del diccionario my_new_dict
my_values = my_new_dict.values()

# Imprime el tipo de dato de my_values, que es dict_values
print(type(my_values))  # <class 'dict_values'>

# Imprime los valores del diccionario my_new_dict
print(my_new_dict.values())

# Convierte los valores de my_new_dict en una lista, luego crea un diccionario usando estos valores como claves.
# Luego convierte las claves de este nuevo diccionario en una lista y la imprime.
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))

# Convierte las claves de my_new_dict en una tupla y la imprime
print(tuple(my_new_dict))

# Convierte las claves de my_new_dict en un conjunto y lo imprime
print(set(my_new_dict))

