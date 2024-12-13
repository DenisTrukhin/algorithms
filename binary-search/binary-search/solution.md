```python
class Solution:
    def good(self, n, target):
        return n <= target 
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while r - l > 1:
            mid = (r + l) // 2
            if self.good(nums[mid], target):
                l = mid
            else:
                r = mid
        return l if nums[l] == target else -1
```