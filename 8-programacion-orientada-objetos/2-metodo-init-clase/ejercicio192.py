class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def mostrarPermitetro(self):
        per = self.lado * 4
        print(f"El permímetro del cuadrado es: {per}")

    def mostrarSuperficie(self):
        sup = self.lado * self.lado
        print(f"La superficie del cuadrado es {sup}")

cuadrado1 = Cuadrado(12)
cuadrado1.mostrarPermitetro()
cuadrado1.mostrarSuperficie()
