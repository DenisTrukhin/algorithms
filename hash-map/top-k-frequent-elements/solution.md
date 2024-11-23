```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_f = defaultdict(int)
        for n in nums:
            map_f[n] += 1
        freq_reversed = [[] for _ in range(len(nums)+1)]
        for key, value in map_f.items():
            freq_reversed[value].append(key)
        res = []
        for f in freq_reversed[::-1]:
            if f:
                elements_remains = k - len(res)
                res.extend(f[:elements_remains])
                if len(res) == k:
                    break
        return res
```