class Cliente:

    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def addSaldo(self, cantidad):
        self.saldo += cantidad

    def resSaldo(self, cantidad):
        self.saldo -= cantidad
