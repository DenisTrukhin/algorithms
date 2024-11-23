1. Через хэш-таблицу
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = defaultdict(int)
        map_t = defaultdict(int)
        for i in range(len(s)):
            map_s[s[i]] += 1
            map_t[t[i]] += 1
        return map_s == map_t
```
2. Через массив
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0 for _ in range(26)]
        for c in s:
            counter[ord(c) - ord("a")] += 1

        for c in t:
            counter[ord(c) - ord("a")] -= 1
        return counter == [0 for _ in range(26)]
```