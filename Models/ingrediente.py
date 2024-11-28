from db import db
from sqlalchemy import text
from funciones import *
import decimal
from sqlalchemy.ext.hybrid import hybrid_property
from marshmallow import Schema, fields

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key = True)
    _nombre = db.Column("nombre", db.String(45), nullable = False)
    _precio = db.Column("precio", db.Integer, nullable = False)
    _calorias = db.Column("calorias", db.NUMERIC(5,2), nullable = False)
    _vegetariano = db.Column("vegetariano", db.Integer, nullable = False)
    _inventario = db.Column("inventario", db.NUMERIC(5,2), nullable = False)
    _tipo = db.Column("tipo", db.String(15), nullable = False)
    _sabor = db.Column("sabor", db.String(45), nullable = False)

    #Método que determina si un ingrediente es sano
    def es_sano(self) -> bool:
        vegetariano = False
        if self.vegetariano==1:
            vegetariano = True
        return es_sano_ingrediente(self.calorias, vegetariano)

    # Método que permite abastecer un ingrediente
    def abastecer(self) -> None:
        if self.tipo == 'Complemento':
             self.inventario = self.inventario + decimal.Decimal(10.0)
             return
        # Es base
        self.inventario = self.inventario + decimal.Decimal(5.0)

    # Método que permite renovar el inventario
    def renovar_inventario(self):
        self._inventario = decimal.Decimal(0.0)

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
    def calorias(self) -> decimal.Decimal:
        """ Devuelve el valor del atributo privado 'calorias' """
        return self._calorias
    
    @calorias.setter
    def calorias(self, value: decimal.Decimal) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'calorias'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, decimal.Decimal):
            self._calorias = value
        else:
            raise ValueError('Expected decimal')
    
    @property
    def vegetariano(self) -> int:
        """ Devuelve el valor del atributo privado 'vegetariano' """
        return self._vegetariano
    
    @vegetariano.setter
    def vegetariano(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'vegetariano'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self._vegetariano = value
        else:
            raise ValueError('Expected int')
        
    @property
    def inventario(self) -> decimal.Decimal:
        """ Devuelve el valor del atributo privado 'inventario' """
        return self._inventario
    
    @inventario.setter
    def inventario(self, value: decimal.Decimal) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'inventario'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, decimal.Decimal):
            self._inventario = value
        else:
            raise ValueError('Expected decimal')
    
    @property
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
    def sabor(self) -> str:
        """ Devuelve el valor del atributo privado 'sabor' """
        return self._sabor
    
    @sabor.setter
    def sabor(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'sabor'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self._sabor = value
        else:
            raise ValueError('Expected str')
        
class IngredienteEsquema(Schema):
    id = fields.Int(dump_only = True)
    nombre = fields.Str()
    precio = fields.Int()
    calorias = fields.Float()
    sabor = fields.Str()
    vegetariano = fields.Bool()
    tipo = fields.Str()