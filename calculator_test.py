import unittest
from simple_calculator import SimpleCalculator
class CalculatorTest(unittest.TestCase):
    def setup(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2,3), -1)
        self.assertEqual(self.calc.subtract(1, 1), 0)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, -3), -6)
        self.assertEqual(self.calc.multiply(23, 0), 0)
        self.assertEqual(self.calc.multiply(3, 0), 0)
    def test_divide(self):
        self.assertEqual(self.calc(1, 2), 0.5)
        self.assertEqual(self.calc.divide(1, 0), "error! cannot divide by zero")
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.