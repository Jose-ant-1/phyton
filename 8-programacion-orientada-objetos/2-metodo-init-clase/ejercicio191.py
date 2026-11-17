class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print("Coordenada del punto")
        print(f"({self.x},{self.y})")

    def imprimirCuadrante(self):
        if self.x > 0 and self.y > 0:
            print("Primer cuadrante")
        else:
            if self.x < 0 and self.y > 0:
                print("Segundo cuadrante")
            else:
                if self.x < 0 and self.y < 0:
                    print("Tercer cuadrante")
                else:
                    if self.x > 0 and self.y < 0:
                        print("Cuarto cuadrante")

punto1 = Punto(10, -2)
punto1.imprimir()
punto1.imprimirCuadrante()
