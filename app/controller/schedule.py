from datetime import datetime

from flask import current_app

from app.models import db
from app.models.schedule import Schedule
from app.controller.room import RoomController
from app.controller.user import UserController
from app.exceptions.exceptions import UserNotFoundError, RoomNotFoundError, ScheduleNotFoundError


class ScheduleController:

    def __init__(self):
        self.room_controller = RoomController()
        self.user_controller = UserController()

    def create_schedule(self, date, user_name, room_name, description):
        current_app.logger.info("Trying to create a new schedule to date: {}.".format(str(date)))
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError as error:
            current_app.logger.warning(
                "Problem with date parser when create a new schedule. The date is: {} ".format(str(date))
            )
            raise error

        user = self.user_controller.get_user_by_name(user_name)
        if not user:
            current_app.logger.warning("User {} not found when trying to create a new schedule.".format(user_name))
            raise UserNotFoundError()
        room = self.room_controller.get_room_by_name(room_name)
        if not room:
            current_app.logger.warning("Room {} not found when trying to create a new schedule.".format(room_name))
            raise RoomNotFoundError()

        schedule = Schedule(date=date, user=user, room=room, description=description)
        db.session.add(schedule)
        db.session.commit()
        current_app.logger.info("Schedule create.")

    def get_schedule_by_id(self, _id):
        schedule = Schedule.query.filter(Schedule.id == _id).first()
        if schedule:
            return schedule
        raise ScheduleNotFoundError()

    def remove_schedule_by_id(self, _id):
        current_app.logger.info("Removing schedule with id: {}.".format(_id))
        schedule = Schedule.query.filter(Schedule.id == _id).first()
        if schedule:
            db.session.delete(schedule)
            db.session.commit()
            return
        raise ScheduleNotFoundError()

    def get_schedule_by_date(self, date):
        current_app.logger.info("Geting all schedules with date: {}.".format(str(date)))
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError as error:
            raise error

        return Schedule.query.filter(Schedule.date == date.date()).all()

    def get_schedule_by_room_name(self, room_name):
        current_app.logger.info("Geting all schedules for room: {}.".format(room_name))
        room = self.room_controller.get_room_by_name(room_name)
        return room.schedules

    def alter_description_by_id(self, _id, description):
        current_app.logger.info("Trying to alter description of schedule with id: {}.".format(_id))
        schedule = Schedule.query.filter(Schedule.id == _id).first()
        if schedule:
            schedule.description = description
            db.session.commit()
            return
        raise ScheduleNotFoundError()
