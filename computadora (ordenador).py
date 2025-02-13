class Computadora:
    def __init__(self, marca, modelo, procesador, ram, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.encendido = False

    def encender(self):
        if not self.encendido:
            print("La computadora se está encendiendo.")
            self.encendido = True
        else:
            print("La computadora ya está encendida.")

    def apagar(self):
        if self.encendido:
            print("La computadora se está apagando.")
            self.encendido = False
        else:
            print("La computadora ya está apagada.")

    def mostrar_atributos(self):
        estado = "encendida" if self.encendido else "apagada"
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram} GB")
        print(f"Almacenamiento: {self.almacenamiento} GB")
        print(f"Estado: {estado}")

if __name__ == "__main__":
    marca = "vit"
    modelo = "XPS 15"
    procesador = "Intel i5"
    ram = input("Ingrese la cantidad de RAM (en GB): ")
    almacenamiento = input("Ingrese la cantidad de almacenamiento (en GB): ")

    mi_computadora = Computadora(marca, modelo, procesador, ram, almacenamiento)

    while True:
        print("\nMenú:")
        print("1. Encender computadora")
        print("2. Apagar computadora")
        print("3. Mostrar atributos de la computadora")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mi_computadora.encender()
        elif opcion == "2":
            mi_computadora.apagar()
        elif opcion == "3":
            mi_computadora.mostrar_atributos()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")