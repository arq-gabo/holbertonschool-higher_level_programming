#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Presence of docstring"""

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([8, 6, 4, 2]), 8)

    def test_basic_case(self):
        self.assertEqual(max_integer([1, 2, 3, 8]), 8)

    def text_negative_case(self):
        self.assertEqual(max_integer([-10, -3, -4, -1]), -1)

    def test_basic_empty(self):
       self.assertEqual(max_integer([]), None)

    def test_basic_float(self):
        self.assertEqual(max_integer([0.21, 2.3, 4.0]), 4.0)

    def test_basic_oneelement(self):
        self.assertEqual(max_integer([3]), 3)

    def test_basic_string(self):
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
