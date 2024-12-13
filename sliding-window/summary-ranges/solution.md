```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = r = 0
        result = []
        while l < len(nums):
            while r + 1 < len(nums) and nums[r] + 1 == nums[r + 1]:
                r += 1
            if l == r:
                result.append(str(nums[l]))
            else:
                result.append(f"{nums[l]}->{nums[r]}")
            l, r = r + 1, r + 1
        return result
```