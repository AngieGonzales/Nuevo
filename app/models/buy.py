from app import db

class Buys(db.Model):
    __tablename__ = 'buy'
    idBuy = db.Column(db.Integer, primary_key=True)
    nameProductB = db.Column(db.String(225), nullable=False)
    quantityBuy = db.Column(db.Float, nullable=False)
    totalPriceB = db.Column(db.Float, nullable=False)
    dateBuy = db.Column(db.Date, nullable=False)
    id_supplier = db.Column(db.Integer, db.ForeignKey('supplier.idSupplier'))
    