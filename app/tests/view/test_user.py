from app.tests import BaseTests
from app.controller.user import UserController


class UserTestCase(BaseTests):

    def test_post(self):
        response = self.client.post("/user/", json={"name": "Raul Martins"})
        user = UserController().get_user_by_id(1)
        self.assertEqual(user.name, "Raul Martins")
        self.assertEqual(response.status_code, 200)

    def test_get_by_id(self):
        response = self.client.get("/user/1")
        self.assertEqual(response.status_code, 204)

        self.client.post("/user/", json={"name": "Raul Martins"})
        response = self.client.get("/user/1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get("name"), "Raul Martins")
        self.assertEqual(response.json.get("id"), 1)

    def test_get_by_name(self):
        response = self.client.get("/user/Raul")
        self.assertEqual(response.status_code, 204)

        self.client.post("/user/", json={"name": "Raul"})
        response = self.client.get("/user/Raul")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get("name"), "Raul")
        self.assertEqual(response.json.get("id"), 1)
