import unittest
from Models.ingrediente import Ingrediente
from Tests.baseTestCase import BaseTestCase
import decimal

# Clase de prueba de Ingrediente
class TestIngrediente(BaseTestCase):
    # Método de prueba de funcionalidad es sano
    def test_es_sano(self):
        for ingrediente in self.heladeria.ingredientes:
            if ingrediente.vegetariano == True or ingrediente.calorias < decimal.Decimal(100):
                self.assertEqual(ingrediente.es_sano(), True)
            else:
                 self.assertEqual(ingrediente.es_sano(), False)

if __name__ == '__main__':
    unittest.main()