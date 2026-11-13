def sumarLista(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]
    return suma

def mayor(lista):
    mayor = lista[0]
    for x in range(1,len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]
    return mayor

def menor(lista):
    menor = lista[0]
    for x in range(1,len(lista)):
        if lista[x] < menor:
            menor = lista[x]
    return menor

listavalores = [10, 56, 23, 120, 94]
print("La lista completa es")
print(listavalores)
print(f"La suma de los valores es: {sumarLista(listavalores)}")
print(f"El valor mayor es: {mayor(listavalores)}")
print(f"El valor menor es: {menor(listavalores)}")

