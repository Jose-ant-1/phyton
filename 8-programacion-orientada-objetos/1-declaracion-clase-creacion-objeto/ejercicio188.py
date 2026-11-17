class Persona:
    def inicializar(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def mayorEdad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")

persona1 = Persona()
persona1.inicializar("Diego", 40)
persona1.imprimir()
persona1.mayorEdad()

