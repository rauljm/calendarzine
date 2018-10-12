from app.models import db
from app.models.user import User


class UserController:

    def create_user(self, name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_user_by_name(self, name):
        user = User.query.filter(User.name == name).first()
        if user:
            return user
        return False

    def get_user_by_id(self, id):
        user = User.query.filter(User.id == id).first()
        if user:
            return user
        return False
