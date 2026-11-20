import tkinter as tk
import random

class AplicacionAhorcado:
    def __init__(self):
        self.palabras = ["PYTHON", "VARIABLE", "FUNCION", "INTERFAZ", "VENTANA", "PROGRAMA", "TKINTER"]
        self.maxIntentos = 6

        self.ventana1 = tk.Tk()
        self.ventana1.title("Juego del Ahorcado")
        self.ventana1.geometry("450x420")
        self.ventana1.resizable(False, False)

        # Título
        self.lblTitulo = tk.Label(self.ventana1, text="JUEGO DEL AHORCADO", font=("Arial", 14, "bold"))
        self.lblTitulo.grid(column=0, row=0, columnspan=2, pady=10)

        # Palabra oculta
        self.lblPalabra = tk.Label(self.ventana1, text="", font=("Courier", 20, "bold"), fg="darkblue")
        self.lblPalabra.grid(column=0, row=1, columnspan=2, pady=15)

        # Vidas restantes
        self.lblIntentos = tk.Label(self.ventana1, text="", font=("Arial", 11))
        self.lblIntentos.grid(column=0, row=2, columnspan=2, pady=5)

        # Letras usadas
        self.lblUsadas = tk.Label(self.ventana1, text="Letras usadas: Ninguna", font=("Arial", 10, "italic"))
        self.lblUsadas.grid(column=0, row=3, columnspan=2, pady=5)

        # Entrada de letra
        self.lblLetra = tk.Label(self.ventana1, text="Introduce una letra:")
        self.lblLetra.grid(column=0, row=4, padx=15, pady=10, sticky="e")

        self.entryLetra = tk.Entry(self.ventana1, width=6, font=("Arial", 12), justify="center")
        self.entryLetra.grid(column=1, row=4, padx=15, pady=10, sticky="w")
        self.entryLetra.bind("<Return>", lambda event: self.probarLetra())

        # Botón probar letra
        self.btnProbar = tk.Button(self.ventana1, text="Probar Letra", width=15, command=self.probarLetra)
        self.btnProbar.grid(column=0, row=5, columnspan=2, pady=5)

        # Mensaje de estado / resultado
        self.lblMensaje = tk.Label(self.ventana1, text="", font=("Arial", 11, "bold"))
        self.lblMensaje.grid(column=0, row=6, columnspan=2, pady=10)

        # Botón reiniciar
        self.btnReiniciar = tk.Button(self.ventana1, text="Nueva Partida", command=self.nuevaPartida)
        self.btnReiniciar.grid(column=0, row=7, columnspan=2, pady=10)

        self.nuevaPartida()
        self.ventana1.mainloop()

    def nuevaPartida(self):
        self.palabraSecreta = random.choice(self.palabras)
        self.letrasAcertadas = set()
        self.letrasUsadas = set()
        self.intentosRestantes = self.maxIntentos
        self.juegoTerminado = False

        self.btnProbar.config(state="normal")
        self.entryLetra.config(state="normal")
        self.entryLetra.delete(0, tk.END)
        self.lblMensaje.config(text="Adivina la palabra antes de agotar tus intentos.", fg="black")
        self.actualizarPantalla()

    def mostrarProgreso(self):
        progreso = [letra if letra in self.letrasAcertadas else "_" for letra in self.palabraSecreta]
        return " ".join(progreso)

    def actualizarPantalla(self):
        self.lblPalabra.config(text=self.mostrarProgreso())
        self.lblIntentos.config(text=f"Intentos restantes: {self.intentosRestantes}/{self.maxIntentos}")
        usadasTexto = ", ".join(sorted(self.letrasUsadas)) if self.letrasUsadas else "Ninguna"
        self.lblUsadas.config(text=f"Letras usadas: {usadasTexto}")

    def probarLetra(self):
        if self.juegoTerminado:
            return

        letra = self.entryLetra.get().strip().upper()
        self.entryLetra.delete(0, tk.END)

        if len(letra) != 1 or not letra.isalpha():
            self.lblMensaje.config(text="Por favor, introduce una única letra válida (A-Z).", fg="orange")
            return

        if letra in self.letrasUsadas:
            self.lblMensaje.config(text=f"Ya habías probado la letra '{letra}'.", fg="orange")
            return

        self.letrasUsadas.add(letra)

        if letra in self.palabraSecreta:
            self.letrasAcertadas.add(letra)
            self.lblMensaje.config(text=f"¡Bien! La letra '{letra}' está en la palabra.", fg="green")
        else:
            self.intentosRestantes -= 1
            self.lblMensaje.config(text=f"Fallaste. La letra '{letra}' no está.", fg="red")

        self.actualizarPantalla()

        # Comprobar victoria
        if all(l in self.letrasAcertadas for l in self.palabraSecreta):
            self.lblMensaje.config(text=f"¡FELICIDADES! ¡Has adivinado la palabra '{self.palabraSecreta}'!", fg="green")
            self.juegoTerminado = True
            self.btnProbar.config(state="disabled")
            self.entryLetra.config(state="disabled")

        # Comprobar derrota
        elif self.intentosRestantes <= 0:
            self.lblPalabra.config(text=" ".join(list(self.palabraSecreta)))
            self.lblMensaje.config(text=f"¡Has perdido! La palabra era '{self.palabraSecreta}'.", fg="red")
            self.juegoTerminado = True
            self.btnProbar.config(state="disabled")
            self.entryLetra.config(state="disabled")


if __name__ == "__main__":
    aplicacion1 = AplicacionAhorcado()
