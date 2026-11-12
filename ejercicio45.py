multiplo3 = 0
multiplo5 = 0

for x in range(10):
    valor = int(input("Ingrese un número:"))
    if valor % 3 == 0:
        multiplo3 = multiplo3 + 1
    if valor % 5 == 0:
        multiplo5 = multiplo5 + 1

print(f"La cantidad de valores ingresados múltiplos de 3 son {multiplo3}")
print(f"La cantidad de valores ingresados múltiplos de 5 son {multiplo5}")
