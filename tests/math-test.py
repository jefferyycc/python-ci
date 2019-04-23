import unittest
# import pytest
from src.math import Math

class MathTest(unittest.TestCase):
    def setUp(self):
        self.Math = Math()

    def test_increment_returns_correct_result(self):
        self.assertEqual(self.Math.increment(3), 4)

    def test_increment_returns_error_message_if_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.increment, 'three')

    def test_decrement_returns_correct_result(self):
        self.assertEqual(self.Math.decrement(3), 2)

    def test_decrement_returns_error_message_if_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.decrement, 'three')

    def test_addition_returns_correct_result(self):
        result = self.Math.addition(1, 2)
        self.assertEqual(3, result)

    def test_addition_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.addition, 'one', 'two')

    def test_addition_returns_error_message_if_x_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.addition, '1', 'two')

    def test_addition_returns_error_message_if_y_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.addition, 'one', '2')

    def test_subtraction_returns_correct_result(self):
        result = self.Math.subtraction(5, 2)
        self.assertEqual(3, result)

    def test_subtraction_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.subtraction, 'five', 'two')

    def test_subtraction_returns_error_message_if_x_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.subtraction, '5', 'two')

    def test_subtraction_returns_error_message_if_y_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.subtraction, 'five', '2')
        
    def test_multiply_returns_correct_result(self):
        result = self.Math.multiply(5, 2)
        self.assertEqual(10, result)

    def test_multiply_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.multiply, 'five', 'two')

    def test_multiply_returns_error_message_if_x_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.multiply, '5', 'two')

    def test_multiply_returns_error_message_if_y_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.multiply, 'five', '2')

    def test_division_returns_correct_result(self):
        result = self.Math.division(10, 2)
        self.assertEqual(5, result)

    def test_division_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.division, 'five', 'two')

    def test_division_returns_error_message_if_x_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.division, '5', 'two')

    def test_division_returns_error_message_if_y_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.division, 'five', '2')

