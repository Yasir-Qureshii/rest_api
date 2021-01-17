from django.test import TestCase
from .calc import add


class CalcTests(TestCase):
	def test_add_Numers(self):
		"""Test that two numbers are added together"""
		self.assertEqual(add(3, 8), 11)


# Test driven development(TDD): write the test before writing code
