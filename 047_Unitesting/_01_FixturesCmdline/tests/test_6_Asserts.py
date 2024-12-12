import unittest

from  _01_FixturesCmdline.src.simpleCalculator import Calculator

class TestSimpleCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.calc = Calculator(7, 4)

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        del cls.calc

    def setUp(self):
        print("setUp")
        
    def tearDown(self):
        print("tearDown")


    def test_SimpleAdd(self):
        self.assertEqual(11, self.calc.add())

    def test_SimpleSub(self):
        self.assertEqual(3, self.calc.sub())

    def test_ZeroDiv(self):
        self.calc.b = 0
        self.assertRaises(ZeroDivisionError, self.calc.div)
