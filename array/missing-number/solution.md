```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        range_sum = sum(i for i in range(1, len(nums) + 1))
        nums_sum = sum(nums)
        return range_sum - nums_sum
```