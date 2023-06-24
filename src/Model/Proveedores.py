from config.db import db, app, ma


class Proveedores(db.Model):
    __tablename__ = "tblproveedores"

    id = db.Column(db.Integer, primary_key=True)
    Codigo = db.Column(db.String(200))
    NombrePrvdor = db.Column(db.String(200))
    
   

    def __init__(self, Codigo, NombrePrvdor):
        self.Codigo = Codigo
        self.NombrePrvdor = NombrePrvdor
        
        with app.app_context():
            db.create_all()


class ProveedoresSchema(ma.Schema):
    class Meta:
        fields = ('id', 'NmobreP','NombrePrvdor')