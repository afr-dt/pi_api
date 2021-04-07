import os
import unittest

from flask import current_app
from flask_testing import TestCase
from manage import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == os.environ['DATABASE_URL']
        )


if __name__ == '__main__':
    unittest.main()
