def cargarCandidatos():
    candidatos = []
    for x in range(3):
        nom = input("Ingrese el nombre del candidato: ")
        cant = int(input("Los votos de cauntas provincias tiene para cargar?: " ))
        provincias = []
        for z in range(cant):
            prov = input("Nombre de la provincia: ")
            votos = int(input("Cantidad de votos: "))
            provincias.append((prov, votos))
        candidatos.append((nom, provincias))
    return candidatos

def totalVotosCandidato(candidatos):
    for x in range(len(candidatos)):
        suma = 0
        for z in range(len(candidatos[x][1])):
            suma = suma + candidatos[x][1][z][1]
        print(candidatos[x][0],suma)

candidatos = cargarCandidatos()
totalVotosCandidato(candidatos)

