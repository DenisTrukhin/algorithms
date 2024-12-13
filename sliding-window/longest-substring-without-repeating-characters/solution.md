```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, -1
        max_seq = 0
        seen_chars = set()
        while l < len(s):
            while r + 1 < len(s) and s[r + 1] not in seen_chars:
                seen_chars.add(s[r + 1])
                r += 1
            max_seq = max(max_seq, r - l + 1)
            seen_chars.remove(s[l])
            l += 1
        return max_seq
```