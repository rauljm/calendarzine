from flask import Flask
# from flask_restful import Api
from flask_migrate import Migrate

from app.models import db


def create_app(testing=False):
    app = Flask(__name__)
    # api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from app.models.user import User
    from app.models.schedule import Schedule
    from app.models.room import Room
    db.init_app(app)
    Migrate(app, db)

    return app
