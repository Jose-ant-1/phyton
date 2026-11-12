alturas = []
suma = 0
for x in range(5):
    valor = float(input("Ingrese la altura: "))
    alturas.append(valor)
    suma = suma + valor

print(f"Las alturas ingresadas son {alturas}")
promedio = suma / 5
print(f"El promedio de las alturas es {promedio}")

altas = 0
bajas = 0
for x in range(5):
    if alturas[x] > promedio:
        altas = altas + 1
    else:
        if alturas[x] < promedio:
            bajas = bajas + 1

print(f"La cantidad de personas mas bajas al promedio es de {bajas}")
print(f"La cantidad de personas mas altas al promedio es de {altas}")

