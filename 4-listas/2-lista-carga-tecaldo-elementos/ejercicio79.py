sueldosManyana = []

print("Sueldos turno mañana")
for x in range(4):
    valor = float(input("Ingrese el sueldo: "))
    sueldosManyana.append(valor)

sueldosTarde = []

print("Sueldos turno tarde")
for x in range(4):
    valor = float(input("Ingrese el sueldo: "))
    sueldosTarde.append(valor)

print(f"Turno mañana: {sueldosManyana}")
print(f"Turno tarde: {sueldosTarde}")

