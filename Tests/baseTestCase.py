import unittest
from app import create_app, db

class BaseTestCase(unittest.TestCase):
    heladeria = None
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.heladeria = self.app.config['Heladeria']
