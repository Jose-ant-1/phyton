def retornarSuperficie(lad1, lad2):
    return lad1 * lad2

print("Primer rectangulo")
lado1 = int(input("Ingrese el lado mayor del rectangulo: "))
lado2 = int(input("Ingrese el lado menor del rectangulo: "))
print("Segundo rectangulo")
lado3 = int(input("Ingrese el lado mayor del rectangulo: "))
lado4 = int(input("Ingrese el lado menor del rectangulo: "))

if retornarSuperficie(lado1, lado2) == retornarSuperficie(lado3, lado4):
    print("Los rectangulos tienen la misma superficie")
else:
    if retornarSuperficie(lado1, lado2) > retornarSuperficie(lado3, lado4):
        print("El primer rectangulo tiene mayor superficie")
    else:
        print("El segundo rectangulo tiene mayor superficie")
