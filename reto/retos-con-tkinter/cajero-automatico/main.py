import tkinter as tk
from Cajero import Cajero

class Aplicacion:
    def __init__(self):
        self.cajero = Cajero()
        self.clienteActual = self.cajero.clientes[0]  # Por defecto Juan

        self.ventana1 = tk.Tk()
        self.ventana1.title("Cajero Automático")
        self.ventana1.geometry("450x380")
        self.ventana1.resizable(False, False)

        # Título
        self.lblTitulo = tk.Label(self.ventana1, text="CAJERO AUTOMÁTICO", font=("Arial", 14, "bold"))
        self.lblTitulo.grid(column=0, row=0, columnspan=2, pady=10)

        # Selección de cliente
        self.lblSeleccion = tk.Label(self.ventana1, text="Seleccionar cliente:")
        self.lblSeleccion.grid(column=0, row=1, sticky="w", padx=20, pady=5)

        self.btnJuan = tk.Button(self.ventana1, text="Cliente Juan", command=self.seleccionarJuan)
        self.btnJuan.grid(column=0, row=2, padx=20, pady=5, sticky="ew")

        self.btnAna = tk.Button(self.ventana1, text="Cliente Ana", command=self.seleccionarAna)
        self.btnAna.grid(column=1, row=2, padx=20, pady=5, sticky="ew")

        # Información de saldos
        self.lblClienteInfo = tk.Label(self.ventana1, text="", font=("Arial", 11, "bold"), fg="blue")
        self.lblClienteInfo.grid(column=0, row=3, columnspan=2, pady=5)

        self.lblCajeroInfo = tk.Label(self.ventana1, text="", font=("Arial", 10))
        self.lblCajeroInfo.grid(column=0, row=4, columnspan=2, pady=5)

        # Entrada de cantidad
        self.lblMonto = tk.Label(self.ventana1, text="Cantidad (€):")
        self.lblMonto.grid(column=0, row=5, padx=20, pady=10, sticky="e")

        self.entryCantidad = tk.Entry(self.ventana1, width=15)
        self.entryCantidad.grid(column=1, row=5, padx=20, pady=10, sticky="w")

        # Botones de operaciones
        self.btnIngresar = tk.Button(self.ventana1, text="Ingresar Dinero", bg="#d4edda", command=self.ingresarDinero)
        self.btnIngresar.grid(column=0, row=6, padx=20, pady=5, sticky="ew")

        self.btnExtraer = tk.Button(self.ventana1, text="Extraer Dinero", bg="#f8d7da", command=self.extraerDinero)
        self.btnExtraer.grid(column=1, row=6, padx=20, pady=5, sticky="ew")

        # Mensaje de resultado
        self.lblMensaje = tk.Label(self.ventana1, text="Bienvenido al servicio del cajero.", wraplength=400, fg="black")
        self.lblMensaje.grid(column=0, row=7, columnspan=2, pady=15)

        self.actualizarVista()
        self.ventana1.mainloop()

    def seleccionarJuan(self):
        self.clienteActual = self.cajero.buscarCliente("Juan")
        self.lblMensaje.config(text="Cuenta seleccionada: Juan", fg="black")
        self.actualizarVista()

    def seleccionarAna(self):
        self.clienteActual = self.cajero.buscarCliente("Ana")
        self.lblMensaje.config(text="Cuenta seleccionada: Ana", fg="black")
        self.actualizarVista()

    def actualizarVista(self):
        if self.clienteActual:
            self.lblClienteInfo.config(text=f"Cliente: {self.clienteActual.nombre} | Saldo: {self.clienteActual.saldo}€")
        self.lblCajeroInfo.config(text=f"Efectivo en Cajero: {self.cajero.saldoCajero}€")

    def obtenerCantidad(self):
        try:
            texto = self.entryCantidad.get().strip()
            cantidad = int(texto)
            return cantidad
        except ValueError:
            return None

    def ingresarDinero(self):
        cant = self.obtenerCantidad()
        if cant is None:
            self.lblMensaje.config(text="Error: Introduce un número entero válido.", fg="red")
            return
        exito, msg = self.cajero.ingresar(self.clienteActual, cant)
        self.lblMensaje.config(text=msg, fg="green" if exito else "red")
        self.entryCantidad.delete(0, tk.END)
        self.actualizarVista()

    def extraerDinero(self):
        cant = self.obtenerCantidad()
        if cant is None:
            self.lblMensaje.config(text="Error: Introduce un número entero válido.", fg="red")
            return
        exito, msg = self.cajero.extraer(self.clienteActual, cant)
        self.lblMensaje.config(text=msg, fg="green" if exito else "red")
        self.entryCantidad.delete(0, tk.END)
        self.actualizarVista()


if __name__ == "__main__":
    aplicacion1 = Aplicacion()
