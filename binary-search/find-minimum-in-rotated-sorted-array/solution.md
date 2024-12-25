```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = -1, len(nums) - 1
        while (r - l) > 1:
            mid = (r + l) // 2
            if nums[mid] > nums[-1]:
                l = mid
            else:
                r = mid
        return nums[r]
```