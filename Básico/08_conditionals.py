# Inicializa la variable my_condition con el valor False
my_condition = False 

# Condicional if: Si my_condition es True, se ejecuta el bloque de código dentro del if
if my_condition:
    print("Se ejecuta la condición del if")
# En este caso, no se imprime nada porque my_condition es False

# Asigna a my_condition el resultado de 5 * 5, que es 25
my_condition = 5 * 5

# Condicional if, elif, else

# Verifica si my_condition es igual a 10
if my_condition == 10:
    print("Se ejecuta la condición del segundo if")
# En este caso, no se ejecuta porque my_condition es 25

# Verifica si my_condition es mayor que 10 y menor que 20
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
# En este caso, no se ejecuta porque my_condition es 25

# elif: Si la condición anterior no se cumple, verifica si my_condition es igual a 25
elif my_condition == 25:
    print("Es igual a 25")
# Este bloque sí se ejecuta porque my_condition es 25

# else: Si ninguna de las condiciones anteriores se cumple, se ejecuta este bloque
else:
    print("Es menor o igual que 10 o mayor o igual que 20")
# En este caso, no se ejecuta porque la condición del elif fue verdadera

# Este print se ejecuta independientemente de las condiciones anteriores
print("La ejecución continúa")

# Condicional con inspección de valor

# Inicializa la variable my_string con una cadena vacía
my_string = ""

# if not: Verifica si my_string es una cadena vacía o tiene un valor evaluado como False
if not my_string:
    print("Mi cadena de texto es vacía")
# Este bloque se ejecuta porque my_string es una cadena vacía (que se evalúa como False)

# Verifica si my_string es exactamente igual a "Mi cadena de textooooo"
if my_string == "Mi cadena de textooooo":
    print("Estas cadenas de texto coinciden")
# Este bloque no se ejecuta porque my_string es una cadena vacía, no "Mi cadena de textooooo"
