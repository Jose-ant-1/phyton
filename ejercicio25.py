x = int(input("Ingrese la cordenada X: "))
y = int(input("Ingrese la cordenada Y: "))

if x > 0 and y > 0:
    print("Estás en el primer cuadrante")
else:
    if x < 0 and y > 0:
        print("Estás en el segundo cuadrante")
    else:
        if x < 0 and y < 0:
            print("Estás en el tercer cuadrante")
        else:
            print("Estás en el cuarto cuadrante")

            