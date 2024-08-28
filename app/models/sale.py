from app import db

class Sales(db.Model):
    __tablename__ = 'sales'
    idSale = db.Column(db.Integer, primary_key=True)
    dateSale = db.Column(db.DateTime, nullable=False)
    subTotal = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable = False)
    id_customer = db.Column(db.Integer, db.ForeignKey('customer.idCustomer'), nullable=False)

    customer = db.relationship("Customers", back_populates="sales")


    