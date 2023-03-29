from flask import Flask
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

def Startup(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'Ima1i1SFG8169782'
    app.static_folder = 'static'

    from .views import views
    #from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    #app.register_blueprint(auth, url_prefix='/')


    return app