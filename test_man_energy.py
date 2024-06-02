import unittest
from man_energy import consecutive_six

class TestConsecutiveSix(unittest.TestCase):

    def test_no_six(self):
        self.assertEqual(consecutive_six("12345"), 0)

if __name__== '__main__':
    unittest.main()