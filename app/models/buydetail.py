from app import db

class BuyDetails(db.Model):
    __tablename__ = 'buy_detail'
    idBuyDetail = db.Column(db.Integer, primary_key=True)
    quantityBuyD = db.Column(db.Integer, nullable=False)
    unitPriceB = db.Column(db.Float, nullable=False)
    subtotalB = db.Column(db.Float, nullable=False)
    id_buy = db.Column(db.Integer, db.ForeignKey('buy.idBuy'))
    id_product = db.Column(db.Integer, db.ForeignKey('product.idProduct'))