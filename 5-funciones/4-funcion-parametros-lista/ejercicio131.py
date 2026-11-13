def producto(lista):
    prod = 1
    for x in range(len(lista)):
        prod = prod * lista[x]
    return prod

lista = [1, 2, 3, 4, 5]
print(f"Lista: {lista}")
print(f"Multiplicación de todos sus elementos: {producto(lista)}")
