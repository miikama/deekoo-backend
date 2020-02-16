
from passlib.apps import custom_app_context

from deekoo_auth import db



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
        return None

    def __repr__(self):
        return f"User with name: {self.username} and email: {self.email}."

    @staticmethod
    def add_user(username, password, email=''):
        user = User(username=username)
        user.set_password(password)
        if email:
            user.email = email

        return user

        

        
