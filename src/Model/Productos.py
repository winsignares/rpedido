from config.db import db, app, ma


class Productos(db.Model):
    __tablename__ = "tblproductos"

    id = db.Column(db.Integer, primary_key=True)
    NombreP = db.Column(db.String(200))
    Categoria = db.Column(db.String(200))
    
   

    def __init__(self, NombreP, categoria):
        self.NombreP = NombreP
        self.Categoria = categoria
        
        with app.app_context():
            db.create_all()


class ProductosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'NmobreP','Categoria')