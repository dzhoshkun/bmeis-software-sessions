from unittest import TestCase
from interval import Interval, ordered, overlaps, intersect, union, gaps


class TestInterval(TestCase):
    """
    These tests achieve 100% code coverage, so by that metric at least are considered exhaustive. One thing they do 
    omit is checking that operators are commutative, eg. if overlaps(a,b) is correct then one should really check that
    overlaps(b,a) is also correct. I will leave as an exercise to the reader devising a way of checking this property
    in a more elegant manner than simply copy-pasting every test and flipping the arguments.
    
    We can get 100% coverage without testing ordered() directly, so should we?
    
    Another question is if the tests are exhaustive. We know that a test like overlaps(Interval(1,2), Interval(2,3)))
    should be equivalent to overlaps(Interval(1,2), Interval(2,4))) or any other case where the intervals do have
    overlap, so checking with other values would be equivalent tests. Are there situations where this isn't true but a
    test for it isn't present here? What about zero-length intervals like Interval(5,5) in tests? Invalid intevals
    like Interval(5,3)?
    """

    def test_repr(self):
        self.assertIsNotNone(repr(Interval(1, 2)))

    def test_iter(self):
        self.assertListEqual(list(Interval(1, 10)), list(range(1, 11)))

    def test_ordered(self):
        """Test ordering pairs of intervals with them in order, reversed order, and with pairs of identical values."""
        self.assertTupleEqual(ordered(Interval(1, 2), Interval(2, 3)), (Interval(1, 2), Interval(2, 3)))
        self.assertTupleEqual(ordered(Interval(2, 3), Interval(1, 2)), (Interval(1, 2), Interval(2, 3)))
        self.assertTupleEqual(ordered(Interval(1, 2), Interval(1, 2)), (Interval(1, 2), Interval(1, 2)))

    def test_overlap(self):
        """Test intervals overlap by 1, by a small value, and by a large value."""
        self.assertTrue(overlaps(Interval(1, 2), Interval(2, 3)))
        self.assertTrue(overlaps(Interval(1, 3), Interval(2, 4)))
        self.assertTrue(overlaps(Interval(1, 10), Interval(5, 15)))

    def test_not_overlap(self):
        """Test intervals do not overlap with a small and a large gap."""
        self.assertFalse(overlaps(Interval(1, 2), Interval(3, 4)))
        self.assertFalse(overlaps(Interval(1, 10), Interval(20, 30)))

    def test_intersect(self):
        """Test intersection with small and large values of overlap, and intervals entirely within the other."""
        self.assertTrue(intersect(Interval(1, 4), Interval(3, 5)))
        self.assertTrue(intersect(Interval(1, 10), Interval(5, 15)))
        self.assertTrue(intersect(Interval(1, 3), Interval(2, 3)))
        self.assertTrue(intersect(Interval(5, 10), Interval(1, 15)))

    def test_not_intersect(self):
        """Test no intersection between intervals with a small and a large gap."""
        self.assertFalse(intersect(Interval(1, 4), Interval(5, 8)))
        self.assertFalse(intersect(Interval(1, 4), Interval(9, 20)))

    def test_union(self):
        """Test uniting two intervals with small and large overlap."""
        self.assertEqual(union(Interval(1, 2), Interval(2, 4)), Interval(1, 4))
        self.assertEqual(union(Interval(1, 10), Interval(5, 15)), Interval(1, 15))

    def test_not_union(self):
        """Test attempting to unite two intervals with small and large gaps between them."""
        self.assertIsNone(union(Interval(1, 2), Interval(3, 4)))
        self.assertIsNone(union(Interval(1, 5), Interval(10, 20)))

    def test_gaps(self):
        """Test generating gap intervals between intervals with small and large gaps."""
        self.assertListEqual(list(gaps(Interval(1, 2), Interval(2, 5))), [Interval(2, 2)])
        self.assertListEqual(list(gaps(Interval(1, 2), Interval(4, 5))), [Interval(2, 4)])
        self.assertListEqual(list(gaps(Interval(1, 2), Interval(4, 5), Interval(7, 9))), [Interval(2, 4), Interval(5, 7)])

    def test_not_gaps(self):
        """Test the lack of gaps between intersecting intervals."""
        self.assertListEqual(list(gaps(Interval(1, 3), Interval(2, 5))), [])
        self.assertListEqual(list(gaps(Interval(1, 9), Interval(2, 5))), [])
