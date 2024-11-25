# Sistema de Gestión de Pedidos

Este proyecto es una aplicación para la gestión de pedidos, diseñada para un negocio de ventas como Bembos. Permite a los usuarios autenticarse según su rol (Gerente o Cajero) y realizar funciones específicas como registrar pedidos, generar reportes y realizar análisis estadísticos.

## Funcionalidades

### Para Gerentes:
- **Ver análisis estadísticos**: Obtén estadísticas clave sobre los pedidos y gráficos visuales.
- **Generar reportes**: Crea un reporte detallado en formato CSV con datos relevantes.

### Para Cajeros:
- **Registrar pedidos**: Ingresa los datos de un nuevo pedido.
- **Ver pedidos registrados**: Consulta todos los pedidos realizados.

## Requisitos Previos

Asegúrate de tener instalados los siguientes elementos antes de ejecutar el proyecto:

- **Python 3.12.5**
- Bibliotecas requeridas:
  - `pandas`
  - `tk`
  - `openpyxl`
  - `matplotlib`
  - `pytest`

Para instalar las dependencias necesarias, ejecuta:

```bash
pip install pandas tk openpyxl matplotlib pytest