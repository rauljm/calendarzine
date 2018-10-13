from app.tests import BaseTests
from app.controller.room import RoomController


class RoomTestCase(BaseTests):

    def test_post(self):
        response = self.client.post("/room/", json={"name": "Sala", "description": "New"})
        room = RoomController().get_room_by_id(1)
        self.assertEqual(room.name, "Sala")
        self.assertEqual(room.description, "New")
        self.assertEqual(response.status_code, 200)

    def test_get_by_id(self):
        response = self.client.get("/room/1")
        self.assertEqual(response.status_code, 204)

        self.client.post("/room/", json={"name": "Sala", "description": "New"})
        response = self.client.get("/room/1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get("name"), "Sala")
        self.assertEqual(response.json.get("id"), 1)
        self.assertEqual(response.json.get("description"), "New")

    def test_get_by_name(self):
        response = self.client.get("/room/Sala")
        self.assertEqual(response.status_code, 204)

        self.client.post("/room/", json={"name": "Sala", "description": "New"})
        response = self.client.get("/room/Sala")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get("name"), "Sala")
        self.assertEqual(response.json.get("id"), 1)
        self.assertEqual(response.json.get("description"), "New")

    def test_remove_by_id(self):
        response = self.client.delete("room/1")
        self.assertEqual(response.status_code, 204)

        self.client.post("/room/", json={"name": "Sala", "description": "New"})
        response = self.client.get("/room/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get("name"), "Sala")

        response = self.client.delete("/room/1")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/room/1")
        self.assertEqual(response.status_code, 204)

    def test_alter_description_by_id(self):
        self.client.post("/room/", json={"name": "Sala", "description": "New"})
        response = self.client.get("/room/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get("description"), "New")

        response = self.client.put("/room/1", json={"description": "New Description"})
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/room/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get("description"), "New Description")
