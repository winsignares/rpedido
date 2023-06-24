from config.db import db, app, ma


class Clientes(db.Model):
    __tablename__ = "tblclientes"

    id = db.Column(db.Integer, primary_key=True)
    NombreC = db.Column(db.String(200))
    Email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    usuario = db.Column(db.String(200))
    telefono = db.Column(db.String(10))
    direccion = db.Column(db.String(200))
   

    def __init__(self, NombreC, Email, password, usuario, telefono, direccion):
        self.NombreC = NombreC
        self.Email = Email
        self.password = password
        self.usuario = usuario
        self.telefono = telefono
        self.direccion = direccion

        with app.app_context():
            db.create_all()


class ClientesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'NombreC', 'Email', 'password', 'usuario', 'telefono', 'direccion')