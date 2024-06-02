from math import sqrt
import unittest
from exercise_2a import calculate_distance

class TestCalculateDistance(unittest.TestCase):
    def test_distance_between_same_point_is_zero(self):
        point = (3, 5)
        self.assertEqual(calculate_distance(point, point), 0)

    def test_distance_between_different_points(self):
        point1 = (1, 1)
        point2 = (4, 5)
        expected_distance = 5
        self.assertAlmostEqual(calculate_distance(point1, point2), expected_distance, places=6)

if __name__ == '__main__':
    unittest.main()