import random

def jugarDados():
    saldo = 100
    print(f"Empiezas con {saldo} monedas.")

    while saldo > 0:
        print(f"Saldo actual: {saldo} monedas ")
        entrada = input("Cuánto quieres apostar (salir para retirarse): ").lower()

        if entrada == "salir":
            print(f"retirado con {saldo} monedas.")
            break

        if not entrada.isdigit():
            print("Por favor, introduce un número válido.")
            continue

        apuesta = int(entrada)

        if apuesta <= 0 or apuesta > saldo:
            print(f"Apuesta no válida. Debe ser entre 1 y {saldo} monedas.")
            continue

        dado1Usuario = random.randint(1, 6)
        dado2Usuario = random.randint(1, 6)
        totalUsuario = dado1Usuario + dado2Usuario

        
        dado1Pc = random.randint(1, 6)
        dado2Pc = random.randint(1, 6)
        totalPc = dado1Pc + dado2Pc

        print(f"Tus dados: [{dado1Usuario}] y [{dado2Usuario}] Total: {totalUsuario}")
        print(f"Dados del programa: [{dado1Pc}] y [{dado2Pc}] Total: {totalPc}")

        if totalUsuario > totalPc:
            if dado1Usuario == dado2Usuario:
                ganancia = apuesta * 2
                print(f"Dados DOBLES y VICTORIA. Ganas el doble: +{ganancia} monedas.")
            else:
                ganancia = apuesta
                print(f"Ganaste la ronda. +{ganancia} monedas.")
            saldo += ganancia

        elif totalUsuario < totalPc:
            print(f"Perdiste la ronda. -{apuesta} monedas.")
            saldo -= apuesta

        else:
            print("Empate. Recuperas tu apuesta.")

    if saldo == 0:
        print("Te quedaste sin monedas. Fin del juego")

jugarDados()