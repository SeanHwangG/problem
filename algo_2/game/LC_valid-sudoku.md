# [LC_valid-sudoku](https://leetcode.com/problems/valid-sudoku)

Determine if a 9 x 9 Sudoku board is valid

```txt
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: true
```

## Solution

* py

  ```py
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    seen = set()
    for i, row in enumerate(board):
      for j, cval in enumerate(row):
        if cval != ".":
          if (cval, i) in seen or (j, cval) in seen or (i // 3, j // 3, cval) in seen:
            return False
          else:
            seen.add((cval, i))
            seen.add((j, cval))
            seen.add((i//3, j//3, cval))
    return True
  ```
