import tkinter as tk
import random

class AplicacionPiedraPapelTijera:
    def __init__(self):
        self.victorias = 0
        self.derrotas = 0
        self.empates = 0
        self.opciones = ["piedra", "papel", "tijera"]

        self.ventana1 = tk.Tk()
        self.ventana1.title("Piedra, Papel o Tijera")
        self.ventana1.geometry("420x350")
        self.ventana1.resizable(False, False)

        # Título
        self.lblTitulo = tk.Label(self.ventana1, text="PIEDRA, PAPEL O TIJERA", font=("Arial", 14, "bold"))
        self.lblTitulo.grid(column=0, row=0, columnspan=3, pady=10)

        # Instrucción
        self.lblInstruccion = tk.Label(self.ventana1, text="Elige tu jugada:", font=("Arial", 11))
        self.lblInstruccion.grid(column=0, row=1, columnspan=3, pady=5)

        # Botones de juego
        self.btnPiedra = tk.Button(self.ventana1, text="Piedra 🪨", width=12, height=2, command=lambda: self.jugar("piedra"))
        self.btnPiedra.grid(column=0, row=2, padx=10, pady=10)

        self.btnPapel = tk.Button(self.ventana1, text="Papel 📄", width=12, height=2, command=lambda: self.jugar("papel"))
        self.btnPapel.grid(column=1, row=2, padx=10, pady=10)

        self.btnTijera = tk.Button(self.ventana1, text="Tijera ✂️", width=12, height=2, command=lambda: self.jugar("tijera"))
        self.btnTijera.grid(column=2, row=2, padx=10, pady=10)

        # Etiquetas de elecciones
        self.lblJugador = tk.Label(self.ventana1, text="Tú elegiste: -", font=("Arial", 10))
        self.lblJugador.grid(column=0, row=3, columnspan=3, pady=3)

        self.lblRival = tk.Label(self.ventana1, text="La máquina eligió: -", font=("Arial", 10))
        self.lblRival.grid(column=0, row=4, columnspan=3, pady=3)

        # Resultado de la ronda
        self.lblResultado = tk.Label(self.ventana1, text="¡Haz tu primer movimiento!", font=("Arial", 12, "bold"), fg="darkblue")
        self.lblResultado.grid(column=0, row=5, columnspan=3, pady=10)

        # Marcador
        self.lblMarcador = tk.Label(
            self.ventana1,
            text="Victorias: 0 | Derrotas: 0 | Empates: 0",
            font=("Arial", 10, "italic")
        )
        self.lblMarcador.grid(column=0, row=6, columnspan=3, pady=10)

        # Botón reiniciar marcador
        self.btnReiniciar = tk.Button(self.ventana1, text="Reiniciar Marcador", command=self.reiniciarMarcador)
        self.btnReiniciar.grid(column=0, row=7, columnspan=3, pady=5)

        self.ventana1.mainloop()

    def jugar(self, eleccionUsuario):
        rival = random.choice(self.opciones)
        self.lblJugador.config(text=f"Tú elegiste: {eleccionUsuario.capitalize()}")
        self.lblRival.config(text=f"La máquina eligió: {rival.capitalize()}")

        if eleccionUsuario == rival:
            self.empates += 1
            self.lblResultado.config(text="¡Empate!", fg="orange")
        elif (eleccionUsuario == "piedra" and rival == "tijera") or \
             (eleccionUsuario == "papel" and rival == "piedra") or \
             (eleccionUsuario == "tijera" and rival == "papel"):
            self.victorias += 1
            self.lblResultado.config(text="¡Ganaste!", fg="green")
        else:
            self.derrotas += 1
            self.lblResultado.config(text="¡Perdiste!", fg="red")

        self.actualizarMarcador()

    def actualizarMarcador(self):
        self.lblMarcador.config(
            text=f"Victorias: {self.victorias} | Derrotas: {self.derrotas} | Empates: {self.empates}"
        )

    def reiniciarMarcador(self):
        self.victorias = 0
        self.derrotas = 0
        self.empates = 0
        self.lblJugador.config(text="Tú elegiste: -")
        self.lblRival.config(text="La máquina eligió: -")
        self.lblResultado.config(text="Marcador reiniciado. ¡Haz tu jugada!", fg="darkblue")
        self.actualizarMarcador()


if __name__ == "__main__":
    aplicacion1 = AplicacionPiedraPapelTijera()
