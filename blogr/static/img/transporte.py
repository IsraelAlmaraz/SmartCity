from .models import User, GBT, Solicitudes
from flask import Blueprint, request, flash, redirect, url_for, g, render_template
from .auth import login_required  # Se trae el decorador de sesión iniciada
from blogr import db             # Nos trameos la base de datos

bp = Blueprint('mtp', __name__, url_prefix='/mtp')

# lista de posiciones
ld_pos = [{'id': "camion 1", 'lat': 19.028353, 'lon': -98.188938}]


def limpiar_lista():
    """limpia la lista, para que solo contenga las posiciones más recientes"""
    global ld_pos
    ids_list = []
    clean_list = []

    for dicc in ld_pos:
        if not dicc['id'] in ids_list:  # si no tengo guardado tu id
            ids_list.append(dicc['id'])  # guardar tu id
            # guardar el diccionario, primera aparición del id -> pos más reciente
            clean_list.append(dicc)

    ld_pos = clean_list


@bp.route('/ruta33')
def index():
    """Vista llamada index, ligada a la ruta raíz, """
    return render_template('Ruta33.html')


@bp.route('/posiciones', methods=['POST', 'GET'])
def app1():
    "Aquí el esp32 envía las posiciones, JS pide la lista limpia"
    global ld_pos

    if request.method == 'POST':
        if len(ld_pos) < 25:
            data = request.get_json()
            ld_pos.insert(0, data)
            verificacion = f"recibí {data}"
            return (verificacion)
        else:
            limpiar_lista()
    else:
        limpiar_lista()
        return ld_pos
