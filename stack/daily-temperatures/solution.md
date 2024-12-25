```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(0, temperatures[0])]
        result = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                last_idx, _ = stack.pop()
                result[last_idx] = i - last_idx
            stack.append((i, temperatures[i]))
        return result
```