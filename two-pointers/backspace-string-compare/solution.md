```python
class Solution:
    def find_next_idx(self, s, i):
        skip_count = 0
        while i >= 0 and (skip_count > 0 or s[i] == "#"):
            if s[i] == "#":
                skip_count += 1
            else:
                skip_count -= 1
            i -= 1
        return i
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1, p2 = len(s), len(t)
        while p1 > 0 and p2 > 0:
            p1 = self.find_next_idx(s, p1 - 1)
            p2 = self.find_next_idx(t, p2 - 1)
            if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
                return False
        return self.find_next_idx(s, p1 - 1) == self.find_next_idx(t, p2 - 1)
```