* Mark with negative
* Time: O((RxC)^2)
* Space: 1

```py
def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
  row, col = len(board), len(board[0])
  todo = False

  for r in range(row - 2):
    for c in range(col):
      if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:
        board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(board[r][c])
        todo = True

  for r in range(row):
    for c in range(col - 2):
      if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:
        board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])
        todo = True

  for c in range(col):
    wp = row - 1
    for r in range(row - 1, -1, -1):
      if board[r][c] > 0:
        board[wp][c] = board[r][c]
        wp -= 1

    for wp in range(wp, -1, -1):
      board[wp][c] = 0

  return self.candyCrush(board) if todo else board
```
