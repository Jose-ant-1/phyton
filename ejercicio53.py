negativos = 0
positivos = 0
multiplo15 = 0
sumaPares = 0
for x in range(10):
    valor = int(input("Ingrese un valor: "))
    
    if valor < 0:
        negativos = negativos + 1
    else:
        if valor > 0:
            positivos = positivos + 1

    if valor % 15 == 0:
        multiplo15 = multiplo15 + 1

    if valor % 2 == 0:
        sumaPares = sumaPares + valor

print(f"La cantidad de negativos: {negativos}")
print(f"La cantidad de positivos: {positivos}")
print(f"La cantidad de múltiplos de 15: {multiplo15}")
print(f"La suma de los valores pares: {sumaPares}")

