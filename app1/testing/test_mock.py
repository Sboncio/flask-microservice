from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    
    def test_lion(self):
        with patch('requests.get') as g:
            g.return_value.text = "lion"

            response = self.client.get(url_for('generateAnimal'))
            self.assertIn(b'roar',response.data)
