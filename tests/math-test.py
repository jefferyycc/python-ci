import unittest
# import pytest
from src.math import Math

class MathTest(unittest.TestCase):
    def test_increment_returns_correct_result(self):
        self.assertEqual(Math.increment(3), 4)

    def test_increment_returns_error_message_if_args_not_numbers(self):
        self.assertRaises(ValueError, Math.increment, 'three')

    def test_decrement_returns_correct_result(self):
        self.assertEqual(Math.decrement(3), 2)

    def test_decrement_returns_error_message_if_args_not_numbers(self):
        self.assertRaises(ValueError, Math.decrement, 'three')

    def test_addition_returns_correct_result(self):
        result = Math.addition(1, 2)
        self.assertEqual(3, result)

    def test_addition_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, Math.addition, 'one', 'two')

    def test_addition_returns_error_message_if_x_args_not_numbers(self):
        self.assertRaises(ValueError, Math.addition, '1', 'two')

    def test_addition_returns_error_message_if_y_args_not_numbers(self):
        self.assertRaises(ValueError, Math.addition, 'one', '2')

