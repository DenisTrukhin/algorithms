```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = []
        for c in path + "/":
            if c == "/":
                if curr:
                    curr = "".join(curr)
                    if curr == ".":
                        pass
                    elif curr == "..":
                        if stack:
                            stack.pop()
                    else:
                        stack.append(curr)
                    curr = []
            else:
                curr.append(c)
        return f"/{'/'.join(stack)}"
```