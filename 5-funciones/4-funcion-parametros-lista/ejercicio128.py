def mayorMenor(lista):
    mayor = lista[0]
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
        else:
            if lista[i] < menor:
                menor = lista[i]
    print(f"El mayor valor de la lista es: {mayor}")
    print(f"El menor valor de la lista es: {menor}")


lista = []
for x in range(5):
    valor = int(input("Ingrese un valor: "))
    lista.append(valor)
mayorMenor(lista)
    