nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")

if nombre1 == nombre2:
    print("los nombres son igual de largos")
else:
    if nombre1 > nombre2:
        print(f"{nombre1} es mayor alfabéticamente")
    else:
        print(f"{nombre2} es mayor alfabéticamente")

