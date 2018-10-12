from datetime import datetime

from app.controller.schedule import ScheduleController
from app.tests import BaseTests
from app.exceptions.exceptions import UserNotFoundError, RoomNotFoundError


class ScheduleControllerTestCase(BaseTests):

    def setUp(self):
        super().setUp()
        self.schedule_controller = ScheduleController()

        self.schedule_controller.room_controller.create_room("Room to Schedule", "Description")
        self.schedule_controller.user_controller.create_user("User to Schedule")

        self.schedule_controller.create_schedule("2018-10-12", "User to Schedule", "Room to Schedule", "Description")

    def test_common(self):
        schedule = self.schedule_controller.get_schedule_by_id(1)
        self.assertEqual(schedule.date, datetime(2018, 10, 12).date())
        self.assertEqual(schedule.user.name, "User to Schedule")
        self.assertEqual(schedule.room.name, "Room to Schedule")

    def test_remove_schedule(self):
        self.assertTrue(self.schedule_controller.get_schedule_by_id(1))
        self.schedule_controller.remove_schedule_by_id(1)
        self.assertFalse(self.schedule_controller.get_schedule_by_id(1))

    def test_get_schedules_by_date(self):
        self.schedule_controller.room_controller.create_room("Room to Schedule 1", "Description")
        self.schedule_controller.create_schedule("2018-10-12", "User to Schedule", "Room to Schedule 1", "Description")

        schedules = self.schedule_controller.get_schedule_by_date("2018-10-12")
        self.assertEqual(len(schedules), 2)
        self.assertEqual(schedules[0].user.name, "User to Schedule")
        self.assertEqual(schedules[1].user.name, "User to Schedule")
        self.assertEqual(schedules[0].room.name, "Room to Schedule")
        self.assertEqual(schedules[1].room.name, "Room to Schedule 1")

    def test_create_schedule_to_user_that_not_exist(self):
        with self.assertRaises(UserNotFoundError):
            self.schedule_controller.create_schedule(
                "2018-10-12", "User that not exist", "Room to Schedule", "Description"
            )

    def test_create_schedule_to_room_that_not_exist(self):
        with self.assertRaises(RoomNotFoundError):
            self.schedule_controller.create_schedule(
                "2018-10-12", "User to Schedule", "Room that not exist", "Description"
            )

    def test_get_schedules_by_room_name(self):
        self.schedule_controller.create_schedule("2018-10-13", "User to Schedule", "Room to Schedule", "Description")
        schedules = self.schedule_controller.get_schedule_by_room_name("Room to Schedule")
        self.assertEqual(schedules[0].room.name, "Room to Schedule")
        self.assertEqual(schedules[1].room.name, "Room to Schedule")

    def test_alter_description(self):
        schedule = self.schedule_controller.get_schedule_by_id(1)
        self.assertEqual(schedule.description, "Description")

        self.schedule_controller.alter_description_by_id(1, "New description")

        schedule = self.schedule_controller.get_schedule_by_id(1)
        self.assertEqual(schedule.description, "New description")
