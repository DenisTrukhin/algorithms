```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = f = 0
        while f < len(nums):
            if nums[f] != 0:
                nums[s] = nums[f]
                s += 1
            f += 1
        while s < len(nums):
            nums[s] = 0
            s += 1
```