```python
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = [False for _ in range(len(A)+1)]
        res = []
        curr = 0
        for i in range(len(A)):
            if seen[A[i]]:
                curr += 1
            seen[A[i]] = True
            if seen[B[i]]:
                curr += 1
            seen[B[i]] = True
            res.append(curr)
        return res
```