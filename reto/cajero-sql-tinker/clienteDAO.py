import mysql.connector

from Cliente import Cliente  # Ajusta el nombre si tu archivo se llama Cliente.py


class ClienteDAO:
    def abrir(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="cajero_db"  # Cambia al nombre de tu base de datos
        )
        return conexion

    def alta(self, nombre, saldo):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "INSERT INTO clientes (nombre, saldo) VALUES (%s, %s)"
        datos = (nombre, saldo)
        cursor.execute(sql, datos)
        cone.commit()
        nuevo_id = cursor.lastrowid
        cone.close()
        return nuevo_id

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT id, nombre, saldo FROM clientes ORDER BY id ASC"
        cursor.execute(sql)
        filas = cursor.fetchall()
        cone.close()
        return [Cliente(fila[1], fila[2], fila[0]) for fila in filas]

    def buscar_por_id(self, id_cliente):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT id, nombre, saldo FROM clientes WHERE id = %s"
        cursor.execute(sql, (id_cliente,))
        fila = cursor.fetchone()
        cone.close()
        if fila:
            return Cliente(fila[1], fila[2], fila[0])
        return None

    def buscar_por_nombre(self, nombre):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT id, nombre, saldo FROM clientes WHERE LOWER(nombre) = LOWER(%s)"
        cursor.execute(sql, (nombre,))
        fila = cursor.fetchone()
        cone.close()
        if fila:
            return Cliente(fila[1], fila[2], fila[0])
        return None

    def actualizar_nombre(self, id_cliente, nuevo_nombre):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "UPDATE clientes SET nombre = %s WHERE id = %s"
        cursor.execute(sql, (nuevo_nombre, id_cliente))
        cone.commit()
        afectadas = cursor.rowcount
        cone.close()
        return afectadas

    def actualizar_saldo(self, id_cliente, nuevo_saldo):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "UPDATE clientes SET saldo = %s WHERE id = %s"
        cursor.execute(sql, (nuevo_saldo, id_cliente))
        cone.commit()
        afectadas = cursor.rowcount
        cone.close()
        return afectadas

    def baja(self, id_cliente):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(sql, (id_cliente,))
        cone.commit()
        afectadas = cursor.rowcount
        cone.close()
        return afectadas