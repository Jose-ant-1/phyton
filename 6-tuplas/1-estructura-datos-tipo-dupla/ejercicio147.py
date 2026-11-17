def cargarFecha():
    dd = int(input("Ingrese número de día: "))
    mm = int(input("Ingrese número de mes: "))
    aa = int(input("Ingrese número de año: "))
    return(dd,mm,aa)

def imprimirFecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")

fecha = cargarFecha()
imprimirFecha(fecha)

