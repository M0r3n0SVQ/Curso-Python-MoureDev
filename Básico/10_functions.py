# Definición de una función simple llamada my_function
def my_function():
    print("Esto es una función")  # Imprime un mensaje cuando se llama a la función
    
# Llamada a la función my_function
my_function()

# Función con parámetros de entrada (también llamados argumentos)
def sum_two_values(first_value, second_value):
    # Imprime la suma de first_value y second_value
    print(first_value + second_value)
    
# Llamadas a la función sum_two_values con diferentes tipos de argumentos
sum_two_values(5, 7)  # Imprime: 12
sum_two_values(54754, 71231)  # Imprime: 125985
sum_two_values("5", "7")  # Imprime: 57 (concatena las cadenas)
sum_two_values(1.4, 5.2)  # Imprime: 6.6

# Función con parámetros de entrada y retorno de valor
def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value  # Suma los dos valores
    return my_sum  # Devuelve el resultado de la suma

# Llamada a la función sum_two_values y asignación del resultado a my_result
my_result = sum_two_values(1.4, 5.2)  # Esta función solo imprime, no retorna valor
print(my_result)  # Imprime: None, porque sum_two_values no retorna nada

# Llamada a la función sum_two_values_with_return y asignación del resultado a my_result
my_result = sum_two_values_with_return(10, 5)
print(my_result)  # Imprime: 15

# Función con parámetros de entrada pasados por clave (keyword arguments)
def print_name(name, surname):
    # Imprime el nombre y apellido concatenados
    print(f"{name} {surname}")

# Llamada a la función print_name pasando los argumentos por clave
print_name(surname="Moreno", name="Alvaro")  # Imprime: Alvaro Moreno

# Función con parámetros de entrada, uno de ellos con valor por defecto
def print_name_with_default(name, surname, alias="Sin alias"):
    # Imprime el nombre, apellido y alias (si no se proporciona alias, usa el valor por defecto)
    print(f"{name} {surname} {alias}")

# Llamada a la función sin proporcionar el tercer argumento, se usa el valor por defecto
print_name_with_default("Alvaro", "Moreno")  # Imprime: Alvaro Moreno Sin alias

# Llamada a la función proporcionando todos los argumentos
print_name_with_default("Alvaro", "Moreno", "m0r3noSVQ")  # Imprime: Alvaro Moreno m0r3noSVQ

# Función con parámetros de entrada arbitrarios (cantidad variable de argumentos)
def print_upper_texts(*texts):
    # Recorre cada argumento en texts y lo imprime en mayúsculas
    for text in texts:
        print(text.upper())
    
# Llamada a la función con varios argumentos
print_upper_texts("Hola", "Python", "M0r3n0SVQ")
# Imprime:
# HOLA
# PYTHON
# M0R3N0SVQ

