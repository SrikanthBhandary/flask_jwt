import uuid
import datetime
import jwt
from flask import Blueprint, render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Users, Authors
from app.helpers import json_response, authenticator
from app import db, application
registration_blueprint = Blueprint('registrations', __name__)

@registration_blueprint.route('/register', methods=['post'])
def signup_user():
    data = request.get_json()
    password = data['password']
    name = data['name']
    hashed_password = generate_password_hash(password, method='sha256')
    user = Users(public_id=str(uuid.uuid1().hex), name=name, password=hashed_password, admin=False)
    db.session.add(user)  
    db.session.commit()    
    return json_response('User Registered Successfully', 201)

@registration_blueprint.route('/login', methods=['post'])
def login():
    auth = request.authorization    
    if not auth or not auth.username or not auth.password:
        return json_response('Authorization is missing.', 404)
    user = Users.query.filter_by(name=auth.username).first()
    if check_password_hash(user.password, auth.password):  
        token = jwt.encode({'public_id': user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 
        application.config['SECRET_KEY'])  
        return json_response({'token' : token.decode('UTF-8')}, 200)        
    return json_response("Invalid Credentials.", 200)        

    

    

