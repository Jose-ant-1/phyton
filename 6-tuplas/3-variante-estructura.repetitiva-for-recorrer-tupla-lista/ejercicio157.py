def cargar():
    palabras = []
    cant = int(input("Cuantas palabras quiere cargar?"))
    for x  in range(cant):
        pal = input("Ingrese palabra: ")
        palabras.append(pal)
    return palabras

def MasDe5Palabras(palabras):
    print("Palabras ingresadas con más de 5 carácteres")
    for palabra in palabras:
        if len(palabra) > 5:
            print(palabra)

palabras = cargar()
MasDe5Palabras(palabras)

