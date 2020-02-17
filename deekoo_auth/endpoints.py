
from flask import Blueprint, jsonify, request, g

from deekoo_auth.models import User
from deekoo_auth import db, auth


api_endpoints = Blueprint('api', __name__)


CREATED = 201
UNAUTHORIZED = 401
UNPROCESSABLE_ENTITY = 422


class MapEntry:

    def __init__(self, longitude, latitude, user):
        self.longitude = longitude
        self.latitude = latitude
        self.user = user

    def to_json(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'user': self.user
        }

class MapService:

    def entries_for_user(self, user):
        return {
            'entries': [
                MapEntry(60, 25, "Anon").to_json()
            ]
        }



@api_endpoints.route('/authenticate', methods=['POST'])
@auth.login_required
def authenticate():
    """
        This route is used to obtain a new access token.

        This can be accessed with a valid access token
        or with login credentials.
        
    """ 
    token = g.user.generate_token()

    return jsonify({
        "token": token.decode('ascii')
    })


@api_endpoints.route('/users', methods=['POST'])
def new_user():
    if request.json is None:
        return jsonify(), UNPROCESSABLE_ENTITY
        
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email', '')

    if not username or not password:
        return jsonify(), UNPROCESSABLE_ENTITY  

    user = User.add_user(username, password, email)

    if not user:
        return jsonify(), UNPROCESSABLE_ENTITY  

    token = user.generate_token()

    db.session.add(user)
    db.session.commit()

    return jsonify({"token": token.decode('ascii')}), CREATED


@api_endpoints.route('/users', methods=['GET'])
def get_users():    
    users = User.query.all()
    db.session.commit()

    user_list = [str(user) for user in users]
    
    return jsonify({'users': user_list})



@api_endpoints.route('/map', methods=['GET'])
@auth.login_required
def map():
    entries = MapService().entries_for_user(g.user)
    return jsonify(entries) 

