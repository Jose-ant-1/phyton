x = 1
suma = 0
while x <= 10:
    valor = int(input("Ingrese un valor: "))
    suma = suma + valor
    x = x + 1
media = suma / 10

print(f"La suma de los 10 valores es de {suma}")
print(f"El promedio es de {media}")
