from app import db

class SaleDetails(db.Model):
    __tablename__ = 'sale_detail'
    idSaleDetail = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    subTotal = db.Column(db.Float, nullable=False)
    id_sale = db.Column(db.Integer, db.ForeignKey('sale.idSale'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.idProduct'))

    sales = db.relationship("Sales", back_populates="sale_detail")
    products = db.relationship("Products", back_populates="sale_detail")