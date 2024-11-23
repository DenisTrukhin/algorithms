```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cit_count = [0 for _ in range(len(citations) + 1)]
        for c in citations:
            cit_count[min(c, len(citations))] += 1
        count = 0
        for i in range(len(citations), -1, -1):
            count += cit_count[i]
            if count >= i:
                return i
        return count
```