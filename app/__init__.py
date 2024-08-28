from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(customer_idCustomer):
        from .models.customer import Customers
        return Customers.query.get(customer_idCustomer)
    
    from app.routes import principal_routes, product_routes
    app.register_blueprint(principal_routes.bp)
    app.register_blueprint(product_routes.bp)

    from app.routes.user_routes import auth_bp
    app.register_blueprint(auth_bp)

    return app