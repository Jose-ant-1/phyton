def menorValor():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))
    print("Menor de los tres")
    if valor1 < valor2 and valor1 < valor3:
        print(valor1)
    else:
        if valor2 < valor3:
            print(valor2)
        else:
            print(valor3)

menorValor()
menorValor()