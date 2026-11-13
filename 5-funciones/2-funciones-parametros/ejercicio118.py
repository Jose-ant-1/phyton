'''
def mostrar_perimetro(lado):
    per = lado * 4
    print(f"El perimetro del cuadrado es: {per}")

def mostrar_superficie(lado):
    sup = lado * lado
    print(f"La superficie del cuadrado es: {sup}")

def cargar_dato():
    la = int(input("Ingrese el valor del lado del cuadrado: "))
    respuesta = input("Desea calcular el perimetro o la superficie? (perimetro/superficie): ")
    if respuesta == "perimetro":
        mostrar_perimetro(la)
    if respuesta == "superficie":
        mostrar_superficie(la)

cargar_dato()
'''

def cantidadVocales(cadena):
    cant = 0
    for x in range(len(cadena)):
        if cadena[x] == "a" or cadena[x] == "e" or cadena[x] == "i" or cadena[x] == "o" or cadena[x] == "u":
            cant = cant + 1
    print(f"La cantidad de vocales de la palarbra {cadena} es: {cant}")

cantidadVocales("hola")
cantidadVocales("administracion")
cantidadVocales("correr")
