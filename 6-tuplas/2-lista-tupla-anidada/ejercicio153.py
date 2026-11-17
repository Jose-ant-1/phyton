def cargarEmpleados():
    empleados = []
    for x in range(5):
        nom = input("Ingrese el nombre del empleado: ")
        su1 = int(input("Ingrese su primer sueldo:"))
        su2 = int(input("Ingrese su primer sueldo:"))
        su3 = int(input("Ingrese su primer sueldo:"))
        empleados.append([nom,(su1,su2,su3)])
    return empleados

def ganancias(empleados):
    print("Monto total ganado por empleado en los últimos tres meses:")
    for x in range(5):
        total = empleados[x][1][0] + empleados[x][1][1] + empleados[x][1][2]
        print(empleados[x][0], total)

def gananciasSuperiorA10000(empleados):
    print("empleados con ingresos superiores a 10000 en los últimos 3 meses")
    for x in range(5):
        total = empleados[x][1][0] + empleados[x][1][1] + empleados[x][1][2]
        if total > 10000:
            print(empleados[x][0], total)

empleados = cargarEmpleados()
ganancias(empleados)
gananciasSuperiorA10000(empleados)

