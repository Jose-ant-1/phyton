def retornarMayor(v1, v2):
    if v1 > v2:
        return v1
    else:
        return v2

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
print(f"el mayor es {retornarMayor(valor1, valor2)}")
