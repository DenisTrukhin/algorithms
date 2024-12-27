```python
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        brackets_count = 0
        for c in A:
            if c == "(":
                brackets_count += 1
            else:
                brackets_count -= 1
                if brackets_count < 0:
                    return 0
        brackets_count = 0
        for c in A[::-1]:
            if c == ")":
                brackets_count += 1
            else:
                brackets_count -= 1
                if brackets_count < 0:
                    return 0
        return 1
```