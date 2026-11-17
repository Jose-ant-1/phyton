from Cliente import Cliente

class Cajero:

    def __init__(self):
        self.saldoCajero = 5000
        self.clientes = [Cliente("Juan", 2000), Cliente("Ana", 4000)]

    def ingresar(self, cliente, cantidad):
        self.saldoCajero += cantidad
        cliente.addSaldo(cantidad)
        print(f"Se ha depositado {cantidad} en la cuenta de {cliente.nombre}. Nuevo saldo {cliente.saldo}")

    def extraer(self, cliente, cantidad):
        if self.saldoCajero < cantidad:
            print("No se puede realizar la operación debido a falta de efectivo en el cajero")
        else:
            if cliente.saldo >= cantidad:
                cliente.resSaldo(cantidad)
                self.saldoCajero -= cantidad
                print(f"operación finalizada. Nuevo saldo: {cliente.saldo}")
            else:
                print(f"La cuenta del cliente tiene {cliente.saldo}, por lo que no se puede retirar {cantidad}")

    def buscarCliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return cliente
        return None

    def salir(self):
        print("Gracias por usar nuestro servicio")
