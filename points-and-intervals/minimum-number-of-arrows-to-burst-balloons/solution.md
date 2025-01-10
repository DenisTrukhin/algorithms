```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def has_intersection(p1, p2):
            return max(p1[0], p2[0]) <= min(p1[1], p2[1])
        
        points.sort()
        intersection = points[0]
        arrows = 0
        for p in points[1:]:
            if has_intersection(intersection, p):
                intersection = [max(intersection[0], p[0]), min(intersection[1], p[1])]
            else:
                arrows += 1
                intersection = p
        return arrows + 1
```