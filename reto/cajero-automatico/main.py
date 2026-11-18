from Cajero import Cajero

cajero = Cajero()
opcion = 0
cliente = None

while not cliente:
    usuario = input("Bienvenido. ¿De quien es la cuenta que desea iniciar las operaciones?: ")
    cliente = cajero.buscarCliente(usuario)
   


while opcion != 3:

    if cliente:
        print("Listadod de operaciones")
        print("_______________________")
        print("1 - Extraer dinero")
        print("2 - Ingresar dinero")
        print("3 - salir")
        opcion = int(input("¿Qué deseas hacer?: "))
        if opcion == 1:
            cantidad = int(input("Cuanto dinero quiere extraer?: "))
            cajero.extraer(cliente, cantidad)
        elif opcion == 2:
            cantidad = int(input("Cuanto dinero quiere ingresar?: "))
            cajero.ingresar(cliente, cantidad)
        elif opcion == 3:
            cajero.salir
        else:
            print("Opción no válida")
    else:
        print("El nombre ingresado no está registrado en el cajero")

    
    
'''
    Banco - elegir banco
    cajero automático tiene 1000 iniciales


    cliente
        depositar
        extraer
        salir
    
    
        elegir el banco
        elegir si operar o ver depósito
        para operar elegir cliente
    
'''
