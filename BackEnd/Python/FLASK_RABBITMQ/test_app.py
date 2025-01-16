import unittest
from unittest.mock import patch, MagicMock
from wsgi import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the testing client and database
        self.app = app
        self.client = app.test_client() 

    def test_ping_route(self):
        # Test the /ping route
        response = self.client.get('/ping')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "pong")

    @patch("uuid.uuid4")
    @patch("wsgi.send_message")
    def test_user_request_route(self, mock_send_message, mock_uuid):
        # Test the /user_request route
        mock_uuid.return_value = "test-uuid"
        response = self.client.post('/user_request', json={"request": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok", "uid": "test-uuid"})

    @patch("wsgi.send_message")
    def test_new_info_route(self, mock_send_message):
        # Test the /new_info route
        response = self.client.post('/new_info', json={"info": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok"})