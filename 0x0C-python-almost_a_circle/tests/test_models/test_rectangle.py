#!/usr/bin/python3
""" Test Rectangle Module
"""


import os
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rect(self):
        r = Rectangle(10, 10)
        self.assertEqual(r.id, 1)

    def test_rect2(self):
        r = Rectangle(1, 5)
        self.assertEqual(r.id, 2)

    def test_rect3(self):
        r = Rectangle(11, 15, 0, 0, 12)
        self.assertEqual(r.id, 12)
