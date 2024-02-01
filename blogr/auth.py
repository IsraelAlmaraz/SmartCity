from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
#Flash es para los errores.


# Para el generador de contraseñas
from werkzeug.security import generate_password_hash, check_password_hash
    #generate_password_hash Para encripatar la contraseña
    #check_password_hash Para checar la conttraseña


# Blueprint para usuarios normales
bp = Blueprint('auth', __name__, url_prefix='/auth')

# Blueprint para usuarios de GBT
bp_authGBT = Blueprint('authGBT', __name__, url_prefix='/authGBT')


# Importamos los modelos
from .models import User,GBT

# Importamos el objecto de SQLAlchemy()
from blogr import db

import functools

@bp.route('/register', methods = ('GET','POST'))
def registerVIEW():
    # Cuendo el metodo es POST
    if request.method == 'POST':
        # Extracion de valores
        username = request.form.get('username')                         # Opción 2 para obtener el valor
        # username = request.form['username']                           # Opción 2 para obtener el valor
        email = request.form.get('email')                               # Opción 1 para obtener el valor
        # email = request.form['username']                              # Opción 2 para obtener el valor
        password = request.form.get('password')                         # Opción 1 para obtener el valor
        # password = request.form['password']                           # Opción 2 para obtener el valor
        
        # Verificador de datos
        # print('username:',username)
        # print('email:', email)
        # print('password',password)
        
        # Constructor de User def __init__(self, username, email, password, photo = None)
        user = User(username, email, generate_password_hash(password))
        # --- Validación de datos ---
        error = None

        # Comparando nombre de usuario con los existentes
        userEmail = User.query.filter_by(email = email).first()

        # Verificio que no exista
        if userEmail == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.loginVIEW'))
        else:
            error = f'El correo {email} ya esta registrado'
        flash(error)
    # Template principal
    return render_template('auth/register.html')

@bp.route('/login', methods = ('GET','POST'))
def loginVIEW():
    if request.method == 'POST':
        print('Entra')
        email = request.form.get('email') # Forma 1 de obtener datos
        password= request.form.get('password')

        # --- Validando datos ---
        error = None
       
        user = User.query.filter_by(email=email).first()
       
        

            # Filtra por la columna email y buscar el primer valor que conincide con email
        # print(user)
        
        # Validación de contraseña
        if user == None or not check_password_hash(user.password, password):
            error = 'Correo contraseña incorrecta'
   
        # Iniciando sesion
        if error is None:
            session.clear()
            session['user_id']=user.id
            return redirect(url_for('post.postsVIEW')) #Cuando inicia sessión nos va enviar a la sessión de inicio
         
        # Mensaje de error
        flash(error)
    
    # Template principal
    return render_template('auth/login.html')

# Para verificar que esta iniciada una seccción
@bp.before_app_request
def loadLoggedInIser():
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)
# Cerrar sesión
        
# auth.py
@bp.route('/logout')
def logoutVIEW_auth():
    session.clear()
    return redirect(url_for('home.index'))


# Para verificar que este iniciada la sección en la vista

def login_required(view):
    @functools.wraps(view)                      # @functools.wraps la decoradora
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.loginVIEW')) # Sino existe tiene que redireccionar
        return view(**kwargs)                      # Si esta regresa a la vista en que esta
    return wrapped_view                            # Ejecuta la función


# Editar Perfil
#from werkzeug.utils import secure_filename # secure_filenameCuando se tiene espacios los cambia por '_'
# El getPhoto: Nos permiet obtener la dirección de la foto del usuario con el id.
# def getPhoto(id):
#     user = User.query.get_or_404(id)     # Se extraen los valores del usuario con el id dado
#     photo = None
#     if photo != None:                    # Sí existe valor los guarda y sino   
#         photo = user.photo
#     return photo 



# --- Perfil del usuario ---
# Para este caso ya se requiere que este una session activa
# Se requiere que obtener el id
@bp.route('/profile/<int:id>', methods=('GET', 'POST')) # Se agrag , id=g.user.id a las llamadas de la función "profileVIEW(id)"
@login_required #Petición de una sección iniciada
def profileVIEW_auth(id):
    user = User.query.get_or_404(id)      # Se extraen los valores del usuario con el id dado
    if request.method == 'POST':
        user.username = request.form.get('username')         # Forma 1 de estraer valores
        # La diferencia entre el siguiente y el anterior es que uno se va directo a sustituir y el segundo se extra el valor para comparar
        password = request.form.get('password')              # Extracción de valores F1
        error= None
        
        if len(password)!=0:                                     # Si es diferente de 0 se rescribe la contraseña. Al final si hay un mensaje de erro no se guardan los cambios
            user.password = generate_password_hash(password)
        elif len(password)> 0 and len(password) < 6:             # En caso de que se tenga una longitud mayor a 6, entonces se procede a guardarla sino se manda un mensaje de eror.
            error='La contraseña debe tener más de 5 caracteres'

        if request.files['photo']:                               # Si se a utilizado el metodo file que es el botos de explorar.
            photo = request.files['photo']
            #photo.save(f'blogr/static/media/{secure_filename(photo.filename)}')
           # user.photo = f'media/{secure_filename(photo.filename)}'


        if error is not None:                                    # Si la variable erro no esta vacia entonces envía los mesajes con la función flash().
            flash(error)
        else:                                                    # Sí la variable error esta vacia entonces se procede a guardar actualizar los datos (commit) sino no se guardan los cambios.
            db.session.commit()
            return redirect(url_for('auth.profileVIEW_auth', id=user.id)) # Se envia el id porquue es un requisito de la ruta.
        flash(error)                                             # Flash final
    # Se envía photo solo en render_template ya que es en redirect no lo pide, esto es a que la función es diferente al .HTML
    return render_template('auth/profile.html', user=user) 




@bp_authGBT.route('/registerGBT', methods = ('GET','POST'))
def registerGBTVIEW():
    # Cuendo el metodo es POST
    if request.method == 'POST':
        # Extracion de valores
        username = request.form.get('username')                         # Opción 2 para obtener el valor
        # username = request.form['username']                           # Opción 2 para obtener el valor
        email = request.form.get('email')                               # Opción 1 para obtener el valor
        # email = request.form['username']                              # Opción 2 para obtener el valor
        password = request.form.get('password')                         # Opción 1 para obtener el valor
        # password = request.form['password']                           # Opción 2 para obtener el valor
        
        # Verificador de datos
        # print('username:',username)
        # print('email:', email)
        # print('password',password)
        
        # Constructor de User def __init__(self, username, email, password, photo = None)
        gbt_user = GBT(username, email, generate_password_hash(password), area=request.form.get('area'))

        # --- Validación de datos ---
        error = None

        # Comparando nombre de usuario con los existentes
        userEmail = GBT.query.filter_by(email = email).first()

        # Verificio que no exista
        if userEmail == None:
            db.session.add(gbt_user)
            db.session.commit()
            return redirect(url_for('authGBT.loginGBTVIEW'))
        else:
            error = f'El correo {email} ya esta registrado'
        flash(error)
    # Template principal
    return render_template('auth/registerGBT.html')

@bp_authGBT.route('/loginGBT', methods=('GET', 'POST'))
def loginGBTVIEW():
    if request.method == 'POST':
        email = request.form.get('email')  # Forma 1 de obtener datos
        password = request.form.get('password')

        # --- Validando datos ---
        error = None
        gbt_user = GBT.query.filter_by(email=email).first()

        # Validación de contraseña
        if gbt_user is None or not check_password_hash(gbt_user.password, password):
            error = 'Correo o contraseña incorrecta'

        if error is None:
            session.clear()
            session['user_id_GBT'] = gbt_user.id
            next_url = request.args.get('next')  # Obtiene la URL a la que se intentaba acceder
            
            # Cambia la línea de redirección para dirigir al usuario a /gbt/gbtindex
            # Ejemplo de redirección después del login
            return redirect(url_for('gbt.gbtindexVIEW'))

        # Mensaje de error
        flash(error)

    # Template principal
    return render_template('auth/loginGBT.html')


           
    

  # ))#
#
# Para verificar que esta iniciada una seccción
@bp_authGBT.before_app_request # Para que se ejecute en cada iteración automaticamente
def loadLoggedInIser():
    user_id_GBT = session.get('user_id_GBT') # Si alguien incio sección no va a devolver el id del usuario y sino un valor nulo
    
    if user_id_GBT is None: # Si es nulo nadie ha iniciado sección
        g.gbt_user = None# Guardamos el valor en g
    else:
        g.gbt_user = GBT.query.get_or_404(user_id_GBT) # Si ya iniciaron sección, hacemos una seunda consulta que es sacar el valor de id de usuario. Si existe el usuario va regresar el valor del usuario y sino va a regresar un error 404

# Cerrar sesión
@bp_authGBT.route('/logout')
def logoutVIEW():
    session.clear() # Con esto se cierra la sección
    return redirect(url_for('home.index')) # Con esto redireccionamos a la pagina principal

# Para verificar que este iniciada la sección en la vista

def login_required_gbt(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.gbt_user is None:
            return redirect(url_for('auth.loginGBTVIEW'))
        return view(**kwargs)
    return wrapped_view



# Editar Perfil
#from werkzeug.utils import secure_filename # secure_filenameCuando se tiene espacios los cambia por '_'
# El getPhoto: Nos permiet obtener la dirección de la foto del usuario con el id.
# def getPhoto(id):
#     user = User.query.get_or_404(id)     # Se extraen los valores del usuario con el id dado
#     photo = None
#     if photo != None:                    # Sí existe valor los guarda y sino   
#         photo = user.photo
#     return photo 



# --- Perfil del usuario ---
# Para este caso ya se requiere que este una session activa
# Se requiere que obtener el id
@bp_authGBT.route('/profileGBT/<int:id>', methods=('GET', 'POST')) # Se agrag , id=g.user.id a las llamadas de la función "profileVIEW(id)"
@login_required_gbt #Petición de una sección iniciada
def profileGBTVIEW(id):
    gbt_user = GBT.query.get_or_404(id)      # Se extraen los valores del usuario con el id dado
    if request.method == 'POST':
        gbt_user.username = request.form.get('username')         # Forma 1 de estraer valores
        # La diferencia entre el siguiente y el anterior es que uno se va directo a sustituir y el segundo se extra el valor para comparar
        password = request.form.get('password')              # Extracción de valores F1
        error= None
        
        if len(password)!=0:                                     # Si es diferente de 0 se rescribe la contraseña. Al final si hay un mensaje de erro no se guardan los cambios
            gbt_user.password = generate_password_hash(password)
        elif len(password)> 0 and len(password) < 6:             # En caso de que se tenga una longitud mayor a 6, entonces se procede a guardarla sino se manda un mensaje de eror.
            error='La contraseña debe tener más de 5 caracteres'

        if request.files['photo']:                               # Si se a utilizado el metodo file que es el botos de explorar.
            photo = request.files['photo']
            #photo.save(f'blogr/static/media/{secure_filename(photo.filename)}')
           # user.photo = f'media/{secure_filename(photo.filename)}'


        if error is not None:                                    # Si la variable erro no esta vacia entonces envía los mesajes con la función flash().
            flash(error)
        else:                                                    # Sí la variable error esta vacia entonces se procede a guardar actualizar los datos (commit) sino no se guardan los cambios.
            db.session.commit()
            return redirect(url_for('authGBT.profileGBT_VIEW', id=gbt_user.id))
       # Se envia el id porquue es un requisito de la ruta.
        flash(error)                                             # Flash final
    # Se envía photo solo en render_template ya que es en redirect no lo pide, esto es a que la función es diferente al .HTML
    return render_template('auth/profileGBT.html', user=gbt_user) 
