import random
import time
import os

class CuentaBancaria:
    @staticmethod
    def _generar_numero():
        return ''.join(str(random.randint(0, 9)) for _ in range(10))
    
    @staticmethod
    def _generar_saldo():
        return random.randint(100, 1000)
    
    def __init__(self):
        self.numero = self._generar_numero()
        self.saldo = self._generar_saldo()
    
    def _limpiar_pantalla(self, segundos):
        time.sleep(segundos)
        os.system("cls")
    
    def operar_deposito(self):
        monto = float(input("\nMonto a depositar: $"))
        self.saldo += monto
        print("\n Depósito realizado correctamente")
        self._limpiar_pantalla(1.5)
    
    def operar_retiro(self):
        monto = float(input("\nMonto a retirar: $"))
        if monto > self.saldo:
            print("\n Error: Fondos insuficientes")
            self._limpiar_pantalla(1.5)
            return
        self.saldo -= monto
        print("\n Retiro realizado correctamente")
        self._limpiar_pantalla(1.5)
    
    def mostrar_estado(self):
        print(f"\nSaldo disponible: ${self.saldo:.2f}")
        self._limpiar_pantalla(2)

def mostrar_menu():
    print("\n" + "═"*40)
    print(" MENU PRINCIPAL ".center(40, "═"))
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir del sistema")
    print("═"*40 + "\n")

# Configuración inicial
os.system("cls")
cuenta_usuario = CuentaBancaria()
print("BIENVENIDO A BANCO VIRTUAL")
print(f"\nNúmero de cuenta: {cuenta_usuario.numero}")

while True:
    mostrar_menu()
    
    try:
        opcion = int(input("Seleccione una operación: "))
    except ValueError:
        print("\n Error: Ingrese solo números del 1 al 4")
        time.sleep(1.5)
        os.system("cls")
        continue
    
    if opcion == 1:
        cuenta_usuario.operar_deposito()
    elif opcion == 2:
        cuenta_usuario.operar_retiro()
    elif opcion == 3:
        cuenta_usuario.mostrar_estado()
    elif opcion == 4:
        print("\n¡Gracias por usar nuestros servicios!")
        time.sleep(1)
        break
    else:
        print("\n Opción no válida - Intente nuevamente")
        time.sleep(1)
    
    os.system("cls")