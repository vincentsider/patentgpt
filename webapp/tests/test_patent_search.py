import unittest
from webapp.patent_search import search_patent

class TestPatentSearch(unittest.TestCase):

    def setUp(self):
        self.query1 = "Artificial Intelligence"
        self.query2 = "Non-existing patent"

    def test_search_patent(self):
        result1 = search_patent(self.query1)
        result2 = search_patent(self.query2)

        self.assertIsNotNone(result1)
        self.assertIsNone(result2)

if __name__ == '__main__':
    unittest.main()