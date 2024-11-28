from flask import Blueprint, render_template, current_app
from flask_login import login_required, current_user

heladeria_blueprint = Blueprint('heladeria_bp', __name__, url_prefix="/")

@heladeria_blueprint.route('/ingredientes')
@login_required
def ingredientes():
    if not current_user.es_admin and not current_user.es_empleado:
        return render_template('NoAutorizado.html')

    heladeria = current_app.config['Heladeria']
    return render_template("ingredientes.html", ingredientes = heladeria.ingredientes)

@heladeria_blueprint.route('/productos_publico')
def productosPublico():
    heladeria = current_app.config['Heladeria']
    return render_template("productosSimple.html", productos = heladeria.productos)

@heladeria_blueprint.route('/productos')
@login_required
def productos():
    heladeria = current_app.config['Heladeria']
    return render_template("productos.html", productos = heladeria.productos)

@heladeria_blueprint.route('/abastecer')
@login_required
def abastecer():
    if not current_user.es_admin and not current_user.es_empleado:
        return render_template('NoAutorizado.html')

    try:
        heladeria = current_app.config['Heladeria']
        heladeria.abastecer_inventario()
        return render_template('Success.html', mensaje = f"Se abasteció el inventario 📦")
    except Exception as e:
        return render_template('Error.html', mensaje = f"Error {str(e)}")

@heladeria_blueprint.route('/renovarInventario')
@login_required
def renovarInventario():
    if not current_user.es_admin and not current_user.es_empleado:
        return render_template('NoAutorizado.html')

    try:
        heladeria = current_app.config['Heladeria']
        heladeria.renovar_inventario()
        return render_template('Success.html', mensaje = f"Se renovó el inventario de complementos 🫗")
    except Exception as e:
        return render_template('Error.html', mensaje = f"Error {str(e)}")

@heladeria_blueprint.route('/vender')
@login_required
def venderLista():
    heladeria = current_app.config['Heladeria']
    return render_template("productosVenta.html", productos = heladeria.productos)

@heladeria_blueprint.route('/productoMasRentable')
@login_required
def productoMasRentable():
     try:
         if not current_user.es_admin:
            return render_template('NoAutorizado.html')

         heladeria = current_app.config['Heladeria']
         producto_mas_rentable = heladeria.obtener_producto_mas_rentable().get("nombre", "")
         rentabilidad = heladeria.obtener_producto_mas_rentable().get("rentabilidad", "")
         return render_template('Success.html', mensaje = f"El producto más rentable es {producto_mas_rentable}, rentabilidad: {"${:,.0f}".format(rentabilidad)}")
     except Exception as e:
        return render_template('Error.html', mensaje = f"Error {str(e)}")

@heladeria_blueprint.route('/vender/<idProducto>')
@login_required
def vender(idProducto):
    try:
        heladeria = current_app.config['Heladeria']
        for producto in heladeria.productos:
            if producto.id == int(idProducto):
                ingrediente_faltante = producto.obtener_ingrediente_faltante()
                if ingrediente_faltante != None:
                    return render_template('Warning.html', mensaje = f"“¡Oh no! Nos hemos quedado sin {ingrediente_faltante.nombre} 😥 para hacer {producto.nombre}")
                vendido = heladeria.vender_producto(producto)
                if vendido:
                    return render_template('Success.html', mensaje = f"¡Vendido el producto {producto.nombre}!")
                else:
                    return render_template('Warning.html', mensaje = f"No se pudo vender el producto {producto.nombre}")
        return render_template('Warning.html', mensaje = f"No se encontró el producto {idProducto}")
    except Exception as e:
        return render_template('Error.html', mensaje = f"Error {str(e)}")
