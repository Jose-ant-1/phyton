x = 1
pares = 0
impares = 0
n = int(input("Cantidad de números que se va a ingresar: "))

while x <= n:
    valor = int(input("Ingrese el valor: "))
    if valor % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    x = x + 1

print(f"La cantidad de pares es {pares}")
print(f"La cantidad de impares es {impares}")


