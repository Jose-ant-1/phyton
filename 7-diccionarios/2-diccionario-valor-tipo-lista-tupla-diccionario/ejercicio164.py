def cargar():
    agenda = {}
    continua1 = "s"

    while continua1 == "s":
        fecha = input("Ingrese la fecha con formato dd/mm/aa: ")
        continua2 = "s"
        lista = []
        while continua2 == "s":
            hora = input("Ingrese la hora d ela actividad con formato hh:mm ")
            actividad = input("Ingrese la descripción de la actividad: ")
            lista.append((hora, actividad))
            continua2 = input("Ingresa otra actividad para la misma fecha[s/n]: ")
        agenda[fecha] = lista
        continua1 = input("Ingresa otra fecha [s/n]: ")
    return agenda

def imprimir(agenda):
    print("Listado complet de la agenda")
    for fecha in agenda:
        print(f"Para la fecha: {fecha}")
        for hora, actividad in agenda[fecha]:
            print(hora, actividad)

def consultarFecha(agenda):
    fecha = input("Ingrese la fehca que desea consultar: ")
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("No hay actividades agendadas para dicha fecha")


agenda = cargar()
imprimir(agenda)
consultarFecha(agenda)
