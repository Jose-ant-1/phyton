def cargar():
    diccionario = {}
    continua = "s"

    while continua == "s":
        caste = input("Ingrese palabra en castellano: ")
        ing = input("Ingrese la palabra en inglés: ")
        diccionario[ing] = caste
        continua = input("Quiere cargar otra palabra?: [S/N]")
    return diccionario

def imprimir(diccionario):
    print("Listado completo del diccionario")
    for ingles in diccionario:
        print(ingles, diccionario[ingles])

def consultarPalabra(diccionario):
    pal = input("Ingrese la palabra en inglés a consultar: ")
    if pal in diccionario:
        print(f"En castellano significa: {diccionario[pal]}")

diccionario = cargar()
imprimir(diccionario)
consultarPalabra(diccionario)
