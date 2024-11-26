time: O(n)
mem: O(n)
```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_arr = [0]
        suffix_arr = [0]
        for n in nums:
            prefix_arr.append(prefix_arr[-1] + n)
        for n in nums[::-1]:
            suffix_arr.append(suffix_arr[-1] + n)
        for i in range(len(nums)):
            if prefix_arr[i] == suffix_arr[len(nums)-i-1]:
                return i
        return -1 
```
Эталон
time: O(n)
mem: O(1)
```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        left_sum = 0
        for i, n in enumerate(nums):
            right_sum = nums_sum - left_sum - n
            if left_sum == right_sum:
                return i
            left_sum += n
        return -1
```