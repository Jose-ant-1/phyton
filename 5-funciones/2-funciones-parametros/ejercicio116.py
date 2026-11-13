def mostrarMensaje(mensaje):
    print("**********************************")
    print(mensaje)
    print("**********************************")

def cargaSuma():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    suma = valor1 + valor2
    print(f"El resultado de la suma es: {suma}")

mostrarMensaje("El programa calcula la suma de los valores ingresador por teclado")
cargaSuma()
mostrarMensaje("Gracias por usar este programa")
