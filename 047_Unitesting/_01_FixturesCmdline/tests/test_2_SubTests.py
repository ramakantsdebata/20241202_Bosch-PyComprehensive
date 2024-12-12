import unittest

class NumbersTest(unittest.TestCase):
    def test_even(self):
        """Test the numbers from 0-5 for being even"""
        for num in range(0, 6):
            with self.subTest(testNo = num):
                self.assertEqual(0, num%2)