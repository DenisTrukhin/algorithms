```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, -1
        zeros_count = 0
        max_seq = 0
        while l < len(nums):
            while r + 1 < len(nums) and (nums[r + 1] == 1 or zeros_count < k):
                r += 1
                if nums[r] == 0:
                    zeros_count += 1
            max_seq = max(max_seq, r - l + 1)
            if nums[l] == 0:
                zeros_count -= 1
            l += 1
        return max_seq
```