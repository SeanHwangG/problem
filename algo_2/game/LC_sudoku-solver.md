# [LC_sudoku-solver](https://leetcode.com/problems/sudoku-solver)

* en

  ```en
  Solve a Sudoku puzzle by filling the empty cells
  ```

* tc

  ```tc
  Input:
  board =
  [["5","3",".",".","7",".",".",".","."],
   ["6",".",".","1","9","5",".",".","."],
   [".","9","8",".",".",".",".","6","."],
   ["8",".",".",".","6",".",".",".","3"],
   ["4",".",".","8",".","3",".",".","1"],
   ["7",".",".",".","2",".",".",".","6"],
   [".","6",".",".",".",".","2","8","."],
   [".",".",".","4","1","9",".",".","5"],
   [".",".",".",".","8",".",".","7","9"]]

  Output:
  [["5","3","4","6","7","8","9","1","2"],
   ["6","7","2","1","9","5","3","4","8"],
   ["1","9","8","3","4","2","5","6","7"],
   ["8","5","9","7","6","1","4","2","3"],
   ["4","2","6","8","5","3","7","9","1"],
   ["7","1","3","9","2","4","8","5","6"],
   ["9","6","1","5","3","7","2","8","4"],
   ["2","8","7","4","1","9","6","3","5"],
   ["3","4","5","2","8","6","1","7","9"]]
  ```

## Solution

* py

  ```py
  def solveSudoku(self, board: List[List[str]]) -> None:
    box = lambda r, c: [(r - r % 3 + di, c - c % 3 + dj) for di in range(3) for dj in range(3)]
    neighs = lambda r, c: set([tup for k in range(9) for tup in [(k, c), (r, k)]] + box(r, c)) - {(r, c)}
    getCands = lambda r, c: set(map(str, range(1, 10))) - set(board[r][c] for r, c in neighs(r, c))

    for r, c in product(range(9), range(9)):
      if board[r][c] == '.':
        for x in getCands(r,c):
          board[r][c] = x
          if self.solveSudoku(board):
            return board
        board[r][c] = '.'
        return False
    return board
  ```
