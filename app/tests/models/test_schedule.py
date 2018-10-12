from datetime import datetime

from app.tests import BaseTests
from app.models.schedule import Schedule
from app.models.room import Room
from app.models.user import User
from app.models import db


class ScheduleTestCase(BaseTests):

    def test_common(self):
        new_user = User(name="Luiza")
        db.session.add(new_user)

        new_room = Room(name="Room")
        db.session.add(new_room)

        new_schedule = Schedule(date=datetime(2018, 10, 12), user=new_user, room=new_room)
        db.session.add(new_schedule)

        db.session.commit()

        schedule = Schedule.query.one()
        self.assertEqual(schedule.date, datetime(2018, 10, 12).date())
        self.assertEqual(schedule.user.name, "Luiza")
        self.assertEqual(schedule.room.name, "Room")

    def test_user_and_room_with_many_schedules(self):
        new_user = User(name="Luiza")
        db.session.add(new_user)

        new_room = Room(name="Room")
        db.session.add(new_room)

        first_schedule = Schedule(date=datetime(2018, 10, 12), user=new_user, room=new_room)
        db.session.add(first_schedule)

        second_schedule = Schedule(date=datetime(2018, 10, 13), user=new_user, room=new_room)
        db.session.add(second_schedule)

        db.session.commit()

        user = User.query.one()
        room = Room.query.one()

        self.assertEqual(len(user.schedules), 2)
        self.assertEqual(len(room.schedules), 2)

        self.assertEqual(user.schedules[0].date, datetime(2018, 10, 12).date())
        self.assertEqual(user.schedules[1].date, datetime(2018, 10, 13).date())

        self.assertEqual(room.schedules[0].date, datetime(2018, 10, 12).date())
        self.assertEqual(room.schedules[1].date, datetime(2018, 10, 13).date())
