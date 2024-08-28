from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app.models.product import Products
from app import db

bp = Blueprint('product', __name__)

@bp.route('/producto')
@login_required
def index():
    data = Products.query.all()
    return render_template('productos/index.html', data=data)

