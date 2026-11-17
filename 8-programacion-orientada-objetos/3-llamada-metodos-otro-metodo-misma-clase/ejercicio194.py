class Operacion:

    def __init__(self):
        self.valor1 = int(input("Ingrese primer valor: "))
        self.valor2 = int(input("Ingrese segundo valor: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        print(f"La suma es {self.valor1 + self.valor2}")

    def restar(self):
        print(f"La resta es {self.valor1 - self.valor2}")

    def multiplicar(self):
        print(f"El producto es {self.valor1 * self.valor2}")

    def dividir(self):
        print(f"La division es {self.valor1 / self.valor2}")

operacion1 = Operacion()
