import unittest
import os

os.environ['TESTING'] = "TESTING"
from wsgi import app, db  # Import your app and db

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the testing client and database
        self.app = app
        self.client = app.test_client()  # Flask's built-in test client

        with app.app_context():
            db.create_all()  # Create tables

    def tearDown(self):
        # Tear down the test database
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_ping_route(self):
        # Test the /ping route
        response = self.client.get('/ping')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "pong")

    def test_database_insert(self):
        # Test inserting into the database
        from wsgi import Responses  # Assuming a Responses model exists
        with app.app_context():
            response = Responses(uuid="tesrffft", status=True)
            db.session.add(response)
            db.session.commit()
            query_result = Responses.query.first()
            self.assertTrue(query_result.status)

    def test_new_request_route(self):
        # Test the /new_request route
        uuid = "test0"
        response = self.client.post('/new_request', json={"uuid": uuid, "request": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok", "message": "Request created", "uuid": uuid})

    def test_update_response_route(self):
        # Test the /update_response route
        uuid = "test1"
        response = self.client.post('/new_request', json={"uuid": uuid, "request": "test"})
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/update_response', json={"uuid": uuid, "response": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok", "message": "Response updated", "uuid": uuid})

    def test_read_response_route(self):
        # Test the /read_response route
        uuid = "test2"
        response = self.client.post('/new_request', json={"uuid": uuid, "request": "test"})
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get(f'/read_response?uuid={uuid}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "processing", "response": None, "reason": None})

        response = self.client.post('/update_response', json={"uuid": uuid, "response": "test", "reason": "test reason"})
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f'/read_response?uuid={uuid}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok", "response": "test", "reason": "test reason"})

if __name__ == '__main__':
    unittest.main()
