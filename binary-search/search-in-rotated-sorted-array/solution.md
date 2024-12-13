```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def good(val, target):
            return val > target
            
        def good2(val, target):
            return val <= target
        
        l, r = -1, len(nums) - 1
        while r - l > 1:
            m = (l + r) // 2
            if good(nums[m], nums[-1]):
                l = m
            else:
                r = m
        offset = r % len(nums)
        l, r = offset, offset + len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if good2(nums[m % len(nums)], target):
                l = m
            else:
                r = m
        return l % len(nums) if nums[l % len(nums)] == target else -1
```