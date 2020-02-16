
from passlib.apps import custom_app_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                            BadSignature, SignatureExpired)

import flask
from deekoo_auth import db, auth

def token_key():
    return flask.current_app.config.get('SECRECT_TOKEN_KEY')

def token_expiration_time():
    return flask.current_app.config.get('SECRECT_TOKEN_EXPIRE_TIME')



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(320), index=True)
    api_auth_token = db.Column(db.String(255), index=True)    
    map_auth_token = db.Column(db.String(255), index=True)

    def set_password(self, password: str):
        """
            Given an already validated password, encrypt and store the hash
        """
        self.password_hash = custom_app_context.encrypt(password)

    def verify_password(self, password: str):
        """
            Check if the argument password is this users password
        """
        return custom_app_context.verify(password, self.password_hash)

    def generate_token(self):
        """
            generate an access token for the user
        """
        print(f"token key has type {type(token_key())}")
        s = Serializer(token_key(), expires_in=token_expiration_time())
        
        return s.dumps({
                            'id': self.id
                        })

    def __repr__(self):
        return f"User with name: {self.username} and email: {self.email}."

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(token_key())
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None

        user = User.query.get(data.get('id'))
        return user

    @staticmethod
    def get_user(username: str, password: str):
        user = User.query.filter_by(username=username)
        if not user:
            return None

        if user.verify_password(password):
            return user

        return None

    @staticmethod
    def add_user(username, password, email=''):
        user = User(username=username)
        user.set_password(password)
        if email:
            user.email = email

        return user


@auth.verify_password
def verify_password(username_or_token: str, password: str):
    """
        A method for HTTPBasicAuth for handling the authentication

        Authenticate based on token or id
    """
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    
    flask.g.user = user
    return True
    

        
