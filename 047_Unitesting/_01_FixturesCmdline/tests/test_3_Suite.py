import unittest

class MathTestClass(unittest.TestCase):
    def test_addition(self):
        result = 2 + 3
        self.assertEqual(result, 6, "2 + 3 should equal 5")


if __name__ == "__main__":
    print("Testing...")
    suite = unittest.TestLoader().loadTestsFromTestCase(MathTestClass)

    runner = unittest.TextTestRunner()

    runner.run(suite)