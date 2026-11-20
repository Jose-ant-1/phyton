import tkinter as tk
import random

class AplicacionDadosApuesta:
    def __init__(self):
        self.saldoInicial = 100
        self.saldo = self.saldoInicial

        self.ventana1 = tk.Tk()
        self.ventana1.title("Juego de Dados y Apuestas")
        self.ventana1.geometry("460x420")
        self.ventana1.resizable(False, False)

        # Título
        self.lblTitulo = tk.Label(self.ventana1, text="DADOS Y APUESTAS", font=("Arial", 14, "bold"))
        self.lblTitulo.grid(column=0, row=0, columnspan=2, pady=10)

        # Saldo actual
        self.lblSaldo = tk.Label(self.ventana1, text=f"Saldo actual: {self.saldo} monedas", font=("Arial", 12, "bold"), fg="darkgreen")
        self.lblSaldo.grid(column=0, row=1, columnspan=2, pady=5)

        # Campo apuesta
        self.lblApuesta = tk.Label(self.ventana1, text="Cantidad a apostar:")
        self.lblApuesta.grid(column=0, row=2, padx=15, pady=5, sticky="e")

        self.entryApuesta = tk.Entry(self.ventana1, width=12)
        self.entryApuesta.grid(column=1, row=2, padx=15, pady=5, sticky="w")
        self.entryApuesta.insert(0, "10")

        # Botón tirar dados
        self.btnLanzar = tk.Button(self.ventana1, text="🎲 Tirar Dados 🎲", font=("Arial", 11, "bold"), bg="#cce5ff", command=self.tirarDados)
        self.btnLanzar.grid(column=0, row=3, columnspan=2, pady=12, sticky="ew", padx=50)

        # Resultados de dados
        self.lblDadosUsuario = tk.Label(self.ventana1, text="Tus dados: [-] y [-] | Total: -", font=("Arial", 10))
        self.lblDadosUsuario.grid(column=0, row=4, columnspan=2, pady=3)

        self.lblDadosPc = tk.Label(self.ventana1, text="Dados del rival: [-] y [-] | Total: -", font=("Arial", 10))
        self.lblDadosPc.grid(column=0, row=5, columnspan=2, pady=3)

        # Mensaje de resultado de la ronda
        self.lblMensaje = tk.Label(self.ventana1, text="Introduce tu apuesta y lanza los dados.", font=("Arial", 10), wraplength=400)
        self.lblMensaje.grid(column=0, row=6, columnspan=2, pady=10)

        # Botón reiniciar
        self.btnReiniciar = tk.Button(self.ventana1, text="Reiniciar Partida (100 monedas)", command=self.reiniciarJuego)
        self.btnReiniciar.grid(column=0, row=7, columnspan=2, pady=10)

        self.ventana1.mainloop()

    def tirarDados(self):
        if self.saldo <= 0:
            self.lblMensaje.config(text="Te has quedado sin monedas. Pulsa en Reiniciar Partida.", fg="red")
            return

        textoApuesta = self.entryApuesta.get().strip()
        if not textoApuesta.isdigit():
            self.lblMensaje.config(text="Error: Introduce un número válido para apostar.", fg="red")
            return

        apuesta = int(textoApuesta)
        if apuesta <= 0 or apuesta > self.saldo:
            self.lblMensaje.config(text=f"Apuesta inválida. Debe estar entre 1 y {self.saldo} monedas.", fg="red")
            return

        # Tirada de dados
        dado1Usuario = random.randint(1, 6)
        dado2Usuario = random.randint(1, 6)
        totalUsuario = dado1Usuario + dado2Usuario

        dado1Pc = random.randint(1, 6)
        dado2Pc = random.randint(1, 6)
        totalPc = dado1Pc + dado2Pc

        self.lblDadosUsuario.config(text=f"Tus dados: [{dado1Usuario}] y [{dado2Usuario}] | Total: {totalUsuario}")
        self.lblDadosPc.config(text=f"Dados del rival: [{dado1Pc}] y [{dado2Pc}] | Total: {totalPc}")

        if totalUsuario > totalPc:
            if dado1Usuario == dado2Usuario:
                ganancia = apuesta * 2
                self.saldo += ganancia
                self.lblMensaje.config(text=f"¡DADOS DOBLES Y VICTORIA! Ganas el doble: +{ganancia} monedas.", fg="green")
            else:
                ganancia = apuesta
                self.saldo += ganancia
                self.lblMensaje.config(text=f"¡Ganaste la ronda! +{ganancia} monedas.", fg="green")
        elif totalUsuario < totalPc:
            self.saldo -= apuesta
            self.lblMensaje.config(text=f"Perdiste la ronda. -{apuesta} monedas.", fg="red")
        else:
            self.lblMensaje.config(text="¡Empate! Recuperas tu apuesta.", fg="orange")

        self.lblSaldo.config(text=f"Saldo actual: {self.saldo} monedas")

        if self.saldo <= 0:
            self.lblSaldo.config(text="Saldo actual: 0 monedas (BANCARROTA)", fg="red")
            self.lblMensaje.config(text="¡Te has quedado sin monedas! Fin del juego. Pulsa Reiniciar.", fg="red")

    def reiniciarJuego(self):
        self.saldo = self.saldoInicial
        self.lblSaldo.config(text=f"Saldo actual: {self.saldo} monedas", fg="darkgreen")
        self.lblDadosUsuario.config(text="Tus dados: [-] y [-] | Total: -")
        self.lblDadosPc.config(text="Dados del rival: [-] y [-] | Total: -")
        self.lblMensaje.config(text="Partida reiniciada con 100 monedas. ¡Buena suerte!", fg="black")
        self.entryApuesta.delete(0, tk.END)
        self.entryApuesta.insert(0, "10")


if __name__ == "__main__":
    aplicacion1 = AplicacionDadosApuesta()
