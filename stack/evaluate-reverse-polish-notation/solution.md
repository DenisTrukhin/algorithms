```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        math_operators = {"+", "-", "*", "/"}
        for t in tokens:
            if t in math_operators:
                s, f = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(f + s)
                elif t == "-":
                    stack.append(f - s)
                elif t == "*":
                    stack.append(f * s)
                else:
                    stack.append(int(f / s))
            else:
                stack.append(int(t))
        return int(stack[0])
```