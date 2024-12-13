```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_anagram = [0] * 26
        for c in s1:
            target_anagram[ord(c) - ord("a")] += 1
        
        i = 0
        cur_anagram = [0] * 26
        while i < len(s2):
            cur_anagram[ord(s2[i]) - ord("a")] += 1
            if i - len(s1) >= 0:
                cur_anagram[ord(s2[i - len(s1)]) - ord("a")] -= 1
            if cur_anagram == target_anagram:
                return True
            i += 1
        return False
```