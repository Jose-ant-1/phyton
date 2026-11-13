lista = []

for x in range(5):
    valor = int(input("Ingrese un valor: "))
    lista.append(valor)

for x in range(4):
    for y in range(4-x):
        if lista[y] > lista[y + 1]:
            aux = lista[y]
            lista[y] = lista[y + 1]
            lista[y + 1] = aux


print(f"Lista ordenada de menor a mayor: {lista}")

for x in range(4):
    for y in range(4-x):
        if lista[y] < lista[y + 1]:
            aux = lista[y]
            lista[y] = lista[y + 1]
            lista[y + 1] = aux

print(f"Lista ordenada de mayor a menor: {lista}")
