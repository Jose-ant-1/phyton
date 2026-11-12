oracion = input("Ingrese la oración: ")
oracionMinus = oracion.lower()
cantidad = 0
x = 0

while x < len(oracion):
    if oracion[x]=="a" or oracion[x]=="e" or oracion[x]=="i" or oracion[x]=="o" or oracion[x]=="u":
        cantidad = cantidad + 1
    x = x + 1

print(f"Las cantidad de vocales de la oración son {cantidad}")

