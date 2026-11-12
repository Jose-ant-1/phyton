sueldo = int(input("Ingrese el sueldo del empleado: "))
antiguedad = int(input("Ahora ingrese su antigüedad en años: "))

if sueldo < 500 and antiguedad > 10:
    aumento = sueldo * 0.20
    print(f"El sueldo a pagar es de {sueldo + aumento}")
else:
    if sueldo < 500:
        aumento = sueldo * 0.05
        print(f"El sueldo a pagar es de {sueldo + aumento}")
    else:
        print(f"El sueldo a pagar es de {sueldo}")


