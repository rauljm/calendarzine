from app.controller.room import RoomController
from app.tests import BaseTests
from app.exceptions.exceptions import RoomNotFoundError


class UserControllerTestCase(BaseTests):

    def test_common(self):
        room_controller = RoomController()
        room_controller.create_room("New Room Controller", "Description")

        room_by_name = room_controller.get_room_by_name("New Room Controller")
        self.assertEqual(room_by_name.name, "New Room Controller")

        room_by_id = room_controller.get_room_by_id(1)
        self.assertEqual(room_by_id.id, 1)

    def test_remove_room(self):
        room_controller = RoomController()
        room_controller.create_room("New Room Controller", "Description")

        room_by_name = room_controller.get_room_by_name("New Room Controller")
        self.assertTrue(room_by_name)

        room_controller.delete_room_by_id(room_by_name.id)
        with self.assertRaises(RoomNotFoundError):
            room_controller.get_room_by_id(1)

    def test_alter_room(self):
        room_controller = RoomController()
        room_controller.create_room("New Room Controller", "Description")

        room_by_name = room_controller.get_room_by_name("New Room Controller")
        self.assertEqual(room_by_name.description, "Description")

        room_controller.alter_description_by_id(room_by_name.id, "New Description")
        room_by_name = room_controller.get_room_by_name("New Room Controller")

        self.assertEqual(room_by_name.description, "New Description")

    def test_get_room_by_id_that_not_exist(self):
        room_controller = RoomController()
        with self.assertRaises(RoomNotFoundError):
            room_controller.get_room_by_id(1)

    def test_get_room_by_name_that_not_exist(self):
        room_controller = RoomController()
        with self.assertRaises(RoomNotFoundError):
            room_controller.get_room_by_name("Bla")

    def test_remove_room_that_not_exist(self):
        room_controller = RoomController()
        with self.assertRaises(RoomNotFoundError):
            room_controller.delete_room_by_id(1)

    def test_alter_room_that_not_exist(self):
        room_controller = RoomController()
        with self.assertRaises(RoomNotFoundError):
            room_controller.alter_description_by_id(1, "test")
