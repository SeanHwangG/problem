# [LC_design-tic-tac-toe](https://leetcode.com/problems/design-tic-tac-toe)

Implement the TicTacToe class:
TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that player with id player plays at the cell (row, col) of board
  Move is guaranteed to be a valid move

```txt
Input:
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]

Output:
[null, 0, 0, 0, 0, 0, 0, 1]
```

## Solution

* py

  ```py
  class TicTacToe(object):
    def __init__(self, n):
      self.n, self.count = n, collections.Counter()

    def move(self, row, col, player):
      for i, x in enumerate((row, col, row+col, row-col)):
        self.count[i, x, player] += 1
        if self.count[i, x, player] == self.n:
          return player
      return 0
  ```
