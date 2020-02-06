"""
Here is where we want you to write your unit tests for the Interval library. You should write enough tests to exercise
all the functionality (ie. test each method and function) the library provides. This will involve calling functions and
methods multiple times with different input to test different behaviour. Remember that the tests are meant to find bugs
not show the Interval library is perfect, it might well be a huge bug's nest but who knows? Your tests should represent
what it should do, not reflect what it actually does.
"""

from unittest import TestCase
from .interval import Interval, ordered, overlaps, intersect, union, gaps


class TestOverlaps(TestCase):
    """
    Simple example of testing the `overlaps` function. This class is for testing this particular functionality but needs
    more unit test methods to do it comprehensively. Further classes can be defined in this file to test other aspects
    of the library.
    """

    def setUp(self):
        """Not a test case but a method for setting up testing data, called by TestCase when testing starts."""
        self.iv0 = Interval(1, 2)
        self.iv1 = Interval(3, 4)
        self.iv3 = Interval(1, 3)
        self.iv4 = Interval(2, 8)

    def test_overlap(self):
        """Test overlaps() on intervals which don overlap."""
        self.assertTrue(overlaps(self.iv3, self.iv1))
        self.assertTrue(overlaps(self.iv3, self.iv4))
        # test other overlapping intervals, ones with smaller or larger areas of overlap to show overlaps() works in a range of cases
        
    def test_not_overlap(self):
        """Test overlaps() on intervals which don't overlap."""
        self.assertFalse(overlaps(self.iv0, self.iv1))
        # test other overlapping intervals, ones with smaller or larger gaps between them
        
    def test_ordered(self):
        """Provide tests here to ensure ordered() behaves correctly. This may require multiple tests with different input."""

    def test_intersect(self):
        """Test intersection with small and large values of overlap, and intervals entirely within the other."""
        
    # However many more tests are needed to ensure all of the code given to you has been executed at least once
    