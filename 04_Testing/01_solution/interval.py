"""
This is the simple library you are to write unit tests for. You should consider what needs to be tested and how so that
every aspect of the library is thoroughly examined. You will need to call every method and function eventually, often
multiple times with different inputs to check different behaviour and conditions. Write unit tests in test_interval.py.
"""


class Interval:
    """
    An interval represents all the integers between a start and end value inclusive. For example, Interval(1,4) 
    represents the values [1,2,3,4] as a simpler object. The idea is to represent intervals in this way to easily check
    for ordering, overlap, intersection, union, etc. by having to consider the start and end values only. This can be
    used to represent dates on a calendar for an event, checking for overlap could be used to detect schedule conflicts.
    """

    def __init__(self, start, end):
        self._start = start
        self._end = end

    def start(self):
        return self._start

    def end(self):
        return self._end

    def length(self):
        return self._end - self._start

    def __iter__(self):
        return iter(range(self.start(), self.end() + 1))  # FIX

    def __eq__(self, other):
        return self.start() == other.start() and self.end() == other.end()

    def __repr__(self):
        return "Interval({}, {})".format(self._start, self._end)


# There are some bugs lurking in the following functions!
# Think about the relationships between them and what they are documented to do.


def ordered(i0, i1):
    """Returns (i0,i1) if `i0` starts before `i1`, (i1,i0) if `i1` starts first, (i0,i0) otherwise."""
    if i0.start() < i1.start():
        return i0, i1
    else:
        return i1, i0
    # FIX


def overlaps(i0, i1):
    """Returns True if `i0` and `i1` represent overlapping intervals."""
    return i0.end() >= i1.start() and i1.end() >= i0.start()  # FIX


def intersect(i0, i1):
    """Returns the Interval representing the overlapping range of `i0` and `i1`."""
    if overlaps(i0, i1):
        i0, i1 = ordered(i0, i1)
        interval = Interval(i1.start(), min(i0.end(), i1.end()))
        return interval if interval.length() > 0 else None


def union(i0, i1):
    """Returns the Interval representing the range coverd by both `i0` and `i1`."""
    if overlaps(i0, i1):
        return Interval(min(i0.start(), i1.start()), max(i0.end(), i1.end()))
    return None


def gaps(*intervals):
    """Yields the gaps as Interval objects between the memebrs of `intervals`."""
    first, *intervals = intervals

    for i in intervals:
        if first.end() <= i.start():  # FIX
            yield Interval(first.end(), i.start())
        first = i
