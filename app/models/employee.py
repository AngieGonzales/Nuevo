from app import db

class Employees(db.Model):
    __tablename__ = 'employee'
    idEmployee = db.Column(db.Integer, primary_key=True)
    nameEmployee = db.Column(db.String(25), nullable=False)
    phoneEmployee = db.Column(db.String(25), nullable=False)
    emailEmployee = db.Column(db.String(25), nullable=False)