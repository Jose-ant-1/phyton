lista1 = []

for x in range(5):
    valor = int(input("Ingrese un valor: "))
    lista1.append(valor)

print(f"Lista original: {lista1}")

lista2 = []
posicion = 0

while posicion < len(lista1):
    if lista1[posicion] >= 10:
        lista2.append(lista1.pop(posicion))
    else:
        posicion = posicion + 1

print(f"Lista después de borrar los elemenot mayores o iguales a 10: {lista1}")
print(f"Lista generada con los elementos mayores o iguales a 10: {lista2}")

