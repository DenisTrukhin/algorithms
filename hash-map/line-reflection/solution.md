```python
from typing import (
    List,
)

class Solution:
    """
    @param points: n points on a 2D plane
    @return: if there is such a line parallel to y-axis that reflect the given points
    """
    def is_reflected(self, points: List[List[int]]) -> bool:
        if points:
            min_x, max_x = points[0][0], points[0][0]
            u_points = set()
            for x, y in points:
                u_points.add((x, y))
                if x < min_x:
                    min_x = x
                elif x > max_x:
                    max_x = x
            for x, y in u_points:
                reflect_point = (min_x + max_x - x, y)
                if reflect_point not in u_points:
                    return False
        return True
```