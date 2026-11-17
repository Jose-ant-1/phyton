def cargar(): 
    alumnos = {}
    for x in range(3):
        dni = int(input("Ingrese el número de dni: "))
        listaMaterias = []
        continua = "s"
        while continua == "s":
            materia = input("Ingrese el nombre de materia que cursa: ")
            nota = int(input("Ingrese la nota: "))
            listaMaterias.append((materia,nota))
            continua = input("Desea cargar otra materia para dicho alumno [s/n]: ")
        alumnos[dni] = listaMaterias
    return alumnos

def listar(alumnos):
    for dni in alumnos:
        print(f"Dni del alumno: {dni}")
        print(f"Materias que cursa y notas")
        for nota,materia in alumnos[dni]:
            print(materia,nota)

def consultaNotas(alumnos):
    dni = int(input("Ingrese el dni a consultar: "))
    if dni in alumnos:
        for nota,materia in alumnos[dni]:
            print(materia,nota)

alumnos = cargar()
listar(alumnos)
consultaNotas(alumnos)

