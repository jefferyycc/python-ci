import unittest
from src.math import Math

class MathTest(unittest.TestCase):
    def setUp(self):
        self.Math = Math()

    # Test increment
    def test_increment_returns_correct_result(self):
        self.assertEqual(self.Math.increment(3), 4)

    def test_increment_returns_error_message_if_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.increment, 'three')

    # Test decrement
    def test_decrement_returns_correct_result(self):
        self.assertEqual(self.Math.decrement(3), 2)

    def test_decrement_returns_error_message_if_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.decrement, 'three')

    # Test addition
    def test_addition_returns_correct_result(self):
        result = self.Math.addition(1, 2)
        self.assertEqual(3, result)

    def test_addition_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.addition, 'one', 'two')

    def test_addition_returns_error_message_if_x_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.addition, '1', 'two')

    def test_addition_returns_error_message_if_y_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.addition, 'one', '2')

    # Test subtraction
    def test_subtraction_returns_correct_result(self):
        result = self.Math.subtraction(5, 2)
        self.assertEqual(3, result)

    def test_subtraction_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.subtraction, 'five', 'two')

    def test_subtraction_returns_error_message_if_x_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.subtraction, '5', 'two')

    def test_subtraction_returns_error_message_if_y_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.subtraction, 'five', '2')

    # Test multiply
    def test_multiply_returns_correct_result(self):
        result = self.Math.multiply(5, 2)
        self.assertEqual(10, result)

    def test_multiply_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.multiply, 'five', 'two')

    def test_multiply_returns_error_message_if_x_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.multiply, '5', 'two')

    def test_multiply_returns_error_message_if_y_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.multiply, 'five', '2')

    # Test division
    def test_division_returns_correct_result(self):
        result = self.Math.division(10, 2)
        self.assertEqual(5, result)

    def test_division_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.division, 'five', 'two')

    def test_division_returns_error_message_if_x_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.division, '5', 'two')

    def test_division_returns_error_message_if_y_args_not_numbers(self):
        self.assertRaises(ValueError, self.Math.division, 'five', '2')

    # Test calculations
    def test_calculater_returns_correct_result(self):
        calc_str = "2 * 3 + 1"
        result = self.Math.calc(calc_str)
        self.assertEqual(7, result)

    def test_calculater_returns_correct_result_but_add_symbol_first(self):
        calc_str = "1 + 2 * 3"
        result = self.Math.calc(calc_str)
        self.assertEqual(7, result)

    def test_calculater_sub_div_returns_correct_result(self):
        calc_str = "9 / 3 + 1"
        result = self.Math.calc(calc_str)
        self.assertEqual(4, result)

    def test_calculater_sub_div_returns_correct_result_but_sub_symbol_first(self):
        calc_str = "1 + 9 / 3"
        result = self.Math.calc(calc_str)
        self.assertEqual(4, result)

    def test_calculater_all_symbols_returns_correct_result(self):
        calc_str = "2 - 9 / 3 + 2 + 1 * 7"
        result = self.Math.calc(calc_str)
        self.assertEqual(8, result)

    # Test calculations considering parentheses
    def test_calculater_parentheses_returns_correct_result(self):
        calc_str = "2 * (3 + 1)"
        result = self.Math.calc_p(calc_str)
        self.assertEqual(8, result)

    def test_calculater_parentheses_all_symbols_returns_correct_result(self):
        calc_str = "( 2 - 9 ) / 7 + ((2 + 1) * 7)"
        result = self.Math.calc_p(calc_str)
        self.assertEqual(20, result)

