from flask import jsonify, make_response
from functools import wraps
from flask import request
import jwt
from app import application
from app.models import Users

def json_response(message, code, result_dict={}):
    return make_response(message, code, result_dict) 

def authenticator(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        print("*" * 100)
        print(request.headers)
        if 'x-access-tokens' in request.headers:  
          token = request.headers['x-access-tokens']         
        if not token:  
          return jsonify({'message': 'a valid token is missing'})   
        try:  
          data = jwt.decode(token, application.config['SECRET_KEY']) 
          current_user = Users.query.filter_by(public_id=data['public_id']).first()  
        except Exception as e:
            print(e)
            return jsonify({'message': 'token is invalid'})  
        return f(current_user, *args,  **kwargs)  
    return decorator