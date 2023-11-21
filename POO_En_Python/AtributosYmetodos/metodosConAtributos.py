class CuentaBancaria:
    # Definición de la clase CuentaBancaria para gestionar una cuenta bancaria.

    def __init__(self, titular, saldo=0):
        # Método constructor que inicializa la cuenta con un titular y un saldo inicial (por defecto es 0).
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        # Método para realizar un depósito en la cuenta.
        self.saldo += cantidad
        print(f"Se depositaron {cantidad} unidades. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        # Método para retirar dinero de la cuenta, siempre y cuando haya saldo suficiente.
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad} unidades. Saldo actual: {self.saldo}")
        else:
            print("Saldo insuficiente para realizar el retiro.")

    def mostrar_saldo(self):
        # Método para mostrar el saldo actual de la cuenta.
        print(f"Saldo actual de {self.titular}: {self.saldo}")

# Creación de una instancia de la clase CuentaBancaria
cuenta_1 = CuentaBancaria("Cristian peña", 1000)

# Uso de los métodos de la cuenta bancaria para realizar operaciones y mostrar información.
cuenta_1.mostrar_saldo()  
cuenta_1.depositar(500)  
cuenta_1.retirar(200)  
cuenta_1.mostrar_saldo()
