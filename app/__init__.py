from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .auth import auth

def create_app():
    ## iniciar el servidor con el nombre del archivo
    app = Flask(__name__)
    ## configuracion flask
    app.config.from_object(Config)
    app.app.register_blueprint(auth)
    
    return app
    