cantidad = int(input("Cuantos empelados tiene la empresa?: "))
sueldos = []

for x in range(cantidad):
    su = int(input("Ingrese el sueldo del empleado: "))
    sueldos.append(su)

for x in range(cantidad - 1):
    for y in range(cantidad - 1 - x):
        if sueldos[y] > sueldos[y + 1]:
            aux = sueldos[y]
            sueldos[y] = sueldos[y + 1]
            sueldos[y + 1] = aux

print(f"Lista de sueldos ordenada: {sueldos}")


