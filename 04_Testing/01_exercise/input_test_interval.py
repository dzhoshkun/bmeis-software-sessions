from .interval import Interval


class IntervalPair:

    def __init__(self, iv_tuple_1, iv_tuple_2):
        self.iv1 = Interval(iv_tuple_1[0], iv_tuple_1[1])
        self.iv2 = Interval(iv_tuple_2[0], iv_tuple_2[1])

    def as_tuple(self):
        return self.iv1, self.iv2


NON_OVERLAPPING_INTERVAL_PAIRS = [
    IntervalPair((1, 5), (10, 25)),
    IntervalPair((10, 25), (1, 5)),
    IntervalPair((10, 25), (26, 34)),
    IntervalPair((26, 34), (10, 25)),
]
OVERLAPPING_INTERVAL_PAIRS = [
    IntervalPair((1, 10), (8, 15)),
    IntervalPair((8, 15), (1, 10)),
    IntervalPair((8, 15), (15, 25)),
    IntervalPair((15, 25), (8, 15)),
    IntervalPair((-5, 3), (1, 10)),
    IntervalPair((1, 10), (-5, 3)),
    IntervalPair((-5, 1), (1, 10)),
    IntervalPair((1, 10), (-5, 1)),
]
ORDERED_OVERLAPPING_INTERVAL_PAIRS = [
    IntervalPair((1, 10), (8, 20)),
    IntervalPair((1, 10), (8, 10)),
]
ORDERED_NON_OVERLAPPING_INTERVAL_PAIRS = [
    IntervalPair((1, 10), (11, 20)),
    IntervalPair((1, 10), (15, 20)),
]
UNORDERED_INTERVAL_PAIRS = [
    IntervalPair((0, 10), (-1, 9)),
]
