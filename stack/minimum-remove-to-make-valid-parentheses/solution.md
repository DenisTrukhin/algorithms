```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s_list = list(s)
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    s_list[i] = "#"
        for i in stack:
            s_list[i] = "#"
        return "".join([c for c in s_list if c != "#"])
```

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        balance = 0
        s_list = list(s)
        for i, c in enumerate(s):
            if c == "(":
                balance += 1
            if c == ")":
                if balance == 0:
                    s_list[i] = "#"
                else:
                    balance -= 1
        balance = 0
        for i, c in enumerate(s[::-1]):
            if c == ")":
                balance += 1
            if c == "(":
                if balance == 0:
                    s_list[len(s) - i - 1] = "#"
                else:
                    balance -= 1
        return "".join([c for c in s_list if c != "#"])
```