### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Alvaro", "Moreno", 24

# Imprime un mensaje personalizado en la consola
# Utiliza el método format() para insertar los valores de las variables
# en las posiciones indicadas por las llaves {}
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

# Imprime el mismo mensaje, pero utilizando la sintaxis de formateo
# con el operador % (más antigua)
# %s se usa para insertar cadenas, %d para números enteros, %f para números decimales
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

# Imprime un mensaje personalizado utilizando f-strings.
# Las llaves {} permiten insertar el valor de las variables directamente
# en la cadena de texto.
# f-strings ofrecen una forma concisa y legible de formatear cadenas en Python.
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

# La sintaxis general del slicing es [start:end:step]. Los valores por defecto son:
# start: 0 (inicio de la secuencia)
# end: longitud de la secuencia (fin de la secuencia)
# step: 1 (tomar cada elemento)

language_slice = language[0:6:2]
print(language_slice)

# Reverse
# Para imprimir la palabra al reves
reversed_language = language[::-1]
print(reversed_language)

# Funciones

# Pone la primera letra en mayúscula
print(language.capitalize())

# Pone la palabra en mayúscula
print(language.upper())

# Cuenta la cantidad de veces que aparece en la palabra la letra que le indiques
print(language.count("t"))

# Comprueba si es un número, devuelve boolean
print(language.isnumeric())

# Pasa a minuscula la palabra
print(language.lower())

# Comprueba si comienza con lo que le indiques, devuelve boolean
print(language.startswith("P"))







