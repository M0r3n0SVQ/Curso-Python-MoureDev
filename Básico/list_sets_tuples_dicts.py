# Listas
# - Mutable: Puedes cambiar los elementos después de crear la lista
# - Permite duplicados
# - Ordenada: Mantiene el orden de inserción
# - Sintaxis: []

lista = [1, 2, 3, 4, 4]
lista.append(5)  # Agrega un elemento al final
lista[0] = 10   # Modifica un elemento
print(lista)  # Salida: [10, 2, 3, 4, 4, 5]

# Tuplas
# - Inmutable: No puedes cambiar los elementos después de crear la tupla
# - Permite duplicados
# - Ordenada: Mantiene el orden de inserción
# - Sintaxis: ()

tupla = (1, 2, 3, 4, 4)
# tupla[0] = 10  # Esto generará un error porque las tuplas son inmutables
print(tupla)  # Salida: (1, 2, 3, 4, 4)

# Conjuntos (Sets)
# - Mutable: Puedes agregar o eliminar elementos
# - No permite duplicados
# - No ordenada: No mantiene el orden de inserción
# - Sintaxis: {} o set()

conjunto = {1, 2, 3, 4, 4}  # Los duplicados serán eliminados
conjunto.add(5)  # Agrega un elemento
print(conjunto)  # Salida: {1, 2, 3, 4, 5}

# Diccionarios
# - Mutable: Puedes cambiar los valores y las claves después de crear el diccionario
# - Claves únicas: No permite claves duplicadas, pero los valores pueden duplicarse
# - Ordenado (en versiones de Python 3.7 y posteriores): Mantiene el orden de inserción
# - Sintaxis: {clave: valor}

diccionario = {'a': 1, 'b': 2, 'c': 3}
diccionario['d'] = 4  # Agrega un nuevo par clave-valor
diccionario['a'] = 10  # Modifica un valor existente
print(diccionario)  # Salida: {'a': 10, 'b': 2, 'c': 3, 'd': 4}
