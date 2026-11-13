def cantidadVocalesA(palabra):
    cantidad = 0
    for x in range(len(palabra)):
        if palabra[x] == "a" or palabra[x] == "A":
            cantidad = cantidad + 1
    return cantidad

palabra = input("Ingrese una palabra: ")
print(f"La cantidad de vocales A en la palabra es: {cantidadVocalesA(palabra)}")
