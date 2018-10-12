from flask_testing import TestCase

from app.create_app import create_app
from app.models import db


class BaseTests(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
    TESTING = True

    def create_app(self):

        # pass in test configuration
        return create_app()

    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()
