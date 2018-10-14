from flask import current_app

from app.models import db
from app.models.user import User


class UserController:

    def create_user(self, name):
        current_app.logger.info("Trying to create a new user with name: {}.".format(name))
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_user_by_name(self, name):
        current_app.logger.info("Trying to get user with name: {}.".format(name))
        user = User.query.filter(User.name == name).first()
        if user:
            return user
        return False

    def get_user_by_id(self, _id):
        current_app.logger.info("Trying to get user with id: {}.".format(_id))
        user = User.query.filter(User.id == _id).first()
        if user:
            return user
        return False
