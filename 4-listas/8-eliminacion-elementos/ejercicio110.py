empleados = []
sueldos = []

cant = int(input("Cuatos empleados tiene la empresa?: "))
for x in range(cant):
    nombre = input("Ingrese el nombre del empleado: ")
    sueldo = int(input("Ingrese el sueldo del empleado: "))
    empleados.append(nombre)
    sueldos.append(sueldo)

print("Lista de empleados")
for x in range(cant):
    print(empleados[x], sueldos[x])

posicion = 0
while posicion < len(sueldos):
    if sueldos[posicion] > 10000:
        sueldos.pop(posicion)
        empleados.pop(posicion)
    else:
        posicion = posicion + 1

print("Lista de empleados con sueldos menores a 10000")
for x in range(len(sueldos)):
    print(empleados[x], sueldos[x])



