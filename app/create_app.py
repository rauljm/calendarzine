from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from app.models import db
from app.views.user import UserView, UserGetByIdView, UserGetByNameView


def create_app(testing=False):
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(UserView, "/user/", endpoint='user_api')
    api.add_resource(UserGetByIdView, "/user/<int:_id>")
    api.add_resource(UserGetByNameView, "/user/<string:name>")

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from app.models.user import User
    from app.models.schedule import Schedule
    from app.models.room import Room
    db.init_app(app)
    Migrate(app, db)

    return app
