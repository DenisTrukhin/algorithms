```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_chars = []
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    return "".join(common_chars)
            common_chars.append(strs[0][i])
        return "".join(common_chars)
```