
import sys
import logging

from flask import Flask
from sqlalchemy.exc import OperationalError

from deekoo_auth.models import User

logger = logging.getLogger(__name__)

database_usage = """
Initialize or upgrade database with 

python deekoo_auth/cli.py db upgrade

or 

deekoo_cli db upgrade
"""

def check_database_available(app: Flask):
    """        
        The database has to be created outside the
        application. This is just a step that will 
        check that the configured database is created
        and warns the user about missing database.
    """
    
    try:
        with app.app_context():            
            users = User.query.first()
    except OperationalError:
        print(f"\nDatabase at {app.config['SQLALCHEMY_DATABASE_URI']} does not exist")
        print(database_usage)
        sys.exit(1)
            
    
