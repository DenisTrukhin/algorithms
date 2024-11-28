```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = 100_000
        for i in range(k - 1, len(nums)):
            min_diff = min(min_diff, nums[i] - nums[i - k + 1])
        return min_diff
```