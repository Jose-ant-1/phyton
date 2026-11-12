lista = []

for x in range(5):
    valor = int(input("Ingrese valor: "))
    lista.append(valor)

mayor = lista[0]

for x in range(1,5):
    if lista[x] > mayor:
        mayor = lista[x]

print(f"La lista completa es: {lista}")
print(f"El número mayor de la lista es {mayor}")

