import unittest
from calculator.__main__ import main as cal, make_correct as cor

def simple_cal(calculation: str):
    calculation = cor(calculation)
    result = cal(calculation)[0]
    result = round(result, 2)
    
    return result


class TestCalculator(unittest.TestCase):
    
    def test_detect_number(self):
        self.assertEqual(simple_cal("0 + 1"), 1) # Integer numbers
        self.assertEqual(simple_cal("2.3 + 4.5"), 6.8) # Float numbers
        self.assertEqual(simple_cal("-6 + -7.8"), -13.8) # Negative numbers


    def test_calculations(self):
        self.assertEqual(simple_cal("0 + 1"), 1) # Addition
        self.assertEqual(simple_cal("2 - 3"), -1) # Subtraction
        self.assertEqual(simple_cal("4--5"), 9) # Subtraction negative number
        self.assertEqual(simple_cal("6*7"), 42) # Multiplication
        self.assertEqual(simple_cal("8/9"), 0.89) # Division
        self.assertEqual(simple_cal("10^11"), 100000000000) # Raising to a power


    def test_calculations_roots(self):
        self.assertEqual(simple_cal("1√2"), 1.41) # Square root
        self.assertEqual(simple_cal("3∛4"), 4.76) # Cube root
        self.assertEqual(simple_cal("5∜6"), 7.83) # Fourth root


    def test_parentheses(self):
        self.assertEqual(simple_cal("0 + (1 + 2)"), 3) # One parentheses
        self.assertEqual(simple_cal("(3 + 4) + (5 + 6)"), 18) # Two parentheses
        self.assertEqual(simple_cal("7 + (8 + (9 + 10))"), 34) # Parentheses inside parentheses
        self.assertEqual(simple_cal("11 + ((12 + 13) + 14)"), 50) # Parentheses inside parentheses variant 2
        self.assertEqual(simple_cal("(15 + (16 + 17)) + (18 + 19)"), 85) # Parentheses inside and outside parentheses
        self.assertEqual(simple_cal("(20 + 21)(22 + 23)"), 1845) # Multiplication witout mark
        