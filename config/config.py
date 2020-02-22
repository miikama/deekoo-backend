import os
_project_root_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_db_name = 'production.db'
_db_path = os.path.join(_project_root_directory, _db_name)

DEBUG = False
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f'sqlite:////{_db_path}'

SECRECT_TOKEN_KEY = os.getenv('SECRET_TOKEN_KEY', 'suchsecrecymuchnumbers')
SECRECT_TOKEN_EXPIRE_TIME = 500

if not DEBUG:
    assert SECRECT_TOKEN_KEY != 'suchsecrecymuchnumbers', "Set the environment variable SECRET_TOKEN_KEY"