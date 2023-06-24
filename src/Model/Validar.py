from config.db import db, app, ma 

class Validar(db.Model):
    __tablename__ = "tblvalidar"
    
    id = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(200))
    Email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    id_Cliente = db.Column(db.Integer, db.ForeignKey('tblclientes.id'))
    id_Repartidor = db.Column(db.Integer, db.ForeignKey('tblrepartidor.id'))
    

    def __init__(self, id_Cliente, id_Repartidor):
        self.id_Cliente = id_Cliente
        self.id_Repartidor = id_Repartidor


with app.app_context():
    db.create_all()

class ValidarSchema(ma.Schema):
    class meta:
        fields = ('id_Cliente','id_Producto')