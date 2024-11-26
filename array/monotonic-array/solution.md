```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_inc = is_dec = False
        for i in range(1, len(nums)):
            if is_inc is is_dec is False:
                is_inc = nums[i] > nums[i-1]
                is_dec = nums[i] < nums[i-1]
            else:
                if is_inc and nums[i] < nums[i-1]:
                    return False
                if is_dec and nums[i] > nums[i-1]:
                    return False
        return True 
```

*Эталон*
```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # идея в том, что нам не важно монотонно возрастает массив
        # или монотонно убыват, поэтому мы заводим 2 флага:
        # на монотонное возрастание и на монотонное убывание
        is_inc = True
        is_dec = True
        for i in range(1, len(nums)):
            is_inc = is_inc and nums[i - 1] <= nums[i]
            is_dec = is_dec and nums[i - 1] >= nums[i]
        return is_inc or is_dec
```