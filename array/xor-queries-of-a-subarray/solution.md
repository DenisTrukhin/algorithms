```python
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref_arr = [0]
        for n in arr:
            pref_arr.append(pref_arr[-1] ^ n)
        res = []
        for l, r in queries:
            res.append(pref_arr[r + 1] ^ pref_arr[l])
        return res
```