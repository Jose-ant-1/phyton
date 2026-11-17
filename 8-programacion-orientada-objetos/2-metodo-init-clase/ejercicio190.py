class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.sueldo = float(input("Ingrese el sueldo: "))

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Sueldo: {self.sueldo}")

    def pagaImpuestos(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")

empleado1 = Empleado()
empleado1.imprimir()
empleado1.pagaImpuestos()
