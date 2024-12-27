```python
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class PointsComparator(tuple):
    def __le__(self, other):
        return self[0] < other[0] or (self[0] == other[0] and self[1] < other[1])

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        points = []
        for i in intervals:
            points.append((i.start, 1))
            points.append((i.end, -1))
        points.sort(key=PointsComparator)
        rooms, max_rooms = 0, 0
        for p in points:
            rooms += p[1]
            max_rooms = max(max_rooms, rooms)
        return max_rooms
```