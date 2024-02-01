from flask import Blueprint, request, flash, redirect, url_for, g, render_template
from .auth import login_required # Se trae el decorador de sesión iniciada
from blogr import db             # Nos trameos la base de datos


bp= Blueprint('post', __name__, url_prefix = '/post')

@bp.route('/posts')
@login_required                 # Aplico la peditición de inicio de sección con el decorador que hice
def postsVIEW():
    return render_template('admin/posts.html') # Envío los datos al documento HTML




