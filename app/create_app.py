from flask import Flask
# from flask_restful import Api
from flask_migrate import Migrate

from models import db


def create_app():
    app = Flask(__name__)
    # api = Api(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from models.user import User
    from models.schedule import Schedule
    Migrate(app, db)

    return app
