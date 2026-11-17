def cargar():
    productos = {}
    continua = "s"
    while continua == "s":
        codigo = int(input("Ingrese el código del producto: "))
        descripcion = input("Ingrese la descripción: ")
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock actual: "))
        productos[codigo] = (descripcion, precio, stock)
        continua = input("Desea cargar otro producto? [s/n]")
    return productos

def imprimir(productos):
    print("Listado completo de productos:")
    for codigo in productos:
        print(codigo,productos[codigo][0], productos[codigo][1],productos[codigo][2])

def consulta(productos):
    codigo = int(input("Ingrese el código de artículos a consultar: "))
    if codigo in productos:
        print(productos[codigo][0], productos[codigo][1], productos[codigo][2])

def listadoStockCero(productos):
    print("Listado de articulos con stok en cero: ")
    for codigo in productos:
        if productos [codigo][2] == 0:
            print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])

productos = cargar()
imprimir(productos)
consulta(productos)
listadoStockCero(productos)
