from flask import Blueprint, render_template, request
from .models import User,GBT,Solicitudes # Model Class of tables
#from .authGBT import login_requiredgbt  # Importa el decorador de inicio de sesión

bp= Blueprint('home', __name__)


# Funcion para obtener el usuario
#def getUser(id):
    #user = User.query.get_or_404(id)
  #  return user


@bp.route('/', methods=['GET','POST'])
def index():    
    return render_template('index.html')


@bp.route('/blog/<url>')
def blogVIEW(url):
    return render_template('blog.html')

@bp.route('/index2', methods=['GET','POST'])
def index2():    
    return render_template('index2.html')
@bp.route('/ruta33')
def ruta33():
    return render_template('ruta33.html')
