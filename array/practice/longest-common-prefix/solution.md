```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = []
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return "".join(pref)
            pref.append(char)
        return "".join(pref)
```