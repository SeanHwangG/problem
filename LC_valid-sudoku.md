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
