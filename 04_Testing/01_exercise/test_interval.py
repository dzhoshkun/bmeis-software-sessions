"""
Here is where we want you to write your unit tests for the Interval library. You should write enough tests to exercise
all the functionality (ie. test each method and function) the library provides. This will involve calling functions and
methods multiple times with different input to test different behaviour. Remember that the tests are meant to find bugs
not show the Interval library is perfect, it might well be a huge bug's nest but who knows? Your tests should represent
what it should do, not reflect what it actually does.
"""

from unittest import TestCase
from .interval import Interval, ordered, overlaps, intersect, union, gaps


class IntervalPair:

    def __init__(self, iv_tuple_1, iv_tuple_2):
        self.iv1 = Interval(iv_tuple_1[0], iv_tuple_1[1])
        self.iv2 = Interval(iv_tuple_2[0], iv_tuple_2[1])


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
        self.non_overlapping_interval_pairs = [
            IntervalPair((1, 5), (10, 25)),
            IntervalPair((10, 25), (1, 5)),
            IntervalPair((10, 25), (26, 34)),
            IntervalPair((26, 34), (10, 25)),
        ]
        self.overlapping_interval_pairs = [
            IntervalPair((1, 10), (8, 15)),
            IntervalPair((8, 15), (1, 10)),
            IntervalPair((8, 15), (15, 25)),
            IntervalPair((15, 25), (8, 15)),
            IntervalPair((-5, 3), (1, 10)),
            IntervalPair((1, 10), (-5, 3)),
            IntervalPair((-5, 1), (1, 10)),
            IntervalPair((1, 10), (-5, 1)),
        ]

    def test_overlap(self):
        """Test overlaps() on intervals which don overlap."""
        self.assertTrue(overlaps(self.iv3, self.iv1))
        self.assertTrue(overlaps(self.iv3, self.iv4))
        for interval_pair in self.overlapping_interval_pairs:
            self.assertTrue(overlaps(interval_pair.iv1, interval_pair.iv2))
        
    def test_not_overlap(self):
        """Test overlaps() on intervals which don't overlap."""
        self.assertFalse(overlaps(self.iv0, self.iv1))
        for interval_pair in self.non_overlapping_interval_pairs:
            self.assertFalse(overlaps(interval_pair.iv1, interval_pair.iv2))
        
    def test_ordered(self):
        """
        Provide tests here to ensure ordered() behaves correctly. This may require multiple tests with different input.
        """
        raise NotImplementedError()

    def test_not_ordered(self):
        raise NotImplementedError()

    def test_intersect(self):
        """Test intersection with small and large values of overlap, and intervals entirely within the other."""
        raise NotImplementedError()

    def test_not_intersect(self):
        raise NotImplementedError()

    def test_union(self):
        raise NotImplementedError()

    def test_empty_union(self):
        raise NotImplementedError()

    def test_intervals_with_gaps(self):
        raise NotImplementedError()

    def test_intervals_with_no_gaps(self):
        raise NotImplementedError()

    def test_intervals_with_and_without_gaps(self):
        raise NotImplementedError()
        
    # However many more tests are needed to ensure all of the code given to you has been executed at least once
