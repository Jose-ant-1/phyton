lista = [[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]

suma = 0

for x in range(len(lista)):
    for y in range(len(lista[x])):
        suma = suma + lista[x][y]
    print(suma)
