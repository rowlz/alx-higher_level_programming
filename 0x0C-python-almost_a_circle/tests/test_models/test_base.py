#!/usr/bin/python3
""" Test Base Module
"""


import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_nb(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_nb2(self):
        b = Base()
        self.assertEqual(b.id, 2)

    def test_nb3(self):
        b = Base(12)
        self.assertEqual(b.id, 12)
