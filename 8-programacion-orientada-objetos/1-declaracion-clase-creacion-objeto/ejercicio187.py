class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def mostrarEstado(self):
        if self.nota <= 4:
            print("Regular")
        else:
            print("Libre")

alumno1 = Alumno()
alumno1.inicializar("Diego", 2)
alumno1.imprimir()
alumno1.mostrarEstado()

alumno2 = Alumno()
alumno2.inicializar("Ana", 10)
alumno2.imprimir()
alumno2.mostrarEstado()



