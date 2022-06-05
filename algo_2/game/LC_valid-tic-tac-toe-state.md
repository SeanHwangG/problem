# [LC_valid-tic-tac-toe-state](https://leetcode.com/problems/valid-tic-tac-toe-state)

```en
Given Tic-Tac-Toe board as string array, return iff it's possible to reach this board position during game
Board is 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square
```

```txt
Input: board = ["XOX"," X ","   "]
Output: false
```

## Solution

* py

  ```py
  def validTicTacToe(self, board):
    b = '|'.join(board)
    x, o = (any(p * 3 in b[s::d] for s in range(9) for d in (1, 3, 4, 5)) for p in 'XO') # 5 for diagonal
    m = b.count('X') - b.count('O')
    return m == (not o) if m else not x
  ```
