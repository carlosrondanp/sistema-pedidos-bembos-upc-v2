import ipywidgets as widgets
from IPython.display import display, clear_output
from utils.analisis import generar_analisis_estadistico, generar_grafico_barras
from utils.reportes import generar_reporte
from controladores.base_datos_usuarios import BaseDatosUsuarios
from controladores.sistema_pedidos import SistemaPedidos

class InterfazUsuario:
    def __init__(self):
        self.base_datos_usuarios = BaseDatosUsuarios()
        self.sistema_pedidos = SistemaPedidos()
        self.usuario_actual = None
        self.output = widgets.Output()
        self._crear_interfaz_login()

    def _crear_interfaz_login(self):
        clear_output(wait=True)
        with self.output:
            clear_output(wait=True)
            usuario_label = widgets.Label("Usuario:")
            self.usuario_entry = widgets.Text(placeholder="Ingrese su usuario")

            contrasena_label = widgets.Label("Contraseña:")
            self.contrasena_entry = widgets.Password(placeholder="Ingrese su contraseña")

            iniciar_sesion_button = widgets.Button(description="Iniciar Sesión", button_style="success")
            iniciar_sesion_button.on_click(self.iniciar_sesion)

            login_ui = widgets.VBox([
                usuario_label, self.usuario_entry,
                contrasena_label, self.contrasena_entry,
                iniciar_sesion_button
            ])
            display(login_ui)

    def iniciar_sesion(self, _):
        nombre = self.usuario_entry.value
        contrasena = self.contrasena_entry.value
        usuario = self.base_datos_usuarios.validar_usuario(nombre, contrasena)

        with self.output:
            clear_output()
            if usuario:
                self.usuario_actual = usuario
                print(f"Bienvenido, {usuario.nombre} ({usuario.rol})")
                self._mostrar_funcionalidades(usuario.rol)
            else:
                print("Error: Usuario o contraseña incorrectos")

    def _mostrar_funcionalidades(self, rol):
        clear_output(wait=True)
        with self.output:
            if rol == "Gerente":
                self._crear_interfaz_gerente()
            elif rol == "Cajero":
                self._crear_interfaz_cajero()

    def _crear_interfaz_gerente(self):
        opciones_label = widgets.Label("Opciones para Gerente:")

        ver_analisis_button = widgets.Button(description="Ver Análisis", button_style="info")
        ver_analisis_button.on_click(self.ver_analisis)

        generar_reporte_button = widgets.Button(description="Generar Reporte", button_style="warning")
        generar_reporte_button.on_click(self.generar_reporte)

        cerrar_sesion_button = widgets.Button(description="Cerrar Sesión", button_style="danger")
        cerrar_sesion_button.on_click(self._crear_interfaz_login)

        gerente_ui = widgets.VBox([
            opciones_label,
            ver_analisis_button,
            generar_reporte_button,
            cerrar_sesion_button
        ])
        display(gerente_ui)

    def _crear_interfaz_cajero(self):
        opciones_label = widgets.Label("Opciones para Cajero:")

        registrar_pedido_button = widgets.Button(description="Registrar Pedido", button_style="info")
        registrar_pedido_button.on_click(self.registrar_pedido)

        ver_registro_button = widgets.Button(description="Ver Pedidos", button_style="info")
        ver_registro_button.on_click(self.ver_registro)

        cerrar_sesion_button = widgets.Button(description="Cerrar Sesión", button_style="danger")
        cerrar_sesion_button.on_click(self._crear_interfaz_login)

        cajero_ui = widgets.VBox([
            opciones_label,
            registrar_pedido_button,
            ver_registro_button,
            cerrar_sesion_button
        ])
        display(cajero_ui)

    def registrar_pedido(self, _):
        clear_output()
        with self.output:
            codigo_entry = widgets.Text(placeholder="Código del pedido")
            producto_entry = widgets.Text(placeholder="Producto")
            cantidad_entry = widgets.IntText(placeholder="Cantidad")
            precio_entry = widgets.FloatText(placeholder="Precio por kg")

            registrar_button = widgets.Button(description="Registrar", button_style="success")

            def registrar(_):
                try:
                    codigo = codigo_entry.value
                    producto = producto_entry.value
                    cantidad = cantidad_entry.value
                    precio_kg = precio_entry.value
                    self.sistema_pedidos.agregar_pedido(codigo, producto, cantidad, precio_kg)
                    print("Pedido registrado con éxito.")
                except ValueError:
                    print("Error: Por favor ingresa datos válidos.")

            registrar_button.on_click(registrar)

            registrar_ui = widgets.VBox([
                widgets.Label("Registrar Pedido"),
                codigo_entry, producto_entry, cantidad_entry, precio_entry, registrar_button
            ])
            display(registrar_ui)

    def ver_registro(self, _):
        clear_output()
        with self.output:
            pedidos = self.sistema_pedidos.obtener_registro()

            if pedidos.empty:
                print("No hay pedidos registrados.")
            else:
                print("Pedidos Registrados:")
                for _, pedido in pedidos.iterrows():
                    texto_pedido = f"{pedido['Codigo']} - {pedido['Producto']} - {pedido['Cantidad']} kg - S/ {pedido['Precio']}"
                    print(texto_pedido)

    def ver_analisis(self, _):
        generar_analisis_estadistico()
        generar_grafico_barras()
        print("Análisis generado.")

    def generar_reporte(self, _):
        generar_reporte()
        print("Reporte generado correctamente.")