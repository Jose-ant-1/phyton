nombres = []
notas = []

for x in range(4):
    nombre = input("Ingrese el nombre del alumno: ")
    nombres.append(nombre)
    nota = int(input("Ingrese la nota del alumno: "))
    notas.append(nota)

cantidad = 0
for x in range(4):
    print(nombres[x])
    print(notas[x])
    if notas[x] >= 8:
        print("Muy bueno")
        cantidad = cantidad + 1
    else:
        if notas[x] >= 4:
            print("Bueno")
        else:
            print("Insuficiente")

print(f"La cantidad de alumnos muy buenos son: {cantidad}")

