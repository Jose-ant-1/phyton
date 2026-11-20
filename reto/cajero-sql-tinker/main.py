import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from Cajero import Cajero 

class Aplicacion:
    def __init__(self):
        self.cajero = Cajero()
        self.clienteActual = None

        self.ventana1 = tk.Tk()
        self.ventana1.title("Cajero Automático - MySQL & CRUD")
        self.ventana1.geometry("540x430")
        self.ventana1.resizable(False, False)

        self.cuaderno = ttk.Notebook(self.ventana1)
        self.cuaderno.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")

        self.pestana_operaciones()
        self.pestana_crud()

        self.refrescar_clientes()
        self.actualizarVista()
        self.ventana1.mainloop()

    # -----------------------------
    # PESTAÑA 1: OPERACIONES CAJERO
    # -----------------------------
    def pestana_operaciones(self):
        self.tab_op = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.tab_op, text="Operaciones")

        marco = ttk.LabelFrame(self.tab_op, text="Operación en cuenta")
        marco.grid(column=0, row=0, padx=15, pady=15, sticky="ew")

        tk.Label(marco, text="Cliente:").grid(column=0, row=0, padx=8, pady=8, sticky="e")
        self.combo_clientes = ttk.Combobox(marco, state="readonly", width=28)
        self.combo_clientes.grid(column=1, row=0, padx=8, pady=8, sticky="w")
        self.combo_clientes.bind("<<ComboboxSelected>>", self.on_seleccionar_cliente)

        self.btn_recargar = ttk.Button(marco, text="Actualizar lista", command=self.refrescar_clientes)
        self.btn_recargar.grid(column=2, row=0, padx=6, pady=8)

        self.lblClienteInfo = tk.Label(marco, text="", font=("Arial", 10, "bold"), fg="blue")
        self.lblClienteInfo.grid(column=0, row=1, columnspan=3, pady=6)

        self.lblCajeroInfo = tk.Label(marco, text="", font=("Arial", 10))
        self.lblCajeroInfo.grid(column=0, row=2, columnspan=3, pady=4)

        tk.Label(marco, text="Cantidad (€):").grid(column=0, row=3, padx=8, pady=10, sticky="e")
        self.entryCantidad = tk.Entry(marco, width=18)
        self.entryCantidad.grid(column=1, row=3, padx=8, pady=10, sticky="w")

        self.btnIngresar = tk.Button(
            marco, text="Ingresar Dinero", bg="#d4edda", command=self.ingresarDinero
        )
        self.btnIngresar.grid(column=0, row=4, padx=10, pady=8, sticky="ew")

        self.btnExtraer = tk.Button(
            marco, text="Extraer Dinero", bg="#f8d7da", command=self.extraerDinero
        )
        self.btnExtraer.grid(column=1, row=4, padx=10, pady=8, sticky="ew")

        self.lblMensaje = tk.Label(
            self.tab_op, text="Bienvenido al servicio del cajero.", wraplength=490, fg="black"
        )
        self.lblMensaje.grid(column=0, row=1, padx=15, pady=10)

    # -----------------------------
    # PESTAÑA 2: CRUD DE CLIENTES
    # -----------------------------
    def pestana_crud(self):
        self.tab_crud = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.tab_crud, text="Gestión Clientes (CRUD)")

        # Alta / Modificación / Baja
        marco_form = ttk.LabelFrame(self.tab_crud, text="Datos del cliente")
        marco_form.grid(column=0, row=0, padx=12, pady=10, sticky="ew")

        tk.Label(marco_form, text="ID (modif./borrar):").grid(column=0, row=0, padx=6, pady=5, sticky="e")
        self.var_id = tk.StringVar()
        tk.Entry(marco_form, textvariable=self.var_id, width=12).grid(column=1, row=0, padx=6, pady=5, sticky="w")

        tk.Label(marco_form, text="Nombre:").grid(column=0, row=1, padx=6, pady=5, sticky="e")
        self.var_nombre = tk.StringVar()
        tk.Entry(marco_form, textvariable=self.var_nombre, width=22).grid(column=1, row=1, padx=6, pady=5, sticky="w")

        tk.Label(marco_form, text="Saldo inicial (€):").grid(column=0, row=2, padx=6, pady=5, sticky="e")
        self.var_saldo = tk.StringVar()
        tk.Entry(marco_form, textvariable=self.var_saldo, width=15).grid(column=1, row=2, padx=6, pady=5, sticky="w")

        ttk.Button(marco_form, text="Crear (Insert)", command=self.crear_cliente).grid(
            column=2, row=0, padx=6, pady=4, sticky="ew"
        )
        ttk.Button(marco_form, text="Renombrar (Update)", command=self.modificar_cliente).grid(
            column=2, row=1, padx=6, pady=4, sticky="ew"
        )
        ttk.Button(marco_form, text="Eliminar (Delete)", command=self.eliminar_cliente).grid(
            column=2, row=2, padx=6, pady=4, sticky="ew"
        )

        # Listado (Read)
        marco_lista = ttk.LabelFrame(self.tab_crud, text="Clientes registrados (Read)")
        marco_lista.grid(column=0, row=1, padx=12, pady=6, sticky="ew")

        ttk.Button(marco_lista, text="Listar todos", command=self.listar_clientes).grid(
            column=0, row=0, padx=6, pady=4, sticky="w"
        )
        self.area_clientes = st.ScrolledText(marco_lista, width=56, height=8)
        self.area_clientes.grid(column=0, row=1, padx=6, pady=6)

    # -----------------------------
    # LÓGICA DE INTERFAZ
    # -----------------------------
    def refrescar_clientes(self):
        clientes = self.cajero.listarClientes()
        self._mapa_combo = {f"{c.id} - {c.nombre}": c for c in clientes}
        valores = list(self._mapa_combo.keys())
        self.combo_clientes["values"] = valores

        if valores:
            if self.clienteActual:
                # Intentar mantener el mismo cliente si sigue existiendo
                actualizado = self.cajero.buscarClientePorId(self.clienteActual.id)
                if actualizado:
                    self.clienteActual = actualizado
                    self.combo_clientes.set(f"{actualizado.id} - {actualizado.nombre}")
                else:
                    self.clienteActual = self._mapa_combo[valores[0]]
                    self.combo_clientes.set(valores[0])
            else:
                self.clienteActual = self._mapa_combo[valores[0]]
                self.combo_clientes.set(valores[0])
        else:
            self.clienteActual = None
            self.combo_clientes.set("")

        self.listar_clientes()
        self.actualizarVista()

    def on_seleccionar_cliente(self, event=None):
        clave = self.combo_clientes.get()
        if clave in self._mapa_combo:
            self.clienteActual = self._mapa_combo[clave]
            self.lblMensaje.config(text=f"Cuenta seleccionada: {self.clienteActual.nombre}", fg="black")
            self.actualizarVista()

    def actualizarVista(self):
        if self.clienteActual:
            self.lblClienteInfo.config(
                text=f"Cliente: {self.clienteActual.nombre} (ID {self.clienteActual.id}) | Saldo: {self.clienteActual.saldo}€"
            )
        else:
            self.lblClienteInfo.config(text="Cliente: Ninguno seleccionado | Saldo: -")
        self.lblCajeroInfo.config(text=f"Efectivo en Cajero: {self.cajero.saldoCajero}€")

    def obtenerCantidad(self):
        try:
            texto = self.entryCantidad.get().strip()
            return int(texto)
        except ValueError:
            return None

    def ingresarDinero(self):
        if not self.clienteActual:
            self.lblMensaje.config(text="Error: No hay ningún cliente seleccionado.", fg="red")
            return
        cant = self.obtenerCantidad()
        if cant is None:
            self.lblMensaje.config(text="Error: Introduce un número entero válido.", fg="red")
            return
        exito, msg = self.cajero.ingresar(self.clienteActual, cant)
        self.lblMensaje.config(text=msg, fg="green" if exito else "red")
        self.entryCantidad.delete(0, tk.END)
        self.refrescar_clientes()

    def extraerDinero(self):
        if not self.clienteActual:
            self.lblMensaje.config(text="Error: No hay ningún cliente seleccionado.", fg="red")
            return
        cant = self.obtenerCantidad()
        if cant is None:
            self.lblMensaje.config(text="Error: Introduce un número entero válido.", fg="red")
            return
        exito, msg = self.cajero.extraer(self.clienteActual, cant)
        self.lblMensaje.config(text=msg, fg="green" if exito else "red")
        self.entryCantidad.delete(0, tk.END)
        self.refrescar_clientes()

    def crear_cliente(self):
        nombre = self.var_nombre.get()
        try:
            saldo = int(self.var_saldo.get().strip())
        except ValueError:
            mb.showwarning("Aviso", "Introduce un saldo inicial entero válido.")
            return

        exito, msg = self.cajero.crearCliente(nombre, saldo)
        mb.showinfo("Resultado", msg) if exito else mb.showwarning("Aviso", msg)
        if exito:
            self.var_nombre.set("")
            self.var_saldo.set("")
            self.refrescar_clientes()

    def modificar_cliente(self):
        try:
            id_cli = int(self.var_id.get().strip())
        except ValueError:
            mb.showwarning("Aviso", "Introduce un ID numérico válido.")
            return

        exito, msg = self.cajero.modificarNombreCliente(id_cli, self.var_nombre.get())
        mb.showinfo("Resultado", msg) if exito else mb.showwarning("Aviso", msg)
        if exito:
            self.var_nombre.set("")
            self.refrescar_clientes()

    def eliminar_cliente(self):
        try:
            id_cli = int(self.var_id.get().strip())
        except ValueError:
            mb.showwarning("Aviso", "Introduce un ID numérico válido.")
            return

        if not mb.askyesno("Confirmar", f"¿Seguro que deseas eliminar al cliente con ID {id_cli}?"):
            return

        exito, msg = self.cajero.eliminarCliente(id_cli)
        mb.showinfo("Resultado", msg) if exito else mb.showwarning("Aviso", msg)
        if exito:
            self.var_id.set("")
            self.refrescar_clientes()

    def listar_clientes(self):
        clientes = self.cajero.listarClientes()
        self.area_clientes.delete("1.0", tk.END)
        if not clientes:
            self.area_clientes.insert(tk.END, "No hay clientes registrados en la base de datos.\n")
            return
        for c in clientes:
            self.area_clientes.insert(tk.END, f"ID: {c.id} | Nombre: {c.nombre} | Saldo: {c.saldo}€\n")


if __name__ == "__main__":
    aplicacion1 = Aplicacion()