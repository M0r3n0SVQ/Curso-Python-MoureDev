# Variables

# Forma correcta de crear variables
my_variable = "My String variable"
print(my_variable)

# Variable int
my_int_variable = 5
print(my_int_variable)

#Variable bool
my_bool_variable = False
print(my_bool_variable)

#Concatenación variables en un print
print(my_variable,my_int_variable,my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Podemos convertir tipos de variables en otra, aquí hemos pasado de int a str, y lo comprobamos con el comando type
my_int_variable_to_str_variable = str(my_int_variable)
print(my_int_variable_to_str_variable)
print(type(my_int_variable_to_str_variable))

# Algunas funciones del sistema
print(len(my_variable))
 
# Variables en una sola línea, no abusar de esta sintaxis
name, surname, alias, age = "Alvaro", "Moreno", "morenobbn", 24
print("Me llamo:",name, surname,". Mi edad es", age, "y mi alias es:", alias)

# Teclado en pantallas
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = 32
# Al introducir nuevo valor de la variable cambia de str a int
print(address)