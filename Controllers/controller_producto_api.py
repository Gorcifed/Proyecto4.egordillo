from flask import Blueprint, current_app,jsonify
from Models.producto import ProductoEsquema

api_producto_blueprint = Blueprint('api_prod_bp', __name__, url_prefix="/api/productos")

# Capacidad que retorna todos los productos
@api_producto_blueprint.route('/')
def productos():
    heladeria = current_app.config['Heladeria']
    producto_Esquema = ProductoEsquema(many=True)
    return jsonify({"data": producto_Esquema.dump(heladeria.productos)})

# Capacidad que retorna un producto por id
@api_producto_blueprint.route('/<idProducto>')
def producto_XId(idProducto):
    producto_Esquema = ProductoEsquema(many=False)
    heladeria = current_app.config['Heladeria']
    for producto in heladeria.productos:
        if producto.id == int(idProducto):
            return jsonify({"data": producto_Esquema.dump(producto)})

    return jsonify({"error": f"El producto con id {idProducto} no existe!"}), 404

# Capacidad que retorna un producto por nombre
@api_producto_blueprint.route('/nombre/<nombreProducto>')
def productoXNombre(nombreProducto):
    producto_Esquema = ProductoEsquema(many=False)
    heladeria = current_app.config['Heladeria']
    for producto in heladeria.productos:
        if producto.nombre == nombreProducto:
            return jsonify({"data": producto_Esquema.dump(producto)})

    return jsonify({"error": f"El producto con el nombre '{nombreProducto}' no existe!"}), 404

# Capacidad que retorna la calorías de un producto
@api_producto_blueprint.route('/calorias/<idProducto>')
def producto_calorias_XId(idProducto):
    heladeria = current_app.config['Heladeria']
    for producto in heladeria.productos:
        if producto.id == int(idProducto):
            return jsonify({"data": producto.calcular_calorias()})

    return jsonify({"error": f"El producto con id {idProducto} no existe!"}), 404

# Capacidad que retorna la rentabilidad de un producto
@api_producto_blueprint.route('/rentabilidad/<idProducto>')
def producto_rentabilidad_xId(idProducto):
    heladeria = current_app.config['Heladeria']
    for producto in heladeria.productos:
        if producto.id == int(idProducto):
            return jsonify({"data": producto.calcular_rentabilidad()})

    return jsonify({"error": f"El producto con id {idProducto} no existe!"}), 404

# Capacidad que retorna el costo de un producto
@api_producto_blueprint.route('/costo/<idProducto>')
def producto_costo_produccion_XId(idProducto):
    heladeria = current_app.config['Heladeria']
    for producto in heladeria.productos:
        if producto.id == int(idProducto):
            return jsonify({"data": producto.calcular_costo()})

    return jsonify({"error": f"El producto con id {idProducto} no existe!"}), 404

# Capacidad que permite vender un producto
@api_producto_blueprint.route('/vender/<idProducto>', methods = ["POST"])
def producto_vender_XId(idProducto):
    try:
        heladeria = current_app.config['Heladeria']
        for producto in heladeria.productos:
            if producto.id == int(idProducto):
                return jsonify({"data": heladeria.vender_producto(producto)})

        return jsonify({"error": f"El producto con id {idProducto} no existe!"}), 404
    except ValueError as val:
        return jsonify({"error": f"{val}"}), 405
    except Exception as err:
        return jsonify({"error": f"Unexpected {err=}, {type(err)=}"}), 500

# Capacidad que permite reabastecer un producto
@api_producto_blueprint.route('/reabastecer/<idProducto>', methods = ["PUT"])
def producto_reabastecer_XId(idProducto):
    try:
        heladeria = current_app.config['Heladeria']
        for producto in heladeria.productos:
            if producto.id == int(idProducto):
                producto.abastecer_inventario()
                return jsonify({"data": True})

        return jsonify({"error": f"El producto con id {idProducto} no existe!"}), 404
    except ValueError as val:
        return jsonify({"error": f"{val}"}), 405
    except Exception as err:
        return jsonify({"error": f"Unexpected {err=}, {type(err)=}"}), 500

# Capacidad que permite renovar el inventario un producto
@api_producto_blueprint.route('/renovar/<idProducto>', methods = ["PUT"])
def producto_renovar_XId(idProducto):
    try:
        heladeria = current_app.config['Heladeria']
        for producto in heladeria.productos:
            if producto.id == int(idProducto):
                producto.renovar_inventario()
                return jsonify({"data": True})

        return jsonify({"error": f"El producto con id {idProducto} no existe!"}), 404
    except ValueError as val:
        return jsonify({"error": f"{val}"}), 405
    except Exception as err:
        return jsonify({"error": f"Unexpected {err=}, {type(err)=}"}), 500