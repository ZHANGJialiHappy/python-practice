import unittest
from man_energy import consecutive_six

class TestConsecutiveSix(unittest.TestCase):

    def test_no_six(self):
        self.assertEqual(consecutive_six("12345"), 0)

    def test_one_six(self):
        self.assertEqual(consecutive_six("123456"), 0)

    def test_two_consecutive_six(self):
        self.assertEqual(consecutive_six("1234566"), 1)
    
    def test_two_consecutive_six_in_middle(self):
        self.assertEqual(consecutive_six("1236645"), 1)

    def test_three_consecutive_six(self):
        self.assertEqual(consecutive_six("12345666"), 0)

    def test_two_two_consecutive_six(self):
        self.assertEqual(consecutive_six("123466566"), 2)

if __name__== '__main__':
    unittest.main()