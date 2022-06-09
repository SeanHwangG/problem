# [LC_check-if-move-is-legal](https://leetcode.com/problems/check-if-move-is-legal)

* en

  ```en
  You are given a 0-indexed 8 x 8 grid board, where board[r][c] represents cell (r, c) on a game board
  On board, free cell is represented by '.', white cell is represented by 'W', and black cell is represented by 'B'
  Move is only legal if, after changing it, cell becomes endpoint of a good line (horizontal, vertical, or diagonal)
  Good line is has three or more cells (including endpoints) where endpoints are in once color, and remainings are opposite
  Given two integers r, c and player color (white or black), return if move is legal
  ```

* tc

  ```tc
  Input: board =
  [[".",".",".","B",".",".",".","."],
   [".",".",".","W",".",".",".","."],
   [".",".",".","W",".",".",".","."],
   [".",".",".","W",".",".",".","."],
   ["W","B","B",".","W","W","W","B"],
   [".",".",".","B",".",".",".","."],
   [".",".",".","B",".",".",".","."],
   [".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"
  Output: true

  Input: board =
  [[".",".",".",".",".",".",".","."],
   [".","B",".",".","W",".",".","."],
   [".",".","W",".",".",".",".","."],
   [".",".",".","W","B",".",".","."],
   [".",".",".",".",".",".",".","."],
   [".",".",".",".","B","W",".","."],
   [".",".",".",".",".",".","W","."],
   [".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"
  Output: false
  ```

## Solution

* py

  ```py
  def checkMove(self, G: List[List[str]], r: int, c: int, color: str) -> bool:
    for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1):
      i, j = r + dr, c + dc
      while 8 > i >= 0 <= j < 8 and G[i][j] not in '.' + color:
        i += dr
        j += dc
      if 8 > i >= 0 <= j < 8 and (abs(i - r) > abs(dr) or abs(j - c) > abs(dc)) and G[i][j] == color:
        return True
    return False
  ```
