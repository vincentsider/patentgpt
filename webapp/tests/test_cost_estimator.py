import unittest
from webapp.cost_estimator import estimate_cost

class TestCostEstimator(unittest.TestCase):

    def setUp(self):
        self.cost_low = 1000
        self.cost_high = 10000

    def test_estimate_cost(self):
        result = estimate_cost()
        self.assertTrue(self.cost_low <= result <= self.cost_high)

if __name__ == '__main__':
    unittest.main()