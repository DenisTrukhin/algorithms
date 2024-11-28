```python
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        length = max_len = 1
        for i in range(1, len(nums)):
            length = length + 1 if nums[i] > nums[i-1] else 1
            max_len = max(max_len, length) 
        return max_len
```
