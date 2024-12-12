import unittest
import unittest.mock
# from unittest import patch

from  _01_FixturesCmdline.src.simpleCalculator import Calculator

class TestSimpleCalculator(unittest.TestCase):

    @unittest.mock.patch('_01_FixturesCmdline.src.simpleCalculator.Calculator')
    def test_SimpleAdd(self, MockClass):
        instance = MockClass()
        instance.add.return_value = 77
        self.assertEqual(77, instance.add())
        self.assertIs(MockClass, Calculator)


    def test_SimpleSub(self):
        self.calc = Calculator(7, 4)
        self.assertEqual(3, self.calc.sub())

