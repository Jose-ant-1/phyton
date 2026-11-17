def cargarPaisesPoblacion():
    paises = []
    for x in range(5):
        nom = input("Ingresar el nombre del pais: ")
        cant = int(input("Ingrese la cantidad de habitantes: "))
        paises.append((nom, cant))
    return paises

def imprimir(paises):
    print("Paises y población")
    for x in range(len(paises)):
        print(paises[x][0], paises[x][1])

def paisConMasPoblacion(paises):
    pos = 0
    for x in range(1,len(paises)):
        if paises[x][1] > paises[pos][1]:
            pos = x
    print(f"El país con mayor cantidad de habitantes es {paises[pos][0]}")


paises = cargarPaisesPoblacion()
imprimir(paises)
paisConMasPoblacion(paises)
