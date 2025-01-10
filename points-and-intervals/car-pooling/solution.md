```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = []
        for num_pass, start, end in trips:
            points.append((start, num_pass))
            points.append((end, -num_pass))
        points.sort()
        curr_num_pass = 0
        for p in points:
            curr_num_pass += p[1]
            if curr_num_pass < 0 or curr_num_pass > capacity:
                return False
        return True
```