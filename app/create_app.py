from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from app.models import db
from app.views.user import UserView, UserGetByIdView, UserGetByNameView
from app.views.room import RoomView, RoomGetByIdView, RoomGetByNameView
from app.views.schedule import ScheduleView, ScheduleGetByIdView, ScheduleGetByDateView, ScheduleGetByRoomView


def create_app(testing=False):
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(UserView, "/user/")
    api.add_resource(UserGetByIdView, "/user/<int:_id>")
    api.add_resource(UserGetByNameView, "/user/<string:name>")

    api.add_resource(RoomView, "/room/")
    api.add_resource(RoomGetByIdView, "/room/<int:_id>")
    api.add_resource(RoomGetByNameView, "/room/<string:name>")

    api.add_resource(ScheduleView, "/schedule/")
    api.add_resource(ScheduleGetByIdView, "/schedule/<int:_id>")
    api.add_resource(ScheduleGetByDateView, "/schedule/<string:date>")

    api.add_resource(ScheduleGetByRoomView, "/schedule/room/<string:room_name>")

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from app.models.user import User
    from app.models.schedule import Schedule
    from app.models.room import Room
    db.init_app(app)
    Migrate(app, db)

    return app
