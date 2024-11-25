```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_map = [0 for _ in range(26)]
        for c in p:
            p_map[ord(c) - ord("a")] += 1
        res = []
        s_map = [0 for _ in range(26)]
        for i in range(len(s)):
            s_map[ord(s[i]) - ord("a")] += 1    
            if i >= len(p):
                s_map[ord(s[i - len(p)]) - ord("a")] -= 1
            if s_map == p_map:
                res.append(i - len(p) + 1)
        return res
```