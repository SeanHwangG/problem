```py
def validTicTacToe(self, board):
  b = '|'.join(board)
  x, o = (any(p * 3 in b[s::d] for s in range(9) for d in (1, 3, 4, 5)) for p in 'XO') # 5 for diagonal
  m = b.count('X') - b.count('O')
  return m == (not o) if m else not x
```
