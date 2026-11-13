nombres = []

for x in range(5):
    nom = input("Ingrese nombre de persona: ")
    nombres.append(nom)

nombresMenor = nombres[0]

for x in range(1,5):
    if nombres[x] < nombresMenor:
        nombresMenor = nombres[x]

print(f"La lista compltea de nombres ingresados son {nombres}")
print(f"El nombre menor en orden alfabético es: {nombresMenor}")
