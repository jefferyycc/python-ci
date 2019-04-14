import unittest
import pytest
from src.math import Math


class MathTest(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(Math.increment(3), 4)

    def test_increment(self):
        self.assertEqual(Math.decrement(3), 2)
