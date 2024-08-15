# Definición de una clase vacía llamada MyEmptyPerson
class MyEmptyPerson:
    pass  # pass se usa para indicar que no hay contenido en la clase por ahora

# Imprime la clase MyEmptyPerson, mostrando que es un objeto de tipo clase
print(MyEmptyPerson)  # Imprime: <class '__main__.MyEmptyPerson'>

# Crea una instancia (un objeto) de la clase MyEmptyPerson e imprime el objeto
print(MyEmptyPerson())  # Imprime: <__main__.MyEmptyPerson object at 0x...>

# Definición de una clase llamada Person con un constructor, funciones y propiedades privadas y públicas
class Person:
    # Método constructor: Se ejecuta al crear una nueva instancia de la clase
    def __init__(self, name, surname, alias="Sin alias"):
        
        # Propiedad pública full_name, accesible desde fuera de la clase
        self.full_name = f"{name} {surname} ({alias})"
        
        # Propiedad privada __name, no accesible directamente desde fuera de la clase
        self.__name = name

    # Método público get_name para acceder al valor de la propiedad privada __name
    def get_name(self):
        return self.__name

    # Método público walk que imprime un mensaje indicando que la persona está caminando
    def walk(self):
        print(f"{self.full_name} está caminando")

# Creación de un objeto (instancia) de la clase Person
my_person = Person("Alvaro", "Moreno")

# Imprime la propiedad pública full_name del objeto my_person
print(my_person.full_name)  # Imprime: Brais Moure (Sin alias)

# Llama al método get_name para obtener el valor de la propiedad privada __name
print(my_person.get_name())  # Imprime: Alvaro

# Llama al método walk para simular que la persona está caminando
my_person.walk()  # Imprime: Alvaro Moreno (Sin alias) está caminando

# Creación de otro objeto de la clase Person, esta vez con un alias
my_other_person = Person("Alvaro", "Moreno", "M0r3n0SVQ")

# Imprime la propiedad pública full_name del objeto my_other_person
print(my_other_person.full_name)  # Imprime: Alvaro Moreno (M0r3noSVQ)

# Llama al método walk del objeto my_other_person
my_other_person.walk()  # Imprime: Alvaro Moreno (M0r3n0SVQ) está caminando

# Modifica la propiedad pública full_name del objeto my_other_person
my_other_person.full_name = "Héctor de León (El loco de los perros)"

# Imprime la nueva propiedad full_name del objeto my_other_person
print(my_other_person.full_name)  # Imprime: Héctor de León (El loco de los perros)

# Modifica nuevamente la propiedad pública full_name a un valor numérico
my_other_person.full_name = 666

# Imprime la propiedad full_name del objeto my_other_person
print(my_other_person.full_name)  # Imprime: 666
