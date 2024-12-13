```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def good(val, target):
            return val <= target
        
        l, r = 0, len(matrix) * len(matrix[0])
        while r - l > 1:
            mid = (l + r) // 2
            row, col = divmod(mid, len(matrix[0]))
            if good(matrix[row][col], target):
                l = mid
            else:
                r = mid
        row, col = divmod(l, len(matrix[0]))
        return matrix[row][col] == target
```