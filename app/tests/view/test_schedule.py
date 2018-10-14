from app.tests import BaseTests


class ScheduleTestCase(BaseTests):

    def setUp(self):
        super().setUp()
        self.client.post("/room/", json={"name": "Sala", "description": "New"})
        self.client.post("/user/", json={"name": "Raul Martins"})

    def test_common(self):
        response = self.client.post(
            "/schedule/", json={
                "user_name": "Raul Martins", "description": "New Schedule",
                "room_name": "Sala", "date": "2018-10-13"
            }
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/schedule/1")
        self.assertEqual(response.json.get("room_name"), "Sala")
        self.assertEqual(response.json.get("id"), 1)
        self.assertEqual(response.json.get("date"), "2018-10-13")
        self.assertEqual(response.json.get("user_name"), "Raul Martins")

    def test_post_new_schedule_with_user_invalid(self):
        response = self.client.post(
            "/schedule/", json={
                "user_name": "Invalid User", "description": "New Schedule",
                "room_name": "Sala", "date": "2018-10-13"
            }
        )

        self.assertEqual(response.status_code, 204)

    def test_post_new_schedule_with_room_invalid(self):
        response = self.client.post(
            "/schedule/", json={
                "user_name": "Raul Martins", "description": "New Schedule",
                "room_name": "Invalid Room", "date": "2018-10-13"
            }
        )

        self.assertEqual(response.status_code, 204)

    def test_remove_by_id(self):
        response = self.client.delete("schedule/1")
        self.assertEqual(response.status_code, 204)

        self.client.post(
            "/schedule/", json={
                "user_name": "Raul Martins", "description": "New Schedule",
                "room_name": "Sala", "date": "2018-10-13"
            }
        )
        response = self.client.get("/schedule/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get("room_name"), "Sala")
        self.assertEqual(response.json.get("id"), 1)
        self.assertEqual(response.json.get("date"), "2018-10-13")
        self.assertEqual(response.json.get("user_name"), "Raul Martins")

        response = self.client.delete("/schedule/1")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/schedule/1")
        self.assertEqual(response.status_code, 204)

    def test_alter_description_by_id(self):
        self.client.post(
            "/schedule/", json={
                "user_name": "Raul Martins", "description": "New Schedule",
                "room_name": "Sala", "date": "2018-10-13"
            }
        )
        response = self.client.get("/schedule/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get("room_name"), "Sala")
        self.assertEqual(response.json.get("id"), 1)
        self.assertEqual(response.json.get("date"), "2018-10-13")
        self.assertEqual(response.json.get("user_name"), "Raul Martins")

        response = self.client.put("/schedule/1", json={"description": "Schedule schedule"})
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/schedule/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get("description"), "Schedule schedule")

    def test_get_schedules_by_date(self):
        self.client.post(
            "/schedule/", json={
                "user_name": "Raul Martins", "description": "New Schedule",
                "room_name": "Sala", "date": "2018-10-13"
            }
        )
        self.client.post(
            "/schedule/", json={
                "user_name": "Raul Martins", "description": "New Schedule 2",
                "room_name": "Sala", "date": "2018-10-13"
            }
        )

        response = self.client.get("/schedule/2018-10-13")
        payload = response.json.get("schedules")
        self.assertEqual(len(payload), 2)

        self.assertEqual(payload[0]["id"], 1)
        self.assertEqual(payload[1]["id"], 2)

        self.assertEqual(payload[0]["room_name"], "Sala")
        self.assertEqual(payload[1]["room_name"], "Sala")

        self.assertEqual(payload[0]["date"], "2018-10-13")
        self.assertEqual(payload[1]["date"], "2018-10-13")

    def test_get_schedules_by_room(self):
        self.client.post(
            "/schedule/", json={
                "user_name": "Raul Martins", "description": "New Schedule",
                "room_name": "Sala", "date": "2018-10-13"
            }
        )
        self.client.post(
            "/schedule/", json={
                "user_name": "Raul Martins", "description": "New Schedule 2",
                "room_name": "Sala", "date": "2018-10-13"
            }
        )

        response = self.client.get("/schedule/room/Sala")
        payload = response.json.get("schedules")
        self.assertEqual(len(payload), 2)

        self.assertEqual(payload[0]["id"], 1)
        self.assertEqual(payload[1]["id"], 2)

        self.assertEqual(payload[0]["room_name"], "Sala")
        self.assertEqual(payload[1]["room_name"], "Sala")

        self.assertEqual(payload[0]["date"], "2018-10-13")
        self.assertEqual(payload[1]["date"], "2018-10-13")
