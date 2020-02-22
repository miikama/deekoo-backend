



import os

from deekoo_auth import create_app
from database import check_database_available

"""

This file provides app for wsgi servers. 

NOTE:   Importing from this file causes instantiation of app.
        Do not import from this file inside the project 

"""

# run with the defeult config
config_full_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'config.py')

app = create_app(config_full_path)

# to run wsgi server we require database
check_database_available(app)
