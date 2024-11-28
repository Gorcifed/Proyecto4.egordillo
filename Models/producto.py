from db import db
from sqlalchemy import text, ForeignKey
from funciones import *
from Models.ingrediente import Ingrediente
from sqlalchemy.ext.hybrid import hybrid_property
from marshmallow import Schema, fields

# Clase que representa el producto
class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key = True)
    _nombre = db.Column("nombre", db.String(45), nullable = False)
    _precio = db.Column("precio", db.Integer, nullable = False)
    id_ingrediente1 = db.Column(db.Integer, nullable=False)
    id_ingrediente2 = db.Column(db.Integer, nullable=False)
    id_ingrediente3 = db.Column(db.Integer, nullable=False)
    _tipo = db.Column("tipo", db.String(15), nullable = False)
    _ingredientes = None
    _ventas_dia = 0
    _precio_ventas_dia = 0

    # Método que permite calcular el costo del producto
    def calcular_costo(self) -> int:
        lista = []
        if(self.tipo == 'Copa'):
            for ingrediente in self.ingredientes:
                lista.append({"nombre": ingrediente.nombre, "precio": ingrediente.precio})
            costo = calcular_costo_produccion_producto(lista)
            return costo
        # Es malteada
        for ingrediente in self.ingredientes:
            lista.append({"nombre": ingrediente.nombre, "precio": ingrediente.precio})

        costo = calcular_costo_produccion_producto(lista) + 500
        return costo

    # Método que permite calcular las calorías
    def calcular_calorias(self) -> float:
        calorias = decimal.Decimal(0.0)
        for ingrediente in self.ingredientes:
            calorias = calorias + ingrediente.calorias

        if self.tipo == 'Copa':
            return round(calorias, 2)
        
        # Es malteada
        return round(calorias, 2) + decimal.Decimal(200)

    # Método que permite calcular la rentabilidad del producto
    def calcular_rentabilidad(self) -> int:
        return self.precio - self.calcular_costo()

    # Método que determina si hay suficientes ingredientes para hacer el producto
    def calcular_ingredientes(self) -> bool:
        for ingrediente in self.ingredientes:
            if ingrediente.tipo == 'Complemento':
                if ingrediente.inventario < 1:
                    return False
            else: # Es Base
                if ingrediente.inventario < .2:
                    return False
        return True
    
     # Método que returna el ingrediente faltante de un producto, None si hay suficiente
    
    # Método que retorna el primer ingrediente faltante
    def obtener_ingrediente_faltante(self) -> Ingrediente:
        for ingrediente in self.ingredientes:
            if ingrediente.tipo == 'Complemento':
                if ingrediente.inventario < 1:
                     return ingrediente
            else: # Es Base
                if ingrediente.inventario < .2:
                    return ingrediente
        return None

    # Método que permite abastecer el inventario de ingredientes
    def abastecer_inventario(self):
        for ingrediente in self.ingredientes:
            ingrediente.abastecer()

    # Método que permite renovar el inventario de ingredientes
    def renovar_inventario(self):
        for ingrediente in self.ingredientes:
            ingrediente.renovar_inventario()

    @hybrid_property
    def nombre(self) -> str:
        """ Devuelve el valor del atributo privado 'nombre' """
        return self._nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'nombre'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self._nombre = value
        else:
            raise ValueError('Expected str')

    @hybrid_property
    def precio(self) -> int:
        """ Devuelve el valor del atributo privado 'precio' """
        return self._precio
    
    @precio.setter
    def precio(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'precio'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self._precio = value
        else:
            raise ValueError('Expected int')
        
    @hybrid_property
    def tipo(self) -> str:
        """ Devuelve el valor del atributo privado 'tipo' """
        return self._tipo
    
    @tipo.setter
    def tipo(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'tipo'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self._tipo = value
        else:
            raise ValueError('Expected str')

    @property
    def ingredientes(self) -> list:
        """ Devuelve el valor del atributo privado 'ingredientes' """
        return self._ingredientes

    @ingredientes.setter
    def ingredientes(self, value:list) -> None:
        """
        Establece un nuevo valor para el atributo privado 'ingredientes'

        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, list):
            self._ingredientes = value
        else:
            raise ValueError('Expected list')
    
    @property
    def ventas_dia(self) -> int:
        """ Devuelve el valor del atributo privado 'ventas_dia' """
        return self._ventas_dia
    
    @ventas_dia.setter
    def ventas_dia(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'ventas_dia'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self._ventas_dia = value
        else:
            raise ValueError('Expected int')
        
    @property
    def precio_ventas_dia(self) -> int:
        """ Devuelve el valor del atributo privado 'precio_ventas_dia' """
        return self._precio_ventas_dia
    
    @precio_ventas_dia.setter
    def precio_ventas_dia(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'precio_ventas_dia'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self._precio_ventas_dia = value
        else:
            raise ValueError('Expected int')

class ProductoEsquema(Schema):
    id = fields.Int(dump_only = True)
    nombre = fields.Str()
    precio = fields.Int()
    tipo = fields.Str()