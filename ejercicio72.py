lista = [1000, 6000, 400, 23, 130, 400, 60, 2000]
cantidad = 0

for x in range(len(lista)):
    if lista [x] > 100:
        cantidad = cantidad + 1
    x = x + 1

print(f"La lista está constituida por {lista}")
print(f"La cantidad de valores mayores a 100 en la lista son: {cantidad}")
