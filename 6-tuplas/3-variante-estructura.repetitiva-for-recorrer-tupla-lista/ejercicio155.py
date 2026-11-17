def cargar():
    lista = []
    for x in range(5):
        num = int(input("Ingrese un valor: "))
        lista.append(num)
    return lista

def imprimir(lista):
    print("Lista completa")
    for elemento in lista:
        print(elemento)

def mayor(lista):
    may = lista[0]
    for elemento in lista:
        if elemento > may:
            may = elemento
    print(f"El elemento mayor de la lista es {may}")

def sumarElementos(lista):
    suma = 0
    for elemento in lista: 
        suma = suma + elemento
    print(f"La suma de todos los elementos es {suma}")

lista = cargar()
imprimir(lista)
mayor(lista)
sumarElementos(lista)