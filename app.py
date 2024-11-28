from flask import Flask,  render_template, request, redirect, url_for, session
from flask_login import LoginManager, login_user, login_required
from dotenv import load_dotenv
from db import db
from Controllers.controller_heladeria import *
from Controllers.controller_producto_api import *
from Controllers.controller_ingrediente_api import *
from Models.ingrediente import Ingrediente
from Models.producto import Producto
from Models.heladeria import Heladeria
from Models.usuario import Usuario
import os

load_dotenv(override=True)

def create_app():
    app = Flask(__name__, template_folder = "Views")
    DB_STRING_CONNECTION = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_STRING_CONNECTION
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    secret_key = os.urandom(24)
    app.config["SECRET_KEY"] = secret_key

    db.init_app(app)

    with app.app_context():
        ingredientes = Ingrediente.query.all()
        productos = Producto.query.all()

        for producto in productos:
            producto.ingredientes = []
            for ingrediente in ingredientes:
                if ingrediente.id == producto.id_ingrediente1:
                    producto.ingredientes.append(ingrediente)
                elif ingrediente.id == producto.id_ingrediente2:
                    producto.ingredientes.append(ingrediente)
                elif ingrediente.id == producto.id_ingrediente3:
                    producto.ingredientes.append(ingrediente)

        heladeria = Heladeria('Disney', ingredientes, productos)
        app.config['Heladeria'] = heladeria

    return app

app = create_app()

login_manager =  LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    for user in Usuario.query.all():
        if user.id == int(user_id):
            return user
    return None

@app.template_filter()
def currencyFormat(value):
    value = float(value)
    return "${:,.0f}".format(value)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/indice')
@login_required
def indice():
    usuario = current_user
    return render_template('indice.html', usuario= usuario)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        for user in Usuario.query.all():
            if user.alias == username and user.contrasena == password:
                print(f"user.alias: {user.alias}, admin: {user.es_admin}, empleado: {user.es_empleado}" )
                login_user(user)
                if(user.es_admin == 1):
                    return redirect(url_for("indice"))
                return redirect(url_for("indice"))
        return render_template("login.html")

@app.route("/logout")
def logout():
    # Clear the session
    session.clear()
    return redirect("/")

app.register_blueprint(heladeria_blueprint)
app.register_blueprint(api_producto_blueprint)
app.register_blueprint(api_ingrediente_blueprint)

if __name__ == '__main__':
    app.run(debug=True)