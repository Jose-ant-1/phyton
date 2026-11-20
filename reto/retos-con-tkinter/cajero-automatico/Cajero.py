from Cliente import Cliente

class Cajero:
    def __init__(self):
        self.saldoCajero = 5000
        self.clientes = [Cliente("Juan", 2000), Cliente("Ana", 4000)]

    def ingresar(self, cliente, cantidad):
        if cantidad <= 0:
            return False, "La cantidad a ingresar debe ser mayor que cero."
        self.saldoCajero += cantidad
        cliente.addSaldo(cantidad)
        return True, f"Se ha depositado {cantidad}€ en la cuenta de {cliente.nombre}. Nuevo saldo: {cliente.saldo}€"

    def extraer(self, cliente, cantidad):
        if cantidad <= 0:
            return False, "La cantidad a extraer debe ser mayor que cero."
        if self.saldoCajero < cantidad:
            return False, "No se puede realizar la operación debido a falta de efectivo en el cajero."
        if cliente.saldo < cantidad:
            return False, f"La cuenta del cliente tiene {cliente.saldo}€, por lo que no se puede retirar {cantidad}€."

        cliente.resSaldo(cantidad)
        self.saldoCajero -= cantidad
        return True, f"Operación finalizada. Retirados {cantidad}€. Nuevo saldo: {cliente.saldo}€"

    def buscarCliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre.lower():
                return cliente
        return None

    def salir(self):
        return "Gracias por usar nuestro servicio"
