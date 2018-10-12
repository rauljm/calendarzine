from app.controller.user import UserController
from app.tests import BaseTests


class UserControllerTestCase(BaseTests):

    def test_common(self):
        user_controller = UserController()
        user_controller.create_user("New User Controller")

        user_by_name = user_controller.get_user_by_name("New User Controller")
        self.assertEqual(user_by_name.name, "New User Controller")

        user_by_id = user_controller.get_user_by_id(1)
        self.assertEqual(user_by_id.id, 1)
