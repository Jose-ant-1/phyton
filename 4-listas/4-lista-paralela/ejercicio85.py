productos = []
precios = []

for x in range(5):
    nombre = input("Ingrese el nombre del producto: ")
    productos.append(nombre)
    precio = int(input("Ingrese el precio del producto: "))
    precios.append(precio)

cantidad = 0
for x in range(1,5):
    if precios[x] > precios[0]:
        cantidad = cantidad + 1

print(f"La cantidad de productos con precio mayor al primer producto es: {cantidad}")

