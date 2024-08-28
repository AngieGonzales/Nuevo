from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.customer import Customers
from app.models.sale import Sales
from app import db

auth_bp = Blueprint('user', __name__)


@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nameUser = request.form['nameUser']
        password  = request.form['password']

        customer = Customers.query.filter_by(nameUser=nameUser,  password = password).first()

        if customer:
            login_user(customer)
            
            flash("Login successful!", "success")
            return redirect(url_for('user.dashboard'))
        
        flash('Invalid credentials. Please try again.', 'danger')
    
    if current_user.is_authenticated:
        return redirect(url_for('user.dashboard'))
    return render_template("/customers/login.html")

@auth_bp.route('/principales')
@login_required
def dashboard():
    return redirect(url_for('user.dashboard'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('user.login'))