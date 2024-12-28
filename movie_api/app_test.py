import unittest
from movie_api.models import Movie, Genre, db

class TestNegativeSum(unittest.TestCase):
    def test_negative_sum(self):
        self.assertEqual(-1 + -1, -2)

if __name__ == '__main__':
    unittest.main()
