alumnos = []
notas = []

for x in range(5):
    nom = input("Ingrese el nombre del alumno: ")
    alumnos.append(nom)
    nota = int(input("Ingrese la nota del alumno: "))
    notas.append(nota)

for x in range(4):
    for y in range(4-x):
        if notas[y] > notas[y + 1]:
            aux = notas[y]
            notas[y] = notas[y + 1]
            notas[y + 1] = aux
            aux2 = alumnos[y]
            alumnos[y] = alumnos[y + 1]
            alumnos[y + 1] = aux2

print("Lista de alumnos y sus notas ordenadas de mayor a menor:")
for x in range(5):
    print(f"{alumnos[x]}: {notas[x]}")
