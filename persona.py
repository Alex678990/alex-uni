import os 
import time 
class Persona:

    def __init__(self, nombre, edad, direccion):
     self.nombre = nombre
     self.edad = edad
     self.direccion = direccion 

    def saludar(self):
        print("Hola, mi nombre es: ", self.nombre)
        time.sleep(2.5)

    def comer(self, hora):
        if hora > 7 and hora < 10:
           print("Hora del desayuno")
        elif hora > 12 and hora < 15:
           print("Hora del almuerzo")
        elif hora > 19 and hora < 21:
           print("Hora de la cena")
        else:
           print(self.name, "no tiene hambre")
        time.sleep(2.5)

fred = Persona("fred", 25, "Calle 12")

while True:
    os.system("cls")
    print("¿Que hará fred?: ")
    print("1. Saludar")
    print("2. Comer")
    print("3. No hacer nada (Salir)")

    eleccion = int(input("Elija una opción (1/2/3): "))
    if eleccion == 1:
        fred.saludar()
    elif eleccion == 2:
        while True:
            hora = float(input("Ingrese la hora (Formato HH.MM por ejemplo 20.02): "))
            if hora < 0 or hora > 24:
                print("Hora inválida")
            else:
                break
        fred.comer(hora)

    else:
        print("No hará nada")
        break