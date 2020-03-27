from flask import Blueprint, render_template, request, jsonify
from app.models import Authors
from app.helpers import json_response, authenticator
from app import db, application
authors_blueprint = Blueprint('authors', __name__)

#e6c5a49e700911eabdedacde48001122


@authors_blueprint.route('/authors/<public_id>', methods=['GET', 'POST']) 
@authenticator 
def get_authors(current_user, public_id):  
     authors = Authors.query.all()   

     output = []  

     for author in authors:   
       author_data = {}  
       author_data['name'] = author.name 
       author_data['book'] = author.book 
       author_data['country'] = author.country  
       author_data['booker_prize'] = author.booker_prize
       output.append(author_data)  

     return jsonify({'list_of_authors' : output})

@authors_blueprint.route('/authors', methods=['POST', 'GET'])
@authenticator
def create_author(current_user):#current_user):   
   data = request.get_json() 
   new_authors = Authors(name=data['name'], country=data['country'], book=data['book'], booker_prize=True, user_id=current_user.id)  
   db.session.add(new_authors)   
   db.session.commit()   
   return jsonify({'message' : 'new author created'})
       
@authors_blueprint.route('/authors/<name>', methods=['DELETE'])
@authenticator
def delete_author(current_user, name):  
    author = Authors.query.filter_by(name=name, user_id=current_user.id).first()   
    if not author:   
       return jsonify({'message': 'author does not exist'})   


    db.session.delete(author)  
    db.session.commit()   
    return jsonify({'message': 'Author deleted'})