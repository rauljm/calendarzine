from app.tests import BaseTests
from app.models.room import Room
from app.models import db


class RoomTestCase(BaseTests):

    def test_common(self):
        new_room = Room(name="Room")
        db.session.add(new_room)
        db.session.commit()

        room = Room.query.one()
        self.assertEqual(room.name, "Room")

    def test_add_many_users(self):
        first_room = Room(name="Room1")
        db.session.add(first_room)
        db.session.commit()

        second_room = Room(name="Room2")
        db.session.add(second_room)
        db.session.commit()

        third_room = Room(name="Room3")
        db.session.add(third_room)
        db.session.commit()

        self.assertEqual(Room.query.count(), 3)
