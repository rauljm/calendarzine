from flask_restful import Resource
from flask import request
from app.controller.room import RoomController
from app.exceptions.exceptions import RoomNotFoundError


class RoomView(Resource):

    def post(self):
        name = request.json.get("name")
        description = request.json.get("description")
        RoomController().create_room(name, description)
        return "", 200


class RoomGetByIdView(Resource):

    def get(self, _id):
        try:
            room = RoomController().get_room_by_id(_id)
        except RoomNotFoundError:
            return "", 204
        return {"name": room.name, "id": room.id, "description": room.description}, 200


class RoomGetByNameView(Resource):

    def get(self, name):
        try:
            room = RoomController().get_room_by_name(name)
        except RoomNotFoundError:
            return "", 204
        return {"name": room.name, "id": room.id, "description": room.description}, 200

    def delete(self, _id):
        try:
            RoomController().delete_room_by_id(_id)
        except RoomNotFoundError:
            return "", 204
        return "", 200

    def put(self, _id):
        description = request.json.get("description")
        try:
            RoomController().alter_description_by_id(_id, description)
        except RoomNotFoundError:
            return "", 204
        return "", 200
