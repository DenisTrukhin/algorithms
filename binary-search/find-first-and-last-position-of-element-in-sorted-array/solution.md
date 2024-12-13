```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def good1(val, target):
            return val < target
        
        def good2(val, target):
            return val == target
            
        l, r = -1, len(nums) - 1
        while (r - l) > 1:
            mid = (r + l) // 2
            if good1(nums[mid], target):
                l = mid
            else:
                r = mid
        if nums[r] != target:
            return [-1, -1]
        
        start, l, r = r, r, len(nums)
        while (r - l) > 1:
            mid = (r + l) // 2
            if good2(nums[mid], target):
                l = mid
            else:
                r = mid
        return [start, l]
```