def retornarSuperficie(lado):
    sup = lado * lado
    return sup

va = int(input("Ingrese el valor del lado del cuadrado: "))
superficie = retornarSuperficie(va)
print(f"La superficie del cuadrado es: {superficie}")