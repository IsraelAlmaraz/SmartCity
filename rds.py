from .models import User, GBT, Solicitudes
from flask import Blueprint, request, flash, redirect, url_for, g, render_template, jsonify
from .auth import login_required  # Se trae el decorador de sesión iniciada
from blogr import db             # Nos trameos la base de datos
from sqlalchemy import or_
from datetime import datetime
import json

bp = Blueprint('rds', __name__, url_prefix='/rds')

# Importamos los modelos


@bp.route('/guardar-datos', methods=['POST', 'GET'])
def guardar_datosVIEW():
    if request.method == 'POST':
        data = request.get_json()

        print(data['lat'])
        print(data['lng'])
        # def __init__(self, author, lat, lng,area,fecha):
        # post = Post(, url, title, info, content)
        # Constructor de User def __init__(self, username, email, password, photo = None)
        Solic = Solicitudes(
            g.user.id, data['lat'], data['lng'], data['area'], data['fecha'], "Aceptado", data['alias'])
        # --- Validación de datos ---
        db.session.add(Solic)
        db.session.commit()

        return {'id': "hola"}

    else:
        return "Hola"


@bp.route('/solicitudes-del-dia', methods=['POST', 'GET'])
def get_solicitudes():

    fecha_actual = datetime.now().date()
    # fecha_actual = "A"
    # obtener solicitudes, filtrar por fecha = hoy, status = aceptado o en proceso

    status1 = 'Aceptado'
    status2 = 'En proceso'

    entradas = Solicitudes.query.filter(
        Solicitudes.fecha == fecha_actual, Solicitudes.area == 1,
        or_(Solicitudes.status == status1, Solicitudes.status == status2)
    ).all()

    result = [{'author': entrada.author, 'lat': entrada.lat, 'lng': entrada.lng, 'area': entrada.area,
               'fecha': str(entrada.fecha), 'alias': entrada.alias, 'status': entrada.status} for entrada in entradas]
    return jsonify(result)

    # author, lat, lng, area, fecha, nombre_del_lugar, status


@bp.route('/actualizar-status', methods=['POST', 'GET'])
def actualizar_status():

    if request.method == 'POST':
        data = request.get_json()
        # data = json.loads(data)
        solicitud = Solicitudes.query.filter(
            Solicitudes.fecha == data['fecha'], Solicitudes.area == data['area'],
            Solicitudes.lat == data['lat'], Solicitudes.lng == data['lng'], Solicitudes.alias == data['alias']
        ).first()

        solicitud.status = data['status']
        db.session.commit()

        return jsonify({'mensaje': 'Estado modificado exitosamente'})

    else:
        return "Hola"


@bp.route('/get_gbt_user')
def get_user():
    return str(g.gbt_user.username)
