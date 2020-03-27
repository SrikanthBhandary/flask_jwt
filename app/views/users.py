
from flask import Blueprint, render_template, request, jsonify
from app.models import Users
from app.helpers import json_response, authenticator
from app import db, application
users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/users', methods=['GET'])
@authenticator
def get_all_users(current_user):
    users = Users.query.all() 
    result = []   
    for user in users:   
        user_data = {}   
        user_data['public_id'] = user.public_id  
        user_data['name'] = user.name 
        user_data['password'] = user.password
        user_data['admin'] = user.admin     
        result.append(user_data)   
    return jsonify({'users': result})  

