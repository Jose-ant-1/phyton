def cargaSuma():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    suma = valor1 + valor2
    print(f"El resultado de la suma es: {suma}")

def separacion():
    print("********************************")

for x in range(5):
    cargaSuma()
    separacion()


