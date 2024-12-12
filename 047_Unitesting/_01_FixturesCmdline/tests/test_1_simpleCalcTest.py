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
        # self.assertEqual(11, TestSimpleCalculator.calc.add())

    def test_SimpleSub(self):
        self.assertEqual(3, self.calc.sub())


class TestSimpleCalculator_02(unittest.TestCase):
    def test_SimpleMul(self):
        self.calc = Calculator(7, 4)
        self.assertEqual(28, self.calc.mul())

    def test_SimpleDiv(self):
        self.calc = Calculator(8, 4)
        self.assertEqual(2, self.calc.div())
