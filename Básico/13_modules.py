# Importa un módulo completo llamado 'my_module'
import my_module

# Llama a la función 'sumValues' desde el módulo 'my_module'
my_module.sumValues(5, 3, 1)  # Supone que suma los valores y realiza alguna operación

# Llama a la función 'printValue' desde el módulo 'my_module'
my_module.printValue("Hola Python!")  # Imprime el valor proporcionado

# Importa específicamente las funciones 'sumValues' y 'printValue' del módulo 'my_module'
from my_module import sumValues, printValue

# Llama a la función 'sumValues' sin necesidad de usar el prefijo del módulo
sumValues(5, 3, 1)  # De nuevo, suma los valores

# Llama a la función 'printValue' sin necesidad de usar el prefijo del módulo
printValue("Hola Python!")  # Imprime el valor proporcionado

# Importa el módulo 'math', que es parte de la biblioteca estándar de Python
import math

# Imprime el valor de 'pi' utilizando el módulo 'math'
print(math.pi)  # Imprime: 3.141592653589793

# Usa la función 'pow' del módulo 'math' para calcular 2 elevado a la potencia de 8
print(math.pow(2, 8))  # Imprime: 256.0

# Importa específicamente la constante 'pi' del módulo 'math' y la renombra a 'PI_VALUE'
from math import pi as PI_VALUE

# Imprime el valor de 'PI_VALUE', que es el valor de pi
print(PI_VALUE)  # Imprime: 3.141592653589793
