clave = input("Ingrese una clave entre 10 y 20 carácteres: ")
if len(clave) >= 10 and len(clave) <= 20:
    print("Entra en el rango correcto")
else:
    print("Es demasiado corto o demasiado largo")
