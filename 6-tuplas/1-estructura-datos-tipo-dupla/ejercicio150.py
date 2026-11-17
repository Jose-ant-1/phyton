def cargarEmpleado():
    nombre = input("Ingrese el nombre del empleado: ")
    sueldo = float(input("Ingrese su salario: "))
    return (nombre, sueldo)

def darMayorSueldo(empleado1, empleado2):
    if empleado1[1] > empleado2[1]:
        print(f"{empleado1[0]} tiene un mayor salario")
    else:
        print(f"{empleado2[0]} tiene un mayor salario")

empleado1 = cargarEmpleado()
empleado2 = cargarEmpleado()

darMayorSueldo(empleado1, empleado2)

