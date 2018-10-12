from app.controller.room import RoomController
from app.tests import BaseTests


class UserControllerTestCase(BaseTests):

    def test_common(self):
        room_controller = RoomController()
        room_controller.create_room("New Room Controller")

        room_by_name = room_controller.get_room_by_name("New Room Controller")
        self.assertEqual(room_by_name.name, "New Room Controller")

        room_by_id = room_controller.get_room_by_id(1)
        self.assertEqual(room_by_id.id, 1)

    def test_remove_room(self):
        room_controller = RoomController()
        room_controller.create_room("New Room Controller")

        room_by_name = room_controller.get_room_by_name("New Room Controller")
        self.assertTrue(room_by_name)

        room_controller.delete_room_by_id(room_by_name.id)
        room_by_name = room_controller.get_room_by_name("New Room Controller")

        self.assertFalse(room_by_name)
