def masCaracteres(palabras):
    pos = 0
    for x in range(len(palabras)):
        if len(palabras[x]) > len(palabras[pos]):
            pos = x
    return palabras[pos]

palabras = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print(f"La palabra con mas caracteres es: {masCaracteres(palabras)}")

