from app import db

class Products(db.Model):
    __tablename__ = 'product'
    idProduct = db.Column(db.Integer, primary_key=True)
    nameProduct = db.Column(db.String(225), nullable=False)
    priceProduct = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.String(255), nullable=False)
    weightProduct = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    id_category = db.Column(db.Integer, db.ForeignKey('category.idCategory'), nullable=False)

    category = db.relationship('Categorys', back_populates='products')
