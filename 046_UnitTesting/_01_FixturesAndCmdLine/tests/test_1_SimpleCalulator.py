import unittest
import sys
sys.path.insert(0, "..\\")

from _01_FixturesAndCmdLine.src.simpleCalculator import Calculator

class TestSimpleCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.obj = Calculator(1, 1)

    @classmethod
    def tearDownClass(cls):
        print("tearDownUpClass")
        del cls.obj

    def setUp(self):
        print("setUp")
        self.obj.a = 10
        self.obj.b = 5
    
    def tearDown(self):
        print("tearDown")
        self.obj.a = 0
        self.obj.b = 0

    def test_SimpleSub(self):
        self.assertEqual(5, self.obj.sub())

    def test_SimpleAdd(self):
        self.assertEqual(15, self.obj.add())

    @unittest.skip
    def test_SimpleMul(self):
        self.assertNotEqual(40, self.obj.mul())

# @unittest.skip
class TestSimpleCalculator_Copy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.obj = Calculator(1, 1)

    @classmethod
    def tearDownClass(cls):
        print("tearDownUpClass")
        del cls.obj

    def setUp(self):
        print("setUp")
        self.obj.a = 10
        self.obj.b = 5
    
    def tearDown(self):
        print("tearDown")
        self.obj.a = 0
        self.obj.b = 0

    def test_SimpleSub(self):
        self.assertEqual(5, self.obj.sub())

    def test_SimpleAdd(self):
        self.assertEqual(15, self.obj.add())

    @unittest.skip
    def test_SimpleMul(self):
        self.assertNotEqual(40, self.obj.mul())
