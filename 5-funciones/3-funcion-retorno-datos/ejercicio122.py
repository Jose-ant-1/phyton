def largo(cadena):
    return len(cadena)

nomrbre1 = input("Ingrese el primer nombre: ")
nomrbre2 = input("Ingrese el segundo nombre: ")
largo1 = largo(nomrbre1)
largo2 = largo(nomrbre2)
if largo1 == largo2:
    print(f"Los nombres {nomrbre1} y {nomrbre2} tienen la misma cantidad de letras")
else:
    if largo1 > largo2:
        print(f"El nombre {nomrbre1} tiene mas letras que {nomrbre2}")
    else:
        print(f"El nombre {nomrbre2} tiene mas letras que {nomrbre1}")