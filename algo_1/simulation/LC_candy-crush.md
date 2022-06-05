# [LC_candy-crush](https://leetcode.com/problems/candy-crush)

```en
Simulate Candicrush
```

```txt
Input:
board =
[[110,5,112,113,114],
 [210,211,5,213,214],
 [310,311,3,313,314],
 [410,411,412,5,414],
 [5,1,512,3,3],
 [610,4,1,613,614],
 [710,1,2,713,714],
 [810,1,2,1,1],
 [1,1,2,2,2],
 [4,1,4,4,1014]]
Output:
[[0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [110,0,0,0,114],
 [210,0,0,0,214],
 [310,0,0,113,314],
 [410,0,0,213,414],
 [610,211,112,313,614],
 [710,311,412,613,714],
 [810,411,512,713,1014]]
```

## Solution

* Mark with negative
* Time: O((RxC)^2)
* Space: 1

* py

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
