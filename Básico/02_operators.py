### Operadores ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3) # Se acerca al entero por el que se puede dividir
print(2 ** 3) # Calcular exponente

# Sirve para concatenar string, no se puede mezclar int con string directamente, podemos utilizar la funcion str
print("Hola " + "Python")
print("Hola " + str(5))
# El signo * podemos multiplicar un string, mientras que el numero sea un entero
print("Hola " * (3 * 6 - 4))

# Podemos cambiar de float a int con la funcion int
my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
# Se puede comparar cadenas, ordena alfabeticamente por ASCII
print("Hola" >= "Python")
print("aaaa" > "abaa")
# Para comparar numeros de caracteres se utiliza funcion len
print(len("aaaa") < len("bbb"))

### Operadores lógicos ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(not(3 > 4))