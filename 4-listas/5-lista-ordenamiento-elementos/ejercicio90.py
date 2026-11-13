paises = []

for i in range(5):
    nom = input("Ingrese el nombre de un país: ")
    paises.append(nom)

for x in range(4):
    for y in range(4-x):
        if paises[y] > paises[y + 1]:
            aux = paises[y]
            paises[y] = paises[y + 1]
            paises[y + 1] = aux

print(f"Lista de paises: {paises}")
