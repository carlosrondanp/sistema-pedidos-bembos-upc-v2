import tkinter as tk
from tkinter import messagebox
from utils.analisis import generar_analisis_estadistico, generar_grafico_barras
from utils.reportes import generar_reporte
from controladores.base_datos_usuarios import BaseDatosUsuarios
from controladores.sistema_pedidos import SistemaPedidos

class InterfazUsuario:
    def __init__(self):
        self.base_datos_usuarios = BaseDatosUsuarios()
        self.sistema_pedidos = SistemaPedidos()
        self.usuario_actual = None
        self.root = tk.Tk()
        self.root.title("Sistema de Pedidos - Login")
        self._crear_interfaz_login()

    def _crear_interfaz_login(self):
        frame_login = tk.Frame(self.root)
        frame_login.pack(pady=20)

        tk.Label(frame_login, text="Usuario").grid(row=0, column=0, padx=5, pady=5)
        self.usuario_entry = tk.Entry(frame_login)
        self.usuario_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_login, text="Contraseña").grid(row=1, column=0, padx=5, pady=5)
        self.contrasena_entry = tk.Entry(frame_login, show="*")
        self.contrasena_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(frame_login, text="Iniciar Sesión", command=self.iniciar_sesion).grid(row=2, column=0, columnspan=2, pady=10)

    def iniciar_sesion(self):
        # Verificar credenciales
        nombre = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()
        usuario = self.base_datos_usuarios.validar_usuario(nombre, contrasena)

        if usuario:
            self.usuario_actual = usuario
            messagebox.showinfo("Inicio de Sesión", f"Bienvenido, {usuario.nombre} ({usuario.rol})")
            self._mostrar_funcionalidades(usuario.rol)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def _mostrar_funcionalidades(self, rol):
        # Limpiar la pantalla anterior
        for widget in self.root.winfo_children():
            widget.destroy()

        if rol == "Gerente":
            self._crear_interfaz_gerente()
        elif rol == "Cajero":
            self._crear_interfaz_cajero()

    def _crear_interfaz_gerente(self):
        frame_gerente = tk.Frame(self.root)
        frame_gerente.pack(pady=20)

        tk.Label(frame_gerente, text="Opciones para Gerente").pack(pady=10)
        tk.Button(frame_gerente, text="Ver Análisis", command=self.ver_analisis).pack(pady=5)
        tk.Button(frame_gerente, text="Generar Reporte", command=self.generar_reporte).pack(pady=5)
        tk.Button(frame_gerente, text="Cerrar Sesión", command=self.cerrar_sesion).pack(pady=5)

    def _crear_interfaz_cajero(self):
        frame_cajero = tk.Frame(self.root)
        frame_cajero.pack(pady=20)

        tk.Label(frame_cajero, text="Opciones para Cajero").pack(pady=10)
        tk.Button(frame_cajero, text="Registrar Pedido", command=self.registrar_pedido).pack(pady=5)
        tk.Button(frame_cajero, text="Ver Pedidos", command=self.ver_registro).pack(pady=5)
        tk.Button(frame_cajero, text="Cerrar Sesión", command=self.cerrar_sesion).pack(pady=5)

    def registrar_pedido(self):
        ventana_registro = tk.Toplevel(self.root)
        ventana_registro.title("Registrar Pedido")

        tk.Label(ventana_registro, text="Código").grid(row=0, column=0, padx=5, pady=5)
        codigo_entry = tk.Entry(ventana_registro)
        codigo_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(ventana_registro, text="Producto").grid(row=1, column=0, padx=5, pady=5)
        producto_entry = tk.Entry(ventana_registro)
        producto_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(ventana_registro, text="Cantidad").grid(row=2, column=0, padx=5, pady=5)
        cantidad_entry = tk.Entry(ventana_registro)
        cantidad_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(ventana_registro, text="Precio por kg").grid(row=3, column=0, padx=5, pady=5)
        precio_entry = tk.Entry(ventana_registro)
        precio_entry.grid(row=3, column=1, padx=5, pady=5)

        def registrar():
            try:
                codigo = codigo_entry.get()
                producto = producto_entry.get()
                cantidad = int(cantidad_entry.get())
                precio_kg = float(precio_entry.get())
                self.sistema_pedidos.agregar_pedido(codigo, producto, cantidad, precio_kg)
                messagebox.showinfo("Éxito", "Pedido registrado con éxito.")
                ventana_registro.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor ingresa datos válidos.")

        tk.Button(ventana_registro, text="Registrar", command=registrar).grid(row=4, column=0, columnspan=2, pady=10)

    def ver_registro(self):
        pedidos = self.sistema_pedidos.obtener_registro()
        
        if pedidos.empty:
            messagebox.showinfo("Registro Vacío", "No hay pedidos registrados.")
            return
        
        ventana_pedidos = tk.Toplevel(self.root)
        ventana_pedidos.title("Registro de Pedidos")

        tk.Label(ventana_pedidos, text="Pedidos Registrados").pack(pady=10)
        for _, pedido in pedidos.iterrows():
            texto_pedido = f"{pedido['Codigo']} - {pedido['Producto']} - {pedido['Cantidad']} kg - S/ {pedido['Precio']}"
            tk.Label(ventana_pedidos, text=texto_pedido).pack()

    def ver_analisis(self):
        generar_analisis_estadistico()
        generar_grafico_barras()

    def generar_reporte(self):
        generar_reporte()
        messagebox.showinfo("Éxito", "Reporte generado correctamente.")

    def cerrar_sesion(self):
        self.root.destroy()
        self.__init__()
        self.root.mainloop()

    def ejecutar(self):
        self.root.mainloop()