from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Customers(db.Model, UserMixin):
    __tablename__ = 'customer'
    idCustomer = db.Column(db.Integer, primary_key=True)
    nameCustomer = db.Column(db.String(25), nullable=False)
    addressCustomer = db.Column(db.String(25), nullable=False)
    emailCustomer = db.Column(db.String(25), nullable=False)
    nameUser = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)

    sales = db.relationship("Sales", back_populates="customer")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return str(self.idCustomer)
