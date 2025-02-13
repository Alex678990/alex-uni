class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        return "odio los lunes" # Sonido de gato

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad) # Llama al constructor de la clase padre
        self.raza = raza
    
    def hacer_sonido(self):
        return "¡Guau!"

# Creación de instancias
animal_generico = Animal("Animalito", 5)
perro = Perro("Max", 7, "sabueso")

# Prueba de las instancias
print(f"Animal gato - garfield: {animal_generico.nombre}, Edad: {animal_generico.edad}")
print(f"Sonido del animal gato: {animal_generico.hacer_sonido()}")

print(f"\nPerro - animal: {perro.nombre}, Edad: {perro.edad}, Raza: {perro.raza}")
print(f"Sonido del perro: {perro.hacer_sonido()}")