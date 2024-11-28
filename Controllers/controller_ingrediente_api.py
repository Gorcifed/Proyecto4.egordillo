from flask import Blueprint, current_app,jsonify
from Models.ingrediente import IngredienteEsquema

api_ingrediente_blueprint = Blueprint('api_ing_bp', __name__, url_prefix="/api/ingredientes")

# Capacidad que retorna todos los ingredientes
@api_ingrediente_blueprint.route('/')
def ingredientes():
    heladeria = current_app.config['Heladeria']
    ingrediente_Esquema = IngredienteEsquema(many=True)
    return jsonify({"data": ingrediente_Esquema.dump(heladeria.ingredientes)})

# Capacidad que retorna un ingrediente por id
@api_ingrediente_blueprint.route('/<idIngrediente>')
def ingrediente_XId(idIngrediente):
    ingrediente_Esquema = IngredienteEsquema(many=False)
    heladeria = current_app.config['Heladeria']
    for ingrediente in heladeria.ingredientes:
        if ingrediente.id == int(idIngrediente):
            return jsonify({"data": ingrediente_Esquema.dump(ingrediente)})

    return jsonify({"error": f"El ingrediente con id {idIngrediente} no existe!"}), 404

# Capacidad que retorna un ingrediente por nombre
@api_ingrediente_blueprint.route('/nombre/<nombreIngrediente>')
def ingrediente_XNombre(nombreIngrediente):
    ingrediente_Esquema = IngredienteEsquema(many=False)
    heladeria = current_app.config['Heladeria']
    for ingrediente in heladeria.ingredientes:
        if ingrediente.nombre == nombreIngrediente:
            return jsonify({"data": ingrediente_Esquema.dump(ingrediente)})

    return jsonify({"error": f"El ingrediente con el nombre '{nombreIngrediente}' no existe!"}), 404

# Capacidad que retorna si un ingrediente es sano
@api_ingrediente_blueprint.route('/essano/<idIngrediente>')
def ingrediente_essano_XId(idIngrediente):
    heladeria = current_app.config['Heladeria']
    for ingrediente in heladeria.ingredientes:
        if ingrediente.id == int(idIngrediente):
            return jsonify({"data": ingrediente.es_sano()})

    return jsonify({"error": f"El ingrediente con id {idIngrediente} no existe!"}), 404