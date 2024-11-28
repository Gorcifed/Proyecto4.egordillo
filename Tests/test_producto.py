import unittest
from Models.producto import Producto
from Tests.baseTestCase import BaseTestCase

# Clase de prueba de Ingrediente
class TestProducto(BaseTestCase):
    # Método de prueba de funcionalidad es sano
    def test_calcular_calorias(self):
        calorias = self.heladeria.productos[5].calcular_calorias()
        self.assertEqual(calorias, 702)

        calorias = self.heladeria.productos[0].calcular_calorias()
        self.assertEqual(calorias, 140)
    
    # Método de prueba de cálculo de costo
    def test_calcular_costo(self):
        for producto in self.heladeria.productos:
            costo = 0
            for ingrediente in producto.ingredientes:
                costo = costo + ingrediente.precio
            if producto.tipo == "Malteada":
                costo = costo + 500 # valor del vaso
                self.assertEqual(producto.calcular_costo(), costo)
            else:
                self.assertEqual(producto.calcular_costo(), costo)

    # Método de prueba de cálculo de rentabilidad
    def test_calcular_rentabilidad(self):
        for producto in self.heladeria.productos:
            costo = 0
            for ingrediente in producto.ingredientes:
                costo = costo + ingrediente.precio
            if producto.tipo == "Malteada":
                costo = costo + 500 # valor del vaso
                self.assertEqual(producto.calcular_rentabilidad(), producto.precio - costo)
            else:
                self.assertEqual(producto.calcular_rentabilidad(), producto.precio - costo)

if __name__ == '__main__':
    unittest.main()