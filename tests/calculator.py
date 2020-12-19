import unittest
from calculator import simple_call

def calculate(x):
    """Call simple_call and return only result."""
    return simple_call(x, 2)[0]


class TestCalculator(unittest.TestCase):
    
    def test_detect_number(self):
        self.assertEqual(calculate("0 + 1"), 1) # Integer numbers
        self.assertEqual(calculate("2.3 + 4.5"), 6.8) # Float numbers
        self.assertEqual(calculate("-6 + -7.8"), -13.8) # Negative numbers


    def test_calculations(self):
        self.assertEqual(calculate("0 + 1"), 1) # Addition
        self.assertEqual(calculate("2 - 3"), -1) # Subtraction
        self.assertEqual(calculate("4--5"), 9) # Subtraction negative number
        self.assertEqual(calculate("6*7"), 42) # Multiplication
        self.assertEqual(calculate("8/9"), 0.89) # Division
        self.assertEqual(calculate("10^11"), 100000000000) # Raising to a power


    def test_calculations_roots(self):
        self.assertEqual(calculate("√0"), 0) # Square root
        self.assertEqual(calculate("∛1"), 1) # Cube root
        self.assertEqual(calculate("∜2"), 1.19) # Fourth root


    def test_parentheses(self):
        self.assertEqual(calculate("0 + (1 + 2)"), 3) # One parentheses
        self.assertEqual(calculate("(3 + 4) + (5 + 6)"), 18) # Two parentheses
        self.assertEqual(calculate("7 + (8 + (9 + 10))"), 34) # Parentheses inside parentheses
        self.assertEqual(calculate("11 + ((12 + 13) + 14)"), 50) # Parentheses inside parentheses variant 2
        self.assertEqual(calculate("(15 + (16 + 17)) + (18 + 19)"), 85) # Parentheses inside and outside parentheses
        self.assertEqual(calculate("(20 + 21)(22 + 23)"), 1845) # Multiplication witout mark
        