def presentacion():
    print("Programa que permite cargar dos valores por teclado.")
    print("Efectua la suma de los valores")
    print("Muestra el resultado de la suma")
    print("*******************************")

def cargaSuma():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    suma = valor1 + valor2
    print(f"El resultado de la suma es: {suma}")

def finalizacion():
    print("********************************")
    print("Gracias por usar este programa")

presentacion()
cargaSuma()
finalizacion()




