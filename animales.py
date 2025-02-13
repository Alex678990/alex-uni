import os
import time

def limpiarConsola():
    time.sleep(1.5)
    os.system("cls") 

class Animal:

    def __init__(self, nombre, edad, especie, sonido):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.sonido = sonido

    def hacerSonido(self):
        print(self.sonido)
        limpiarConsola()

    def cumplirAnios(self):
        self.edad += 1
        print(self.nombre, "cumple año de vida, actualmente tiene", self.edad, "años")
        limpiarConsola()
    
    def eleccion(self):
        while True:
            os.system("cls")
            print("Esto es", self.nombre, "un", self.especie, "de", self.edad, "años")
            print("¿Que hará", self.nombre, "?")
            print("1. Hacer sonido")
            print("2. Cumplir años")
            print("3. Volver")
            eleccion = int(input("Elija una opción (1,2,3): "))
            if eleccion == 1:
                self.hacerSonido()
            elif eleccion == 2:
                self.cumplirAnios()
            elif eleccion == 3:
                limpiarConsola()
                break
            else:
                print("Opción inválida, vuelve a intentarlo")
                limpiarConsola()

dragon= Animal("chimuelo", 3, "dragon", "ruaarrr!")
lobo = Animal("fenrri", 2, "lobo", "auuuuu")
perro= Animal("hachico", 1, "perro", "guau guau!")
vaca = Animal("hellsing", 1, "vaca", "muuuuuu")
raton = Animal("micky mouse", 2, "raton", "hola amiguitos")

while True:
    print("¿Que animal quieres ver?")
    print("1. dragon")
    print("2. lobo")
    print("3. perro")
    print("4. vaca")
    print("5. raton")
    print("6. Salir")

    eleccion = int(input("Elija una opción (1/2/3/4/5): "))
    if eleccion == 1:
        dragon.eleccion()
    elif eleccion == 2:
        lobo.eleccion()
    elif eleccion == 3:
        perro.eleccion()
    elif eleccion == 4:
        vaca.eleccion()
    elif eleccion == 5:
      
     break
    else:
        print("Opción inválida, vuelve a intentarlo")
        limpiarConsola()