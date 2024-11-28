import math
import locale
import decimal

# Función que determina si un ingrediente es sano
# calorias: Calorias totales del producto
# es_vegetariano: Determina si el ingrediente es vegetariano
# return: determina si el ingrediente es sano
def es_sano_ingrediente(calorias: decimal.Decimal, es_vegetariano: bool):
    if isinstance(calorias, decimal.Decimal):
        if isinstance(es_vegetariano, bool):
            return es_vegetariano or calorias < decimal.Decimal(100)
        else:
            raise ValueError('Expected bool')
    else:
        raise ValueError('Expected int')

# Función que permite calcular la suma de calorías de un producto
# calorias: lista con los diccionarios de ingredientes
# multiplicarFactor: determina si el valor se multiplica por .95
# return: calorías totales redondeadas a 2 decimales
def calcular_calorias_producto(calorias: list, multiplicarFactor: bool) -> float:
    acumulador = 0.0
    if isinstance(calorias, list):
        for valor in calorias:
            if isinstance(valor, float):
                acumulador = acumulador + valor
    else:
        raise ValueError('Expected list')
    factor = 1.0
    if multiplicarFactor:
        factor = .95
    return round(acumulador * factor, 2)

# Función que permite calcular el valor de producción de un producto
# ingredientes: lista de ingredientes a calcular
# return: total de costo de producción
def calcular_costo_produccion_producto(ingredientes: list)-> int:
    acumulador = 0
    if isinstance(ingredientes, list):
        for ingrediente in ingredientes:
            if isinstance(ingrediente, dict):
                valor = ingrediente.get("precio", 0)
                acumulador = acumulador + valor
    else:
        raise ValueError('Expected list')

    return acumulador

# Función que permite calcular la rentabilidad de un producto
# precio_producto: precio de venta del producto
# ingredientes: lista de ingredientes a calcular
# return: valor de rentabilidad
def calcular_rentabilidad_producto(precio_producto: int, ingredientes: list) -> int:
    precio_ingredientes = calcular_costo_produccion_producto(ingredientes)
    return precio_producto - precio_ingredientes

# Método que a partir de una lista de productos determina cuál es el más rentable
# productos: Lista de productos a evaluar
def calcular_producto_mas_rentable(productos: list):
    if not isinstance(productos, list):
        raise ValueError('Expected list')

    productoMasRentable = None
    for producto in productos:
        if isinstance(producto, dict):
            rentabilidad = producto.get("rentabilidad", 0)
            if productoMasRentable == None:
                productoMasRentable = producto
            else:
                rentabilidadAnterior = productoMasRentable.get("rentabilidad", 0)
                if rentabilidad > rentabilidadAnterior:
                    productoMasRentable = producto

    return productoMasRentable

def formatear_moneda(numero):
    """Formatea un número como moneda sin decimales, adaptándose a la configuración regional.

    Args:
        numero (float): El número a formatear.

    Returns:
        str: El número formateado como moneda.
    """

    locale.setlocale(locale.LC_ALL, '')  # Utiliza la configuración regional del sistema
    return locale.currency(numero, grouping = True)