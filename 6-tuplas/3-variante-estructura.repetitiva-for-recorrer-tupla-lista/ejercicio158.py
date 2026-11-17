def cargar():
    productos = []
    for x in range(5):
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio: "))
        productos.append((nombre,precio))
    return productos


def imprimir(productos):
    print("Lista de prodcutos con precios")
    for nombre,precio in productos:
        print(nombre,precio)


def imprimirEntre10y15(productos):
    print("Lista de prodcutos que tienen precio entre 10 y 15")
    for nombre,precio in productos:
        if precio>= 10 and precio <= 15:
            print(nombre,precio)






productos = cargar()
imprimir(productos)
imprimirEntre10y15(productos)
