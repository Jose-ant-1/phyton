class Triangulo:
    def inicializar(self):
        self.lado1 = int(input("Ingrese el primer lado: "))
        self.lado2 = int(input("Ingrese el segundo lado: "))
        self.lado3 = int(input("Ingrese el tercer lado: "))

    def imprimir(self):
        print("Valores de los lados del triángulo")
        print(f"Lado 1: {self.lado1}")
        print(f"Lado 2: {self.lado2}")
        print(f"Lado 3: {self.lado3}")

    def ladoMayor(self):
        print("Lado mayor")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(self.lado1)
        else:
            if self.lado2 > self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)

    def esEquilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("El triángulo es equilatero")
        else:
            print("El triángulo no es equilátero")

triangulo1 = Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.ladoMayor()
triangulo1.esEquilatero()
