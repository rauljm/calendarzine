from app.tests import BaseTests
from app.models.user import User
from app.models import db


class UserTestCase(BaseTests):

    def test_common(self):
        new_user = User(name="Luiza")
        db.session.add(new_user)
        db.session.commit()

        new_user = User.query.one()
        self.assertEqual(new_user.name, "Luiza")

    def test_add_many_users(self):
        first_user = User(name="Luiza")
        db.session.add(first_user)
        db.session.commit()

        second_user = User(name="Luiza")
        db.session.add(second_user)
        db.session.commit()

        third_user = User(name="Luiza")
        db.session.add(third_user)
        db.session.commit()

        self.assertEqual(User.query.count(), 3)
