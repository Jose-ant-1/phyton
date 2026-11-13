paises = []
habitantes = []

for x in range(5):
    nom = input("Ingrese el nombre de un país: ")
    paises.append(nom)
    hab = int(input("Ingrese la cantidad de habitantes del país: "))
    habitantes.append(hab)

for x in range(4):
    for y in range(4-x):
        if habitantes[y] > habitantes[y + 1]:
            aux = habitantes[y]
            habitantes[y] = habitantes[y + 1]
            habitantes[y + 1] = aux
            aux2 = paises[y]
            paises[y] = paises[y + 1]
            paises[y + 1] = aux2

print("Lista de paises en orden alfabético")
for x in range(5):
    print(f"{paises[x]}: {habitantes[x]}")

for x in range(4):
    for y in range(4-x):
        if habitantes[y] < habitantes[y + 1]:
            aux = habitantes[y]
            habitantes[y] = habitantes[y + 1]
            habitantes[y + 1] = aux
            aux2 = paises[y]
            paises[y] = paises[y + 1]
            paises[y + 1] = aux2

print("Lista de paises ordenado por cantidad de habitantes")

for x in range(5):
    print(f"{paises[x]}: {habitantes[x]}")


