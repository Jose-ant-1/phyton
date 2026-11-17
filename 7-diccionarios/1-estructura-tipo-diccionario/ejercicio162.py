def cargar():
    personas = {}
    for x in range(4):
        numero = int(input("Ingrese el número de documento: "))
        nombre = input("Ingrese el nombre: ")
        personas[numero] = nombre
    return personas

def imprimir(personas):
    print("Listado del diccionario completo")
    for numero in personas:
        print(numero, personas[numero])

def consultarPorNumero(personas):
    nro = int(input("Ingrese el número de documento a consultar: "))
    if nro in personas:
        print(f"Nombre de la persona: {personas[nro]}")
    else:
        print("No existe una persona con dicho número de documento")

personas = cargar()
imprimir(personas)
consultarPorNumero(personas)