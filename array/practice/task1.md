```python
def sum_arrays(nums1, nums2):
    p1 = len(nums1) - 1
    p2 = len(nums2) - 1
    res = []
    carry = 0
    while p1 >= 0 or p2 >= 0 or carry > 0:
        el1 = nums1[p1] if p1 >= 0 else 0
        el2 = nums2[p2] if p2 >= 0 else 0
        cur_sum = el1 + el2 + carry
        res.append(cur_sum % 10)
        carry = cur_sum // 10
        p1 -= 1
        p2 -= 1
    return res[::-1]
```