def cargarSueldos():
    sueldos = []
    for x in range(10):
        su = int(input("Ingrese sueldo: "))
        sueldos.append(su)
    return sueldos

def imprimirSueldo(sueldos):
    print("Lista de sueldos")
    for x in range(len(sueldos)):
        print(sueldos[x])

def sueldosMayor4000(sueldos):
    cant = 0
    for x in range(len(sueldos)):
        if sueldos[x] > 4000:
            cant = cant + 1
    print(f"Cantidad de empleados con un sueldo superior a 4000: {cant}")

def promedio(sueldos):
    suma = 0
    for x in range(len(sueldos)):
        suma = suma + sueldos[x]
    return suma // 10

def sueldosBajo(sueldos):
    pro = promedio(sueldos)
    print(f"Sueldo promedio de la empresa: {pro}")
    print("Sueldos inferiores al promedio")
    for x in range(len(sueldos)):
        if sueldos[x] < pro:
            print(sueldos[x])

sueldos = cargarSueldos()
imprimirSueldo(sueldos)
sueldosMayor4000(sueldos)
sueldosBajo(sueldos)
