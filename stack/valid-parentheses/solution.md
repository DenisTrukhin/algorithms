```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = {"(", "[", "{"}
        brackets_map = {")": "(", "]": "[", "}": "{"}
        for b in s:
            if b in open_brackets:
                stack.append(b)
            else:
                if not stack:
                    return False
                if stack.pop() != brackets_map[b]:
                    return False
        return len(stack) == 0
```