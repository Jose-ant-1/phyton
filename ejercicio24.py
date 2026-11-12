num1 = int(input("Ingrese el primer valor"))
num2 = int(input("Ingrese el segundo valor"))
num3 = int(input("Ingrese el tercer valor"))

if num1 == num2 and num1 == num3:
    suma = num1 + num2
    print(f"La suma del primer y segundo número es {suma}")
    prod = suma * num3
    print(f"La suma del primero y segundo multiplicado por el tercero es {prod}")

