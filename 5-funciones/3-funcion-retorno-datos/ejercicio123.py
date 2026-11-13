def devolverMedia(v1,v2,v3):
    media = (v1 + v2 + v3) / 3
    return media


valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
valor3 = int(input("Ingrese el tercer valor: "))
print(f"la media de los tres valores es: {devolverMedia(valor1,valor2,valor3)}")
