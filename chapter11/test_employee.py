import unittest
from Employee import Employee

class TestEmployeeRaise(unittest.TestCase):
    def setUp(self):
        self.lain = Employee('lain','iwakura', 200000)

    def test_give_default_raise(self):
        self.lain.give_raise()
        self.assertEqual(self.lain.annual_salary, 205000)

    def test_give_custom_raise(self):
        self.lain.give_raise(10000)
        self.assertEqual(self.lain.annual_salary, 210000)
    
if __name__ == '__main__':
    unittest.main()
