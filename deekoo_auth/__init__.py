
import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_httpauth import HTTPBasicAuth 

db = SQLAlchemy()
auth = HTTPBasicAuth()

from deekoo_auth.database import initialize_database

DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'config.py')

def create_app(config_path: str):
    """
        Given a path to config.py file, init app with database

        Different configuration files are in ../config folder.       
    """

    if not os.path.exists(config_path):
        raise OSError(f"Configuration file {config_path} does not exist")

    # create flask app
    app = Flask(__name__)

    # add app configration    
    app.config.from_pyfile(config_path)

    # initialize database 
    db.init_app(app)
    initialize_database(app, db)

    # initialize api enpoints
    from deekoo_auth.endpoints import api_endpoints
    app.register_blueprint(api_endpoints)

    return app