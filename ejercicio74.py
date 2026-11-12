nombres = ["juan", "ana", "marcos", "carlos", "luis"]
cantidad = 0

for x in range(len(nombres)):
    if len(nombres[x]) >= 5:
        cantidad = cantidad + 1
print(f"Todos los nombres son {nombres}")
print(f"La cantidad de nomrbes con 5 o más caracteres es de {cantidad}")