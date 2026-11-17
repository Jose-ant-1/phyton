def cargar():
    lista = []
    for x in range(5):
        valor = int(input("Ingrese valor: "))
        lista.append(valor)
    return lista

def devolverMayorMenor(lista):
    mayor = lista[0]
    menor = lista[0]

    for x in range(1,len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]
        else:
            if lista [x] < menor:
                menor = lista[x]

    return (mayor,menor)


lista = cargar()
mayor, menor = devolverMayorMenor(lista)
print(f"Mayor valor de la lista: {mayor}")
print(f"Menor valor de la lista: {menor}")


