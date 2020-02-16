
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from deekoo_auth.models import User

from sqlalchemy.exc import OperationalError

import logging
logger = logging.getLogger(__name__)

def initialize_database(app: Flask, db: SQLAlchemy):
    """
        Check if the database already exists, and if not, init it
    """

    with app.app_context():
        db.create_all()
        logger.warn("Created database tables")

            
    
