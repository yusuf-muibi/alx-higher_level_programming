#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
import math
from your_code_file import max_integer  # Replace 'your_code_file' with the actual name of your code file


class TestMaxInteger(unittest.TestCase):
    # Test Cases for Basic Functionality
    def test_max_integer_basic(self):
        """Test max_integer with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_negative_values(self):
        """Test max_integer with a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_mixed_values(self):
        """Test max_integer with a list of mixed positive and negative integers."""
        self.assertEqual(max_integer([10, -5, 8, 3]), 10)

    def test_max_integer_empty_list(self):
        """Test max_integer with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_max_integer_duplicate_values(self):
        """Test max_integer with a list of duplicate values."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_max_integer_single_value(self):
        """Test max_integer with a list containing a single element."""
        self.assertEqual(max_integer([42]), 42)

    def test_max_integer_float_values(self):
        """Test max_integer with a list of floating-point numbers."""
        self.assertEqual(max_integer([3.14, 2.71, 1.618]), 3.14)

    def test_max_integer_string_values(self):
        """Test max_integer with a list of strings."""
        self.assertEqual(max_integer(["apple", "banana", "orange"]), "orange")

    def test_max_integer_mixed_types(self):
        """Test max_integer with a list of mixed types (integers and strings)."""
        self.assertEqual(max_integer([1, 2, "three", 4]), 4)

    def test_max_integer_with_none_values(self):
        """Test max_integer with a list containing None values."""
        self.assertEqual(max_integer([None, 8, 12, None]), 12)

    def test_max_integer_with_empty_string(self):
        """Test max_integer with a list containing an empty string."""
        self.assertEqual(max_integer(["", "abc", "def"]), "def")

    def test_max_integer_with_spaces(self):
        """Test max_integer with a list containing strings with leading/trailing spaces."""
        self.assertEqual(max_integer(["   ", "  abc  ", "def"]), "def")

    # Additional Test Cases
    def test_max_integer_with_positive_and_negative_infinity(self):
        """Test max_integer with positive and negative infinity values."""
        self.assertEqual(max_integer([float("inf"), -float("inf"), 10]), float("inf"))

    def test_max_integer_with_nan_values(self):
        """Test max_integer with a list containing NaN values."""
        self.assertTrue(math.isnan(max_integer([float("nan"), 5, 3])))

    def test_max_integer_with_zero_values(self):
        """Test max_integer with a list containing zero values."""
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_max_integer_with_large_values(self):
        """Test max_integer with a list containing large integer values."""
        self.assertEqual(max_integer([1e20, -1e20, 1e19]), 1e20)


if __name__ == "__main__":
    unittest.main()
