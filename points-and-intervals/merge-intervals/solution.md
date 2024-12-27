```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def has_intersection(i1, i2):
            return max(i1[0], i2[0]) <= min(i1[1], i2[1])
        
        intervals.sort(key=itemgetter(0))
        result = [intervals[0]]
        for i in intervals[1:]:
            last_result = result[-1]
            if has_intersection(i, last_result):
                result[-1] = [min(i[0], last_result[0]), max(i[1], last_result[1])]
            else:
                result.append(i)
        return result
```