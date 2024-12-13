```python
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l, r = 0, 0
        result = 0
        while l < len(seats):
            while r + 1 < len(seats) and seats[r] == seats[r + 1]:
                r += 1
            if seats[r] == 0:
                seq_len = r - l + 1
                if l == 0 or r == len(seats) - 1:
                    result = max(result, seq_len)
                else:
                    result = max(result, (seq_len - 1) // 2 + 1)
            l, r = r + 1, r + 1
        return result
```