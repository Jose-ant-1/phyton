t = int(input("Cuantos triángulos quieres procesar?: "))
cantidad = 0

for x in range(t):
    baseTriangulo = int(input("Ingrese el valor de la base: "))
    alturaTriangulo = int(input("Ingrese el valor de la altura: "))
    superficie = baseTriangulo * alturaTriangulo / 2
    print(f"La superficie es de {superficie}")    
    if superficie > 12:
        cantidad = cantidad + 1

print(f"La cantidd de triángulos con superficie superior a 12 son {cantidad}")

