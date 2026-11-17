class Operaciones:
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))

    def sumar(self):
        print(f"La suma es {self.valor1 + self.valor2}")

    def restar(self):
        print(f"La resta es {self.valor1 - self.valor2}")

    def multiplicar(self):
        print(f"La multiplicación es {self.valor1 * self.valor2}")

    def division(self):
        print(f"La división es {self.valor1 / self.valor2}")

operacion1 = Operaciones()
operacion1.sumar()
operacion1.restar()
operacion1.multiplicar()
operacion1.division()
