1. С 2 циклами
```python
class Solution:
    def checkStr(self, s1: str, s2: str) -> bool:
        map_s = {}
        for i, c in enumerate(s1):
            val_seen_s = map_s.get(c)
            val_s2 = s2[i]
            if val_seen_s:
                if val_seen_s != val_s2:
                    return False
            else:
                map_s[c] = val_s2
        return True
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.checkStr(s, t) and self.checkStr(t, s)
```
2. С 1 циклом
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s, map_t = {}, {}
        for i in range(len(s)):
            if s[i] in map_s and map_s[s[i]] != t[i]:
                return False
            if t[i] in map_t and map_t[t[i]] != s[i]:
                return False
            map_s[s[i]] = t[i]
            map_t[t[i]] = s[i]
        return True
```