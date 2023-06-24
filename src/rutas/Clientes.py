from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.Clientes import Clientes, ClientesSchema
from Model.Repartidor import Repartidor
from Model.RegistroPedido import RegistroPedido
from Model.Productos import Productos
from Model.Proveedores import Proveedores


routes_Cliente = Blueprint("routes_Cliente", __name__)

#CLIENTE - Schema 
Cliente_schema = ClientesSchema()
Clientes_Schema = ClientesSchema(many=True)




@routes_Cliente.route('/Guardar_Clientes', methods=['POST'])
def Guardar_Clientes():
    tipoPersona = request.form['tipoPersona']
    NombreC = request.form['NombreC']
    Email = request.form['Email']
    password = request.form['password']
    usuario = request.form['usuario']
    telefono = request.form['telefono']
    direccion = request.form['direccion'] if tipoPersona == 'PersonaNormal' else ''  # Obtener 'direccion' solo si es 'PersonaNormal', de lo contrario, asignar un valor predeterminado vacío
    
    if tipoPersona == 'PersonaNormal':
        new_cli = Clientes(NombreC, Email, password, usuario, telefono, direccion)
        db.session.add(new_cli)
        db.session.commit()
    elif tipoPersona == 'Repartidor':
        new_rep = Repartidor(NombreC, Email, password, usuario, telefono)
        db.session.add(new_rep)
        db.session.commit()
        
    return "si"

@routes_Cliente.route("/validar_login", methods=["POST"])
def validar_login():
    tipoPersona = request.json['tipoPersona']
    email = request.json["email"]
    password = request.json["password"]
   

    if tipoPersona == 'PersonaNormal':
        cliente = Clientes.query.filter_by(Email=email).first()
        if cliente and cliente.password == password:
            return  jsonify({"message":"Correcto cliente"})
    elif tipoPersona == 'Repartidor':
        repartidor = Repartidor.query.filter_by(Email=email).first()
        if repartidor and repartidor.password == password:
            return jsonify({"message":"Correcto repartidor"})
    
@routes_Cliente.route('/mostrar_pedido', methods=['GET'])
def mostrar_pedido():
    datos= {}
    resultado = db.session.query(RegistroPedido,Clientes,Productos,Proveedores).select_from(RegistroPedido,Clientes,Productos,Proveedores).all()
    i=0
    goria = []
    for cate,clie,pro,prov in resultado:
        i+=1	       
        datos[i] = { 
        'Id':cate.id,
		'N_de_pedido':cate.Num_Pedido,
		'Nombre_del_Cliente':clie.NombreC,
		'Productos':pro.NombreP,
		'Cantidad':cate.Cantidad,                                                    
		'Local':prov.NombrePrvdor,                                                    
        }
        goria.append(datos)
    return jsonify(datos)