from flask_restful import Resource
from flask import request
from app.controller.schedule import ScheduleController
from app.exceptions.exceptions import RoomNotFoundError, ScheduleNotFoundError, UserNotFoundError


class ScheduleView(Resource):

    def post(self):
        date = request.json.get("date")
        user_name = request.json.get("user_name")
        room_name = request.json.get("room_name")
        description = request.json.get("description")

        try:
            ScheduleController().create_schedule(date, user_name, room_name, description)
        except RoomNotFoundError:
            return {"error": "Nome de sala nao encontrada."}, 204
        except UserNotFoundError:
            return "Usuario nao encontrado.", 204
        except ValueError:
            return "Formato de data invalida (YYYY-mm-dd)", 400
        return "", 200


class ScheduleGetByIdView(Resource):

    def get(self, _id):
        try:
            schedule = ScheduleController().get_schedule_by_id(_id)
        except ScheduleNotFoundError:
            return "", 204
        return {"id": schedule.id, "date": schedule.date.strftime("%Y-%m-%d"),
                "room_name": schedule.room.name, "user_name": schedule.user.name,
                "description": schedule.description}, 200

    def delete(self, _id):
        try:
            ScheduleController().remove_schedule_by_id(_id)
        except ScheduleNotFoundError:
            return "", 204
        return "", 200

    def put(self, _id):
        description = request.json.get("description")
        try:
            ScheduleController().alter_description_by_id(_id, description)
        except RoomNotFoundError:
            return "", 204
        return "", 200


class ScheduleGetByDateView(Resource):

    def get(self, date):
        try:
            schedules = ScheduleController().get_schedule_by_date(date)
        except ValueError:
            return "Formato de data invalida (YYYY-mm-dd)", 400

        payload = {"schedules": []}
        for schedule in schedules:
            payload["schedules"].append(
                {"id": schedule.id, "date": schedule.date.strftime("%Y-%m-%d"),
                 "room_name": schedule.room.name, "user_name": schedule.user.name,
                                    "description": schedule.description}
            )
        return payload, 200


class ScheduleGetByRoomView(Resource):

    def get(self, room_name):
        try:
            schedules = ScheduleController().get_schedule_by_room_name(room_name)
        except RoomNotFoundError:
            return "", 204

        payload = {"schedules": []}
        for schedule in schedules:
            payload["schedules"].append(
                {"id": schedule.id, "date": schedule.date.strftime("%Y-%m-%d"),
                 "room_name": schedule.room.name, "user_name": schedule.user.name,
                                    "description": schedule.description}
            )
        return payload, 200
