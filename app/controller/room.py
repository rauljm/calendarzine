from flask import current_app

from app.models import db
from app.models.room import Room
from app.exceptions.exceptions import RoomNotFoundError


class RoomController:

    def create_room(self, name, description):
        current_app.logger.info("Trying to create a new room with name: {}.".format(name))
        room = Room(name=name, description=description)
        db.session.add(room)
        db.session.commit()

    def get_room_by_name(self, name):
        current_app.logger.info("Trying to get room with name: {}.".format(name))
        room = Room.query.filter(Room.name == name).first()
        if room:
            return room
        raise RoomNotFoundError()

    def get_room_by_id(self, _id):
        current_app.logger.info("Trying to get room with id: {}.".format(_id))
        room = Room.query.filter(Room.id == _id).first()
        if room:
            return room
        raise RoomNotFoundError()

    def delete_room_by_id(self, _id):
        current_app.logger.warning("Trying to remove room with id: {}.".format(_id))
        room = self.get_room_by_id(_id)
        if room:
            db.session.delete(room)
            db.session.commit()
            return
        raise RoomNotFoundError()

    def alter_description_by_id(self, _id, description):
        current_app.logger.info("Trying to alter a room with name: {}.".format(_id))
        room = Room.query.filter(Room.id == _id).first()
        if room:
            room.description = description
            db.session.flush()
            db.session.commit()
            return
        raise RoomNotFoundError()
