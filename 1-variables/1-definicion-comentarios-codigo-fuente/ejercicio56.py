suma = 0

valor = int(input("Introduzca valor para sumar (-1 para salir):"))

while valor != -1:
    suma = suma + valor
    valor = int(input("Introduzca valor para sumar (-1 para salir):"))

print(f"La suma total resulta en {suma}")