```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        diff = k % len(nums)
        n_map = {}
        for i, n in enumerate(nums):
            new_pos = i + diff
            if new_pos < len(nums):
                if i in n_map:
                    el = n_map[i]
                else:
                    el = n
                n_map[new_pos] = nums[new_pos]
                nums[new_pos] = el
            else:
                new_pos %= len(nums)
                nums[new_pos] = n_map.get(i, n)
```
*Эталон*
```python
class Solution:
    def reverse(self, nums: List[int], l: int, r: int):
        r -= 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums))
        self.reverse(nums, 0, k)
        self.reverse(nums, k, len(nums))
```