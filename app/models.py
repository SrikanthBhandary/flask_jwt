
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects.postgresql import UUID

from app import db
import uuid 
def generate_uuid():
    return str(uuid.uuid4())

class Users(db.Model):  
  id = db.Column(db.Integer, primary_key=True)
  public_id = db.Column(db.String(50))
  name = db.Column(db.String(50))
  password = db.Column(db.String(500))
  admin = db.Column(db.Boolean)

class Authors(db.Model):  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), unique=True, nullable=False)   
  book = db.Column(db.String(20), unique=True, nullable=False) 
  country = db.Column(db.String(50), nullable=False)  
  booker_prize = db.Column(db.Boolean) 
  user_id = db.Column(db.Integer)