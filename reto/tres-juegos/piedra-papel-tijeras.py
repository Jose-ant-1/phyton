import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    
    while True:
        usuario = input("Elige piedra, papel o tijera (salir para terminar): ").lower()
        
        if usuario == "salir":
            print("Gracias por jugar")
            break
            
        if usuario not in opciones:
            print("Opción no válida. Intenta de nuevo.")
            
        rival = random.choice(opciones)
        print(f"El programa eligió: {rival}")
        
        if usuario == rival:
            print("Empate")
        elif (usuario == "piedra" and rival == "tijera") or (usuario == "papel" and rival == "piedra") or (usuario == "tijera" and rival == "papel"):
            print("ganaste")
        else:
            print("perdiste")

jugar()