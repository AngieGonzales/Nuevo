from flask import Blueprint, render_template, redirect, url_for, request, flash, json
from flask_login import login_required
from app.models.category import Categorys
from app.models.buy import Buys
from app.models.customer import Customers
from app.models.employee import Employees
from app.models.supplier import Suppliers
from app.models.product import Products
from app.models.buydetail import BuyDetails

bp = Blueprint('principal', __name__)

@bp.route('/principales')
def index():
    return render_template('principales/principal.html')
    

@bp.route('/Frutas-Verduras')
def frutas_verduras():
    return render_template('categorys/indexFrutas.html')

@bp.route('/Lacteos-Huevos')
def lacteos_huevos():
    return render_template('categorys/indexLacteos.html')

@bp.route('/Carnes')
def carnes():
    return render_template('categorys/indexCarnes.html')

@bp.route('/Arroz-Granos-Pastas')
def arroz_granos_pastas():
    return render_template('categorys/indexArroz.html')

@bp.route('/Aceites-Sal-Endulzantes')
def aceites_sal_endulzantes():
    return render_template('categorys/indexAceites.html')

@bp.route('/Despensa')
def despensa():
    return render_template('categorys/indexDespensa.html')

@bp.route('/Bebidas')
def bebidas():
    return render_template('categorys/indexBebidas.html')

@bp.route('/AseoPersonal')
def aseo_personal():
    return render_template('categorys/indexAseoPersonal.html')

@bp.route('/AseoHogar')
def aseo_hogar():
    return render_template('categorys/indexAseoHogar.html')

@bp.route('/Mascotas')
def mascotas():
    return render_template('categorys/indexMascotas.html')

@bp.route('/Licores')
def licores():
    return render_template('categorys/indexLicores.html')

@bp.route('/Salsas-Sazonadores')
def salsas_sazonadores():
    return render_template('categorys/indexSalsas.html')

@bp.route('/CarritoCompras')
def ruta_carrito():
    return render_template('carrito/index.html')

@bp.route('/Volver-inicio')
def PaginaInicio():
    return render_template('principales/principal.html')




