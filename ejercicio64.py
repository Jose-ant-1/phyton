mail = input("Ingrese su email: ")

cantidad = 0
x = 0
while x < len(mail):
    if mail[x]=="@":
        cantidad = cantidad + 1
    x = x + 1

if cantidad == 1:
    print("Contiene solo un caracter @ el mail")
else:
    print("Incorrecto")
