aprobados = 0
suspensos = 0
for x in range(10):
    nota = int(input("Ingrese la nota: "))
    if nota >= 7:
        aprobados = aprobados + 1
    else:
        suspensos = suspensos + 1
print(f"Cantidad de aprobados: {aprobados}")
print(f"Cantidad de suspensos: {suspensos}")

