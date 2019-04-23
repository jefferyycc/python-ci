import unittest
# import pytest
from src.math import Math

class MathTest(unittest.TestCase):
    def test_increment_returns_correct_result(self):
        self.assertEqual(Math.increment(3), 4)


    def test_decrement_returns_correct_result(self):
        self.assertEqual(Math.decrement(3), 2)

    def test_addition_returns_correct_result(self):
        result = Math.addition(1, 2)
        self.assertEqual(3, result)
