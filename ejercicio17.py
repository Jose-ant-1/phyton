num = int(input("Ingrese un número de hasta 3 dígitos positivo: "))

if num < 10:
    print("El número tiene un solo dígito")
elif num < 100:
    print("El número tiene dos dígitos")
elif num < 1000:
    print("El número tiene tres dígitos")
else:
    print("Error en la entrada de datos")