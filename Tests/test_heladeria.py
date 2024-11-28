import unittest
from Models.heladeria import Heladeria
from Tests.baseTestCase import BaseTestCase
import decimal

# Clase de prueba de heladeria
class TestHeladeria(BaseTestCase):
    # Método que prueba la funcionalidad deabastecer inventario
    def test_abastecer_inventario(self):
        inventario_frutasVarias = self.heladeria.ingredientes[6].inventario # complemento, inicialmente es 5
        inventario_HeladoVainilla = self.heladeria.ingredientes[3].inventario # base, inicialmente es .2

        self.heladeria.abastecer_inventario()
        self.assertEqual(self.heladeria.ingredientes[6].inventario, inventario_frutasVarias + 10)        
        self.assertEqual(self.heladeria.ingredientes[3].inventario, inventario_HeladoVainilla + decimal.Decimal(5))

    # Método que prueba la renovación de inventario
    def test_renovar_inventario(self):
        self.heladeria.renovar_inventario()
        for ingrediente in self.heladeria.ingredientes:
            if ingrediente.tipo == 'Complemento':
                    self.assertEqual(ingrediente.inventario, 0)

    # Método de prueba de producto más rentable
    def test_obtener_producto_mas_rentable(self):
        productoMasRentable = self.heladeria.obtener_producto_mas_rentable()        
        self.assertEqual(productoMasRentable.get("nombre"), "Malteada Deisy")
    
    # Método de prueba de venta de producto
    def test_vender_producto(self):
        for producto in self.heladeria.productos:
            if producto.calcular_ingredientes() == True:
                self.heladeria.vender_producto(producto)
                self.assertEqual(producto.ventas_dia, 1)
            else:
                try:
                    self.heladeria.vender_producto(producto)
                    self.fail("Se esperaba error")
                except ValueError:
                    self.assertEqual(producto.ventas_dia, 0)
                except  Exception:
                    self.fail("Se esperaba otro tipo de error")

if __name__ == '__main__':
    unittest.main()