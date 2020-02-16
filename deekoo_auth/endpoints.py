
from flask import Blueprint, jsonify, request

from deekoo_auth.models import User
from deekoo_auth import db


api_endpoints = Blueprint('api', __name__)


CREATED = 201
UNPROCESSABLE_ENTITY = 422


@api_endpoints.route('/authenticate', methods=['POST'])
def authenticate():
    print("authenticating")

    return jsonify({
        "token": ''
    })


@api_endpoints.route('/users', methods=['POST'])
def new_user():
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

    return jsonify({"token": token}), CREATED


@api_endpoints.route('/users', methods=['GET'])
def get_users():    
    users = User.query.all()
    db.session.commit()

    for user in users:
        print(user)

    return jsonify({})



@api_endpoints.route('/map', methods=['GET'])
def map():
    print("accessing map")
    return jsonify({
            'data': 'map data'
        }) 

