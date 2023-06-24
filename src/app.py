from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma


#model
from Model.Repartidor import Repartidor
from Model.Clientes import Clientes
from Model.Productos import Productos
from Model.Proveedores import Proveedores
from Model.RegistroPedido import RegistroPedido

#rutas
from rutas.Clientes import routes_Cliente
from rutas.home import routes_home
from rutas.Repartidor import routes_Repartidor


app.register_blueprint(routes_Cliente, url_prefix='/fronted')
app.register_blueprint(routes_home, url_prefix='/fronted')
app.register_blueprint(routes_Repartidor, url_prefix='/fronted')

@app.route("/")
def index():
    titulo="Pagina Principal"
    return render_template('/main/index.html', titulo=titulo)    

# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')