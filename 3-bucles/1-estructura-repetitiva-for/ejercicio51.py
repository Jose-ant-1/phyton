cantTriEquilatero = 0
cantTriIsosceles = 0
cantTriEscaleno = 0

n = int(input("Ingrese la cantidad de triangulos"))
for x in range(n):
    lado1 = int(input("Ingerse el valor de lado 1: "))
    lado2 = int(input("Ingerse el valor de lado 2: "))
    lado3 = int(input("Ingerse el valor de lado 3: "))
    if lado1 == lado2 and lado1 == lado3: 
        print("Triángulo equilátero")
        cantTriEquilatero = cantTriEquilatero + 1
    else:
        if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Triángulo Isósceles")
            cantTriIsosceles = cantTriIsosceles + 1
        else:
            print("Triángulo escaleno")
            cantTriEscaleno = cantTriEscaleno + 1

print(f"Triángulos equiláteros: {cantTriEquilatero}, Triángulos Isósceles: {cantTriIsosceles}, Triángulos escalenos: {cantTriEscaleno}")

