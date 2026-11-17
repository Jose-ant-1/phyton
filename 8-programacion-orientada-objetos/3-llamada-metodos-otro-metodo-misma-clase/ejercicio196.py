class Agenda:
    def __init__(self):
        self.contactos = {}

    def menu(self):
        opcion = 0
        while opcion != 5:
            print("1 - Carga de un contacto en la agenda")
            print("2 - Listado complteo de la agenda")
            print("3 - Consulta ingresando el nombre de la persona")
            print("4 - Modificación del teléfono y mail")
            print("5 - Finalizar programa")
            opcion = int(input("Ingrese su opción: "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listado()
            elif opcion == 3:
                self.consulta()
            elif opcion == 4:
                self.modificacion()

    def cargar(self):
        nombre = input("Ingrese el nombre de la persona: ")
        telefono = input("Ingrese el número de teléfono: ")
        mail = input("Ingrese el mail: ")
        self.contactos[nombre] = (telefono,mail)
        print("___________________________________________________")

    def listado(self):
        print("___________________________________________________")
        print("Listado completo de la agenda")
        for nombre in self.contactos:
            print(nombre,self.contactos[nombre][0],self.contactos[nombre][1])
        print("___________________________________________________")

    def consulta(self):
        print("___________________________________________________")
        nombre = input("Ingrese eln ombre de la persona a consultar: ")
        if nombre in self.contactos:
            print(f"{nombre}, su teléfono es {self.contactos[nombre][0]} y su mail es {self.contactos[nombre][1]}")
        else:
            print("No existe un contacto con ese nombre")
        print("___________________________________________________")

    def modificacion(self):
        print("___________________________________________________")
        nombre = input("Ingrese el nombre de la persona a modificar el teléfono y mail: ")

        if nombre in self.contactos:
            telefono = input("Ingrese el nuevo teléfono: ")
            mail = input("Ingrese el nuevo mail: ")
            self.contactos[nombre] = (telefono,mail)
        else:
            print("No existe un contacto con ese nombre")
        print("___________________________________________________")

agenda = Agenda()
agenda.menu()

