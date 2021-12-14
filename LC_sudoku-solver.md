{% tabs %}{% tab title='LC_37.py' %}

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

{% endtab %}{% endtabs %}
