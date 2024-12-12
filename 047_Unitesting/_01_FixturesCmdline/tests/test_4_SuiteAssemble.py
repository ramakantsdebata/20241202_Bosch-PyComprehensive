import unittest
# from pdb import Pdb

class MathTestCase(unittest.TestCase):
    def test_addition(self):
        result = 2 + 3
        self.assertEqual(result, 5, "2 + 3 should equal 5")

    def test_subtraction(self):
        result = 7 - 4
        self.assertEqual(result, 3, "7 - 4 should equal 3")


class StringTestCase(unittest.TestCase):
    def test_Upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isUpper(self):
        self.assertTrue("foo".isupper())


class ListTestCase(unittest.TestCase):
    def test_append(self):
        my_list = []
        my_list.append(1)
        self.assertIn(1, my_list)

    def test_remove(self):
        my_list = [1, 2, 3]
        # Pdb.break_here()
        my_list.remove(1)
        self.assertNotIn(1, my_list)


def Suite():
    suite = unittest.TestSuite()

    suite.addTest(MathTestCase('test_addition'))
    suite.addTest(MathTestCase('test_subtraction'))

    suite.addTest(StringTestCase('test_Upper'))
    suite.addTest(StringTestCase('test_isUpper'))

    suite.addTest(ListTestCase('test_append'))
    suite.addTest(ListTestCase('test_remove'))

    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(Suite())