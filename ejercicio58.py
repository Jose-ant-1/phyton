print("Datos personales 1")
nombre1 = input("Introduzca su nombre: ")
edad1 = int(input("Introduzca su edad (solo número entero): "))
altura1 = float(input("Introduzca su altura:"))

print("Datos personales 2")
nombre2 = input("Introduzca su nombre: ")
edad2 = int(input("Introduzca su edad (solo número entero): "))
altura2 = float(input("Introduzca su altura:"))

if altura1 > altura2:
    print(f"la  persona más alta es {altura1}")
else :
    print(f"la persona más alta es {nombre2}")

