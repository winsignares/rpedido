from config.db import db, app, ma 

class RegistroPedido(db.Model):
    __tablename__ = "tblregistropedido"

    id = db.Column (db.Integer, primary_key = True)
    id_Cliente = db.Column(db.Integer, db.ForeignKey('tblclientes.id'))
    id_Producto = db.Column(db.Integer, db.ForeignKey('tblproductos.id'))
    id_Local = db.Column(db.Integer, db.ForeignKey('tblproveedores.id'))
    Cantidad = db.Column(db.Integer)
    Num_Pedido = db.Column(db.Integer)
    

    def __init__(self, id_Cliente, id_Producto, id_Local,  Cantidad, Num_Pedido ):
        self.id_Cliente = id_Cliente
        self.id_Producto = id_Producto
        self.id_Local = id_Local
        self.Cantidad = Cantidad
        self.Num_Pedido = Num_Pedido


with app.app_context():
    db.create_all()

class RegistroPedidoSchema(ma.Schema):
    class meta:
        fields = ('id', 'id_Cliente','id_Producto','id_Local', 'Cantidad','Num_Pedido' )