from flask_testing import TestCase
from flask import current_app
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config["TESTING"]=True
        app.config["WFT_CSRF_ENABLOED"]= False
        return app
    
    def test_app_exist(self):
        self.assertIsNotNone(current_app)

