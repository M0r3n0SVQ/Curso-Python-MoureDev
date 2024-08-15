# Asignación de valores a las variables
numberOne = 5
numberTwo = 1
numberTwo = "1"  # Aquí numberTwo se convierte en una cadena ("1")

# Bloque try-except para manejar excepciones
try:
    # Intenta sumar numberOne y numberTwo (un entero y una cadena)
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: 
    # Este bloque se ejecuta si ocurre una excepción (cualquier tipo de error)
    print("Se ha producido un error")

# Bloque try-except-else-finally
try:
    # Intenta sumar numberOne y numberTwo
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: 
    # Este bloque se ejecuta si ocurre una excepción
    print("Se ha producido un error")
else:
    # Este bloque se ejecuta solo si NO se produce ninguna excepción
    print("La ejecución continúa correctamente")
finally:  # Este bloque es opcional
    # Este bloque se ejecuta siempre, independientemente de si hubo o no una excepción
    print("La ejecución continúa")

# Manejo de excepciones específicas por tipo
try:
    # Intenta sumar numberOne y numberTwo
    print(numberOne + numberTwo)
    print("No se ha producido un error")
    
except ValueError:
    # Este bloque se ejecuta si ocurre una excepción de tipo ValueError
    print("Se ha producido un ValueError")
    
except TypeError:
    # Este bloque se ejecuta si ocurre una excepción de tipo TypeError
    print("Se ha producido un TypeError")

# Captura de la información de la excepción
try:
    # Intenta sumar numberOne y numberTwo
    print(numberOne + numberTwo)
    print("No se ha producido un error")
    
except ValueError as eV:
    # Captura la excepción ValueError y la guarda en la variable eV
    print(eV)  # Imprime la información del error
    print("Se ha producido un ValueError")
    
except Exception as my_random_error_name:
    # Captura cualquier otra excepción y la guarda en la variable my_random_error_name
    print(my_random_error_name)  # Imprime la información del error
