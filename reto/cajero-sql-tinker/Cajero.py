from clienteDAO import ClienteDAO


class Cajero:
    def __init__(self, saldo_cajero=5000):
        self.saldoCajero = saldo_cajero
        self.cliente_dao = ClienteDAO()

    def listarClientes(self):
        return self.cliente_dao.recuperar_todos()

    def buscarCliente(self, nombre):
        nombre_limpio = nombre.strip()
        if not nombre_limpio:
            return None
        return self.cliente_dao.buscar_por_nombre(nombre_limpio)

    def buscarClientePorId(self, id_cliente):
        return self.cliente_dao.buscar_por_id(id_cliente)

    def crearCliente(self, nombre, saldo):
        nombre_limpio = nombre.strip()
        if not nombre_limpio:
            return False, "El nombre del cliente no puede estar vacío."
        if saldo < 0:
            return False, "El saldo inicial no puede ser negativo."

        existente = self.cliente_dao.buscar_por_nombre(nombre_limpio)
        if existente is not None:
            return False, f"Ya existe un cliente llamado '{existente.nombre}'."

        nuevo_id = self.cliente_dao.alta(nombre_limpio, saldo)
        return True, f"Cliente '{nombre_limpio}' creado con ID {nuevo_id} y saldo {saldo}€."

    def modificarNombreCliente(self, id_cliente, nuevo_nombre):
        nombre_limpio = nuevo_nombre.strip()
        if not nombre_limpio:
            return False, "El nuevo nombre no puede estar vacío."

        cliente = self.cliente_dao.buscar_por_id(id_cliente)
        if cliente is None:
            return False, "No existe un cliente con ese ID."

        afectadas = self.cliente_dao.actualizar_nombre(id_cliente, nombre_limpio)
        if afectadas == 1:
            return True, f"Nombre actualizado de '{cliente.nombre}' a '{nombre_limpio}'."
        return False, "No se pudo actualizar el nombre del cliente."

    def eliminarCliente(self, id_cliente):
        cliente = self.cliente_dao.buscar_por_id(id_cliente)
        if cliente is None:
            return False, "No existe un cliente con ese ID."

        afectadas = self.cliente_dao.baja(id_cliente)
        if afectadas == 1:
            return True, f"Cliente '{cliente.nombre}' eliminado correctamente."
        return False, "No se pudo eliminar el cliente."

    def ingresar(self, cliente, cantidad):
        if cliente is None:
            return False, "Debes seleccionar un cliente válido."
        if cantidad <= 0:
            return False, "La cantidad a ingresar debe ser mayor que cero."

        nuevo_saldo = cliente.saldo + cantidad
        afectadas = self.cliente_dao.actualizar_saldo(cliente.id, nuevo_saldo)
        if afectadas != 1:
            return False, "Error al actualizar el saldo en la base de datos."

        self.saldoCajero += cantidad
        cliente.saldo = nuevo_saldo
        return True, f"Se ha depositado {cantidad}€ en la cuenta de {cliente.nombre}. Nuevo saldo: {cliente.saldo}€"

    def extraer(self, cliente, cantidad):
        if cliente is None:
            return False, "Debes seleccionar un cliente válido."
        if cantidad <= 0:
            return False, "La cantidad a extraer debe ser mayor que cero."
        if self.saldoCajero < cantidad:
            return False, "No se puede realizar la operación debido a falta de efectivo en el cajero."
        if cliente.saldo < cantidad:
            return False, f"La cuenta del cliente tiene {cliente.saldo}€, por lo que no se puede retirar {cantidad}€."

        nuevo_saldo = cliente.saldo - cantidad
        afectadas = self.cliente_dao.actualizar_saldo(cliente.id, nuevo_saldo)
        if afectadas != 1:
            return False, "Error al actualizar el saldo en la base de datos."

        cliente.saldo = nuevo_saldo
        self.saldoCajero -= cantidad
        return True, f"Operación finalizada. Retirados {cantidad}€. Nuevo saldo: {cliente.saldo}€"

    def salir(self):
        return "Gracias por usar nuestro servicio"