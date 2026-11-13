def tabla(numero, terminos = 11):
    for x in range(1,terminos):
        va = x * numero
        print(va, ",", sep = "", end = "")
    print()

print("Tabla del 3")
tabla(3)
print("Tabla del 3 con 5 terminos")
tabla(3,5)
print("Tabla del 3 con 20 terminos")
tabla(terminos = 20,numero = 3)
