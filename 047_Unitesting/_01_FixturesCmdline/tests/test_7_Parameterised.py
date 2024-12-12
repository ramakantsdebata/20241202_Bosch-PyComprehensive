import unittest
from parameterized import parameterized, parameterized_class

from  _01_FixturesCmdline.src.simpleCalculator import Calculator

class TestSimpleCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # print("setUpClass")
        cls.calc = Calculator(0, 0)

    @classmethod
    def tearDownClass(cls):
        # print("tearDownClass")
        del cls.calc

    def setUp(self):
        # print("setUp")
        self.calc.a = 7
        self.calc.b = 4
        
    def tearDown(self):
        # print("tearDown")
        self.calc.a = 0
        self.calc.b = 0


    def test_SimpleAdd(self):
        self.calc.a = 10
        self.calc.b = 5
        self.assertEqual(15, self.calc.add())
 
    def test_SimpleAdd1(self):
        self.calc.a = 1
        self.calc.b = 5
        self.assertEqual(6, self.calc.add())
 
    def test_SimpleAdd2(self):
        self.calc.a = 100
        self.calc.b = 5
        self.assertEqual(105, self.calc.add())
 
    def test_SimpleAdd3(self):
        self.calc.a = 5
        self.calc.b = 5
        self.assertEqual(10, self.calc.add())
 
    def test_SimpleSub(self):
        self.assertEqual(3, self.calc.sub())


class TestSimpleCalculator_Param_Function(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # print("setUpClass")
        cls.calc = Calculator(0, 0)

    @classmethod
    def tearDownClass(cls):
        # print("tearDownClass")
        del cls.calc

    def setUp(self):
        # print("setUp")
        self.calc.a = 7
        self.calc.b = 4
        
    def tearDown(self):
        # print("tearDown")
        self.calc.a = 0
        self.calc.b = 0


    @parameterized.expand([
        (15, 10, 5),
        (6, 1, 5),
        (105, 100, 5),
        (10, 5, 5)
    ])
    def test_SimpleAdd(self, expec_res, first, second):
        self.calc.a = first
        self.calc.b = second
        self.assertEqual(expec_res, self.calc.add())
  
    def test_SimpleSub(self):
        self.assertEqual(3, self.calc.sub())



@parameterized_class(('expec_sum', 'expec_diff', 'first', 'second'), [
    (15, 5, 10, 5),
    (6, -4, 1, 5),
    (105, 95, 100, 5),
    (10, 0, 5, 5)
])
class TestSimpleCalculator_Param_Class(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # print("setUpClass")
        cls.calc = Calculator(0, 0)

    @classmethod
    def tearDownClass(cls):
        # print("tearDownClass")
        del cls.calc

    def setUp(self):
        # print("setUp")
        self.calc.a = self.first
        self.calc.b = self.second
        
    def tearDown(self):
        # print("tearDown")
        self.calc.a = 0
        self.calc.b = 0


    def test_SimpleAdd(self):
        # self.calc.a = first
        # self.calc.b = second
        self.assertEqual(self.expec_sum, self.calc.add())
  
    def test_SimpleSub(self):
        self.assertEqual(self.expec_diff, self.calc.sub())

