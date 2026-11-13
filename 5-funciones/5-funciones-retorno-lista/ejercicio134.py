def cargarDatos():
    nom = []
    ed = []
    for x in range(5):
        v1 = input("Ingrese el nombre de la persona:  ")
        nom.append(v1)
        v2 = int(input("Ingrese la edad: "))
        ed.append(v2)
    return [nom, ed]


def MayoresEdad(nom,ed):
    print("Nombres de personas mayores de edad")
    for x in range(len(nom)):
        if ed[x] >= 18:
            print(nom[x])

def promedioEdades(ed):
    suma = 0
    for x in range(len(ed)):
        suma = suma + ed[x]
    
    print(f"Edad promedio de las personas: {suma // 5}")

nombres,edades=cargarDatos()
MayoresEdad(nombres,edades)
promedioEdades(edades)
