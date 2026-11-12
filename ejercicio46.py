cantidad = 0
num = int(input("Cuantos valores quieres ingresar?: "))
for x in range(num):
    valor = int(input("Ingrese el valor: "))
    if valor >= 1000:
        cantidad = cantidad + 1

print(f"La cantidad de números ingresados mayores o iguales a 1000 es de {cantidad}")

