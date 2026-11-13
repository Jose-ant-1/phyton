x = 1
contadorSuperior7 = 0
contadorInferior7 = 0

while x <= 10:
    nota = int(input("Ingrese nota: "))
    if nota >= 7:
        contadorSuperior7 = contadorSuperior7 + 1
    else:
        contadorInferior7 = contadorInferior7 + 1
    x = x + 1

print(f"La cantidad de alumnos con notas mayores o iguales a 7 es {contadorSuperior7}")
print(f"La cantidad de alumnos con notas menores a 7 es {contadorInferior7}")