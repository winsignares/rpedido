from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.Repartidor import Repartidor, RepartidorSchema
from Model.RegistroPedido import RegistroPedido
from Model.Productos import Productos
from Model.Proveedores import Proveedores
from Model.Clientes import Clientes


routes_Repartidor = Blueprint("routes_Repartidor", __name__)

#Repartidor - Schema 
Repartidor_schema = RepartidorSchema()
Repartidor_Schema = RepartidorSchema(many=True)


@routes_Repartidor.route('/Guardar_Repartidor', methods=['POST'] )
def Guardar_Repartid():
    
    NombreC = request.form['NombreC']
    Email = request.form['Email']
    password = request.form['password']
    usuario = request.form['usuario']
    telefono = request.form['telefono']
    # problema = date.today()
    print(NombreC)
    new_rep = Repartidor( NombreC,Email,password,usuario,telefono)
    db.session.add(new_rep)
    db.session.commit()
    return "Si"


@routes_Repartidor.route('/eliminarss', methods=['POST'])
def eliminars():
    # Obtener el ID del registro de pedido a eliminar desde la solicitud POST
    id_registro = request.json['id']

    # Lógica para eliminar el registro de pedido en la base de datos
    registro = RegistroPedido.query.get(id_registro)  # Busca el registro de pedido por ID
    if registro:
        db.session.delete(registro)  # Elimina el registro de pedido
        db.session.commit()  # Confirma los cambios en la base de datos
        return jsonify({'message': 'Registro de pedido eliminado correctamente'})
    else:
        return jsonify({'message': 'Registro de pedido no encontrado'})


    