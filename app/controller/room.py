from app.models import db
from app.models.room import Room


class RoomController:

    def create_room(self, name):
        room = Room(name=name)
        db.session.add(room)
        db.session.commit()

    def get_room_by_name(self, name):
        room = Room.query.filter(Room.name == name).first()
        if room:
            return room
        return False

    def get_room_by_id(self, _id):
        room = Room.query.filter(Room.id == _id).first()
        if room:
            return room
        return False

    def delete_room_by_id(self, _id):
        room = self.get_room_by_id(_id)
        db.session.delete(room)
        db.session.commit()
