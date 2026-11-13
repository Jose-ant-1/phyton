def cantidadMayores18(edad1, *edades):
    cant = 0
    if edad1 >= 18:
        cant = cant + 1
    for x in range(len(edades)):
        if edades[x] >= 18:
            cant = cant + 1
    return cant

print(f"La cantidad de personas mayores a 18 son: {cantidadMayores18(23, 6, 7, 19 ,2 ,4)}")
