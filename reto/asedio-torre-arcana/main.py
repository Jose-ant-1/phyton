from Personaje import Personaje
from Mago import Mago
from Guerrero import Guerrero


def pruebaTorre():
    personajesDisponibles = [Mago("Veigar"), Guerrero("Talon")]

    print("Elige personaje: ")
    for i, p in enumerate(personajesDisponibles, 1):
        print(f"{i}. {p.nombre} ({p.__class__.__name__})")

    while True:
        try:
            eleccion = int(input("Introduce el número de tu personaje: "))
            if 1 <= eleccion <= len(personajesDisponibles):
                jugador = personajesDisponibles[eleccion - 1]
                break
            else:
                print("Número fuera de rango")
        except ValueError:
            print("Introduce un número válido")

    guardian = Personaje("Guardián", vida = 60, danyo = 10)
    print(f"Te enfrntas contra {guardian.nombre}")

    while jugador.estaVivo() and guardian.estaVivo():
        print("------------------------------------------")
        jugador.mostrarEstado()
        guardian.mostrarEstado()
        print("------------------------------------------")
        print("1 - atacar")
        print("2 - usar habilidad especial")
        print("3 - consultar estado")
        print("4 - salir")
        opcion = int(input("Elige una opción (1-4): "))
        accionRealizada = False

        if opcion == 1:
            accionRealizada = jugador.atacar(guardian)
        elif opcion == 2:
            accionRealizada = jugador.habilidadEspecial(guardian)
        elif opcion == 3:
            print(" -- Estado actual -- ")
            jugador.mostrarEstado()
            guardian.mostrarEstado()
            continue
        elif opcion == 4:
            print("Partida terminada")
            break
        else:
            print("Opción no válida. Intenta de nuevo")

        if accionRealizada:
            if guardian.estaVivo():
                print(f"El guardian {guardian.nombre} contraataca")
                guardian.atacar(jugador)
            else:
                print(f"Derrotaste a {guardian.nombre}")
                break

    print("==========================")
    if jugador.estaVivo():
        print("Has ganado")
    else:
        print("Has perdido")
    print("==========================")
    
pruebaTorre()
