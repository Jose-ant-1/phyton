class Cliente:
    def __init__(self, nombre, saldo, idCliente=None):
        self.id = idCliente
        self.nombre = nombre
        self.saldo = saldo

    def addSaldo(self, cantidad):
        self.saldo += cantidad

    def resSaldo(self, cantidad):
        self.saldo -= cantidad
