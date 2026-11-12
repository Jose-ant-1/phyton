sueldos = []
suma = 0
for x in range(5):
    valor = float(input("Ingrese el sueldo del operario: "))
    sueldos.append(valor)
    suma = suma + valor

print(f"Lista de sueldos: {sueldos}")
print(f"promedio de sueldos {suma / 5}")
