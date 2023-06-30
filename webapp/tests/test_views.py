import unittest
from flask import url_for
from webapp import create_app, db
from webapp.models import User, Patent, CostEstimate

class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index_page(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_results_page(self):
        response = self.client.get(url_for('results'))
        self.assertEqual(response.status_code, 200)

    def test_cost_estimate_page(self):
        response = self.client.get(url_for('cost_estimate'))
        self.assertEqual(response.status_code, 200)

    def test_error_page(self):
        response = self.client.get(url_for('error'))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()