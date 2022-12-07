######### Imports Flask & Python ###########
from flask import Flask

############## Imports Apps Blueprints ##########
from home.views import home_blueprint
from auth.views import auth_blueprint
from error_pages.handlers import error_pages

#from db.db_connection import get_connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['ENV'] = 'development'

#@app.route('/usuarios')
# def usuarios():
#     connection = get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute('SELECT * FROM users')
#         usuarios = cursor.fetchall()
#         return str(usuarios)

################# Registro de Apps ##################
app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(error_pages)

if __name__ == '__main__':
    app.run(debug=True)