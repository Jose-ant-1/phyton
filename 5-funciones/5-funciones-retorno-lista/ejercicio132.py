def cargaLista():
    li = []
    for x in range(5):
        valor = int(input("Ingrese valor: "))
        li.append(valor)
    return li

def imprimirMayor10(li):
    print("Elementos de la lista mayores a 10")
    for x in range(len(li)):
        if li[x] > 10:
            print(li[x])

lista = cargaLista()
imprimirMayor10(lista)