from flask_restful import Resource
from flask import request
from app.controller.user import UserController


class UserView(Resource):

    def post(self):
        name = request.json.get("name")
        UserController().create_user(name)
        return "", 200


class UserGetByIdView(Resource):

    def get(self, _id):
        user = UserController().get_user_by_id(_id)
        if user:
            return {"name": user.name, "id": user.id}, 200
        return "", 204


class UserGetByNameView(Resource):

    def get(self, name):
        user = UserController().get_user_by_name(name)
        if user:
            return {"name": user.name, "id": user.id}, 200
        return "", 204
