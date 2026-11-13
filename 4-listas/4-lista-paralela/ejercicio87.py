lista1 = []
print("Carga de la primera lista")
for x in range(4):
    valor = int(input("Ingrese un valor: "))
    lista1.append(valor)

lista2 = []
print("Carga de la segunda lista")
for x in range(4):
    valor = int(input("Ingrese un valor: "))
    lista2.append(valor)

listaSuma = []
for x in range(4):
    suma = lista1[x] + lista2[x]
    listaSuma.append(suma)

print(f"La lista resultante es: {listaSuma}")
