import tkinter as tk
from Personaje import Personaje
from Mago import Mago
from Guerrero import Guerrero

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Asedio a la Torre Arcana")
        self.ventana1.geometry("520x480")
        self.ventana1.resizable(False, False)

        self.jugador = None
        self.guardian = None

        # Título
        self.lblTitulo = tk.Label(self.ventana1, text="ASEDIO A LA TORRE ARCANA", font=("Arial", 14, "bold"))
        self.lblTitulo.grid(column=0, row=0, columnspan=2, pady=10)

        # Selección de personaje
        self.lblSeleccion = tk.Label(self.ventana1, text="Selecciona a tu Campeón:", font=("Arial", 11, "bold"))
        self.lblSeleccion.grid(column=0, row=1, columnspan=2, pady=5)

        self.btnMago = tk.Button(
            self.ventana1,
            text="🧙 Mago (Veigar)\nVida: 50 | Maná: 30",
            width=22,
            height=2,
            command=self.elegirMago
        )
        self.btnMago.grid(column=0, row=2, padx=10, pady=5)

        self.btnGuerrero = tk.Button(
            self.ventana1,
            text="⚔️ Guerrero (Talon)\nVida: 70 | Cargas: 2",
            width=22,
            height=2,
            command=self.elegirGuerrero
        )
        self.btnGuerrero.grid(column=1, row=2, padx=10, pady=5)

        # Estado del Jugador
        self.lblEstadoJugador = tk.Label(self.ventana1, text="Jugador: Esperando selección...", font=("Arial", 10, "bold"), fg="blue")
        self.lblEstadoJugador.grid(column=0, row=3, columnspan=2, pady=5)

        # Estado del Guardián
        self.lblEstadoGuardian = tk.Label(self.ventana1, text="Enemigo: Guardián de la Torre", font=("Arial", 10, "bold"), fg="crimson")
        self.lblEstadoGuardian.grid(column=0, row=4, columnspan=2, pady=5)

        # Botones de Acción
        self.btnAtacar = tk.Button(
            self.ventana1,
            text="Atacar",
            font=("Arial", 10, "bold"),
            width=18,
            state="disabled",
            command=self.atacar
        )
        self.btnAtacar.grid(column=0, row=5, padx=10, pady=10)

        self.btnHabilidad = tk.Button(
            self.ventana1,
            text="Habilidad Especial",
            font=("Arial", 10, "bold"),
            width=20,
            state="disabled",
            command=self.usarHabilidad
        )
        self.btnHabilidad.grid(column=1, row=5, padx=10, pady=10)

        # Registro de combate
        self.lblLogJugador = tk.Label(self.ventana1, text="", wraplength=460, fg="black")
        self.lblLogJugador.grid(column=0, row=6, columnspan=2, pady=3)

        self.lblLogRival = tk.Label(self.ventana1, text="", wraplength=460, fg="crimson")
        self.lblLogRival.grid(column=0, row=7, columnspan=2, pady=3)

        # Resultado final
        self.lblResultado = tk.Label(self.ventana1, text="Selecciona un héroe para comenzar el combate.", font=("Arial", 11, "bold"))
        self.lblResultado.grid(column=0, row=8, columnspan=2, pady=10)

        # Reiniciar
        self.btnReiniciar = tk.Button(self.ventana1, text="Cambiar Héroe / Reiniciar", command=self.reiniciar)
        self.btnReiniciar.grid(column=0, row=9, columnspan=2, pady=8)

        self.ventana1.mainloop()

    def elegirMago(self):
        self.jugador = Mago("Veigar")
        self.iniciarCombate("Bola de Fuego")

    def elegirGuerrero(self):
        self.jugador = Guerrero("Talon")
        self.iniciarCombate("Golpe Poderoso")

    def iniciarCombate(self, nombreHabilidad):
        self.guardian = Personaje("Guardián", vida=60, danyo=10)
        self.btnMago.config(state="disabled")
        self.btnGuerrero.config(state="disabled")
        self.btnAtacar.config(state="normal")
        self.btnHabilidad.config(state="normal", text=f"{nombreHabilidad}")
        self.lblResultado.config(text="¡El combate ha comenzado! Elige tu acción.", fg="darkblue")
        self.lblLogJugador.config(text="")
        self.lblLogRival.config(text="")
        self.actualizarEstado()

    def actualizarEstado(self):
        if self.jugador and self.guardian:
            recurso = self.jugador.getRecursoTexto()
            self.lblEstadoJugador.config(
                text=f"{self.jugador.nombre} ({self.jugador.__class__.__name__}) | Vida: {self.jugador.vida}/{self.jugador.vidaMax} | {recurso}"
            )
            self.lblEstadoGuardian.config(
                text=f"{self.guardian.nombre} | Vida: {self.guardian.vida}/{self.guardian.vidaMax}"
            )

    def ejecutarTurno(self, accionJugador, *args):
        exito, msgJugador = accionJugador(*args)
        if not exito:
            self.lblLogJugador.config(text=msgJugador, fg="orange")
            return

        self.lblLogJugador.config(text=msgJugador, fg="blue")

        # Comprobar si el guardián ha muerto
        if not self.guardian.estaVivo():
            self.actualizarEstado()
            self.lblResultado.config(text=f"¡VICTORIA! Derrotaste a {self.guardian.nombre}.", fg="green")
            self.finalizarCombate()
            return

        # Contraataque del Guardián
        _, msgRival = self.guardian.atacar(self.jugador)
        self.lblLogRival.config(text=f"El {self.guardian.nombre} contraataca: {msgRival}", fg="crimson")

        self.actualizarEstado()

        # Comprobar si el jugador ha muerto
        if not self.jugador.estaVivo():
            self.lblResultado.config(text="¡DERROTA! Has sido derrotado.", fg="red")
            self.finalizarCombate()

    def atacar(self):
        self.ejecutarTurno(self.jugador.atacar, self.guardian)

    def usarHabilidad(self):
        self.ejecutarTurno(self.jugador.habilidadEspecial, self.guardian)

    def finalizarCombate(self):
        self.btnAtacar.config(state="disabled")
        self.btnHabilidad.config(state="disabled")

    def reiniciar(self):
        self.jugador = None
        self.guardian = None
        self.btnMago.config(state="normal")
        self.btnGuerrero.config(state="normal")
        self.btnAtacar.config(state="disabled")
        self.btnHabilidad.config(state="disabled", text="Habilidad Especial")
        self.lblEstadoJugador.config(text="Jugador: Esperando selección...")
        self.lblEstadoGuardian.config(text="Enemigo: Guardián de la Torre")
        self.lblLogJugador.config(text="")
        self.lblLogRival.config(text="")
        self.lblResultado.config(text="Selecciona un héroe para comenzar el combate.", fg="black")


if __name__ == "__main__":
    aplicacion1 = Aplicacion()
