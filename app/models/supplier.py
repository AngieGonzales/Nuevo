from app import db

class Suppliers(db.Model):
    __tablename__ = 'supplier'
    idSupplier = db.Column(db.Integer, primary_key=True)
    nameSupplier = db.Column(db.String(25), nullable=False)
    phoneSupplier = db.Column(db.String(25), nullable=False)
    emailSupplier = db.Column(db.String(45), nullable=False)
