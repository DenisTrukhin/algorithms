```python
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        def has_intersection(i1, i2):
            return max(i1[0], i2[0]) <= min(i1[1], i2[1])
        
        f, s = 0, 0
        result = []
        while f < len(firstList) and s < len(secondList):
            if has_intersection(firstList[f], secondList[s]):
                result.append([max(firstList[f][0], secondList[s][0]), min(firstList[f][1], secondList[s][1])])
            if firstList[f][1] < secondList[s][1]:
                f += 1
            else:
                s += 1
        return result
```