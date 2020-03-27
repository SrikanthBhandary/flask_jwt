from flask import Flask
from flask_sqlalchemy import SQLAlchemy
APP_SETTINGS = "app.config.DevelopmentConfig" #Move this to environment

application = Flask(__name__)
application.config.from_object(APP_SETTINGS)
db = SQLAlchemy(application)

from app.models import Users, Authors
from app.views.registration import registration_blueprint
from app.views.users import users_blueprint
from app.views.authors import authors_blueprint

application.register_blueprint(registration_blueprint)
application.register_blueprint(users_blueprint)
application.register_blueprint(authors_blueprint)


