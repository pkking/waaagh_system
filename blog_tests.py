import os
os.environ['TYPE'] = 'TESTING'
from blog import app
import json
import unittest

class blogTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass
    
    def test_empty_post(self):
        # all the resources should return 404
        res = self.app.get('/posts')
        self.assertEqual(res.status_code, 404)
        self.assertIn('not any Post exist', json.loads(res.data.decode('utf-8'))['message'])
        res = self.app.get('/posts/1')
        self.assertEqual(res.status_code, 404)
        self.assertIn("Post id 1 doesn't exist", json.loads(res.data.decode('utf-8'))['message'])

    def test_empty_persion(self):
        # all the resources should return 404
        res = self.app.get('/persions')
        self.assertEqual(res.status_code, 404)
        self.assertIn('not any Persion exist', json.loads(res.data.decode('utf-8'))['message'])
        res = self.app.get('/persions/1')
        self.assertEqual(res.status_code, 404)
        self.assertIn("Persion id 1 doesn't exist", json.loads(res.data.decode('utf-8'))['message'])

    def test_empty_tag(self):
        # all the resources should return 404
        res = self.app.get('/tags')
        self.assertEqual(res.status_code, 404)
        self.assertIn('not any Tag exist', json.loads(res.data.decode('utf-8'))['message'])
        res = self.app.get('/tags/1')
        self.assertEqual(res.status_code, 404)
        self.assertIn("Tag id 1 doesn't exist", json.loads(res.data.decode('utf-8'))['message'])

if __name__ == '__main__':
    unittest.main()