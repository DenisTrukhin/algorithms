```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps_map = defaultdict(int)
        ps_map[0] = 1
        result = cur_sum = 0
        for n in nums:
            cur_sum += n
            if cur_sum - k in ps_map:
                result += ps_map[cur_sum - k]
            ps_map[cur_sum] += 1
        return result
```