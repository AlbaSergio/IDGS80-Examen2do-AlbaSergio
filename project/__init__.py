
import os
from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#Creamos una instancia de SQLAlchemy
db = SQLAlchemy()

from .models import User, Role

userDataStore = SQLAlchemyUserDatastore(db, User, Role)


def create_app():

    app = Flask(__name__)
    
 
    


    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    app.config['SECRET_KEY'] = os.urandom(24)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/xtremshop'
 
    app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'

    app.config['SECURITY_PASSWORD_SALT'] = 'thisissecretsalt'

  
    app.config['UPLOAD_FOLDER'] = '/static/img'
    
    #Inicializamos y creamos la BD
    db.init_app(app)
  

    @app.before_first_request
    def create_all():
        db.create_all()
        
    
    #Conectando los modelos a fask-security usando SQLAlchemyUserDatastore
    security = Security(app, userDataStore)

   
   

   
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
