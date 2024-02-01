from flask import Blueprint, request, flash, redirect, url_for, g, render_template
from .auth import login_required_gbt  # Se trae el decorador de sesión iniciada
from blogr import db             # Nos traemos la base de datos

bp_authGBT = Blueprint('gbt', __name__, url_prefix='/gbt')


@bp_authGBT.route('/gbtindex')
@login_required_gbt
def gbtindexVIEW():
    return render_template('admin/GBT.html')
