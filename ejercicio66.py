oracion = input("Ingrese una oración: ")
cantidad = 0
x = 0
while x < len(oracion):
    if oracion[x]== " ":
        cantidad = cantidad + 1
    x = x + 1
print(f"Los espacios en blanco son {cantidad}")
