# Inicializa la variable my_condition con 0
my_condition = 0    

# Bucle while: Se ejecuta mientras la condición my_condition < 10 sea True
while my_condition < 10:
    print(my_condition)  # Imprime el valor actual de my_condition
    my_condition += 2  # Incrementa my_condition en 2 en cada iteración
# Cuando my_condition no cumple la condición (< 10), se ejecuta el bloque else
else:  # El bloque else es opcional y se ejecuta cuando el while termina normalmente
    print("Mi condición es mayor o igual que 10")
    
# Este print se ejecuta después de que el while termina
print("La ejecución continúa")

# Bucle while: Se ejecuta mientras la condición my_condition < 20 sea True
while my_condition < 20:
    my_condition += 1  # Incrementa my_condition en 1 en cada iteración
    if my_condition == 15:  # Verifica si my_condition es igual a 15
        print("Se detiene la ejecución")
        break  # Si es igual a 15, se rompe el bucle con break
    print(my_condition)  # Imprime my_condition si no se rompe el bucle
    
# Este print se ejecuta después de que el while termina o se rompe
print("La ejecución continúa")

# Bucle for: Itera sobre cada elemento en la lista my_list
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)  # Imprime cada elemento de la lista

# Bucle for: Itera sobre cada elemento en la tupla my_tuple
my_tuple = (25, 1.77, "Alvaro", "Moreno")

for element in my_tuple:
    print(element)  # Imprime cada elemento de la tupla

# Bucle for: Itera sobre cada elemento en el conjunto my_set
my_set = {"Alvaro","Moreno", 24}

for element in my_set:
    print(element)  # Imprime cada elemento del conjunto

# Bucle for: Itera sobre cada clave en el diccionario my_dict
my_dict = {"Nombre":"Alvaro", "Apellido":"Moreno", "Edad":24, 1:"Python"}

for element in my_dict:
    print(element)  # Imprime cada clave del diccionario
    if element == "Edad":  # Verifica si la clave actual es "Edad"
        break  # Si es así, rompe el bucle
else:
    # Este bloque else no se ejecutará porque el bucle fue interrumpido con break
    print("El bucle for para diccionario ha finalizado")
    
# Este print se ejecuta después del bucle for
print("La ejecución continúa")

# Bucle for: Itera sobre cada clave en el diccionario my_dict nuevamente
for element in my_dict:
    print(element)  # Imprime cada clave del diccionario
    if element == "Edad":  # Verifica si la clave actual es "Edad"
        continue  # Si es así, salta el resto del ciclo y continúa con la siguiente iteración
    print("Se ejecuta")  # Este print se ejecuta solo si la clave no es "Edad"
else:
    # Este bloque else se ejecuta porque el bucle no fue interrumpido con break
    print("El bucle for para diccionario ha finalizado")
