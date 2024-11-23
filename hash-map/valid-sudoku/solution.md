1. Первое правильное решение
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            set_l = set()
            for j in range(9):
                if board[i][j] in set_l:
                    return False
                if board[i][j] != ".":
                    set_l.add(board[i][j])
        for j in range(9):
            set_c = set()
            for i in range(9):
                if board[i][j] in set_c:
                    return False
                if board[i][j] != ".":
                    set_c.add(board[i][j])
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                set_s = set()
                for l in range(3):
                    for c in range(3):
                        if board[i+l][j+c] in set_s:
                            return False
                        if board[i+l][j+c] != ".":
                            set_s.add(board[i+l][j+c])
        return True
```
2. Оптимальное решение
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lines = set()
        cols = set()
        blocks = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                block_idx = i // 3 * 3 + j // 3
                if (i, val) in lines or (j, val) in cols or (block_idx, val) in blocks:
                    return False
                lines.add(((i, val)))
                cols.add((j, val))
                blocks.add((block_idx, val))
        return True
```