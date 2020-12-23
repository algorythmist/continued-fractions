import unittest
import pytest
import math

# Fix pytest reporting: ModuleNotFoundError: No module named 'continued_fractions'
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir,"."))

from continued_fractions import *


class ContinuedFractionsTestCase(unittest.TestCase):

    def test_greater_than_one(self):
        l1 = compute_continued_fraction(52, 9)
        self.assertEqual([5, 1, 3, 2], l1)
        l2 = compute_continued_fraction(13, 8)
        self.assertEqual([1, 1, 1, 1, 2], l2)

    def test_less_than_one(self):
        l1 = compute_continued_fraction(5, 8)
        self.assertEqual([0, 1, 1, 1, 2], l1)
        l2 = compute_continued_fraction(7, 9)
        self.assertEqual([0, 1, 3, 2], l2)

    def test_one_over(self):
        l = compute_continued_fraction(1, 9)
        self.assertEqual([0, 9], l)

    def test_zero_numerator(self):
        self.assertEqual([0], compute_continued_fraction(0, 2))

    def test_zero_denominator(self):
        with pytest.raises(ValueError) as ve:
            compute_continued_fraction(2, 0)
        self.assertEqual("Denominator should not be 0", str(ve.value))

    def test_non_integers(self):
        self.assertEqual(compute_continued_fraction(5, 3),
                         compute_continued_fraction(5.2, 3.8))

    def test_unreduced(self):
        l1 = compute_continued_fraction(2, 4)
        self.assertEqual([0, 2], l1)
        l2 = compute_continued_fraction(9, 6)
        self.assertEqual([1, 2], l2)


    def test_continued_fraction_from_real(self):
        l1 = continued_fraction_from_real(2**(1/2),10)
        print(l1)
        l2 = continued_fraction_from_real(7 - 3 ** (1 / 2), 10)
        print(l2)
        l3 = continued_fraction_from_real(math.pi, 10)
        print(l3)
        print(continued_fraction_from_real(3 ** (1 / 2), 10))

    def test_restore(self):
        self.assertEqual(52 / 9, restore([5, 1, 3, 2]))
        self.assertEqual(13 / 8, restore([1, 1, 1, 1, 2]))
        self.assertEqual(0.5, restore([0,2]))