from datetime import datetime

from app.models import db
from app.models.schedule import Schedule
from app.controller.room import RoomController
from app.controller.user import UserController
from app.exceptions.exceptions import UserNotFoundError, RoomNotFoundError


class ScheduleController:

    def __init__(self):
        self.room_controller = RoomController()
        self.user_controller = UserController()

    def create_schedule(self, date, user_name, room_name):
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError as error:
            raise error

        user = self.user_controller.get_user_by_name(user_name)
        if not user:
            raise UserNotFoundError()
        room = self.room_controller.get_room_by_name(room_name)
        if not room:
            raise RoomNotFoundError()

        schedule = Schedule(date=date, user=user, room=room)
        db.session.add(schedule)
        db.session.commit()

    def get_schedule_by_id(self, _id):
        schedule = Schedule.query.filter(Schedule.id == _id).first()
        if schedule:
            return schedule
        return False

    def remove_schedule_by_id(self, _id):
        schedule = Schedule.query.filter(Schedule.id == _id).first()
        if schedule:
            db.session.delete(schedule)
            db.session.commit()

    def get_schedule_by_date(self, date):
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError as error:
            raise error

        return Schedule.query.filter(Schedule.date == date.date()).all()
