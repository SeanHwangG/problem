{% tabs %}{% tab title='LC_1275.py' %}

```py
def tictactoe(self, M: List[List[int]]) -> str:
  def check(r, c, f):
    if all(B[r][i] == f for i in range(3)) or all(B[i][c] == f for i in range(3)):
      return True
    if r == c and all(B[i][i] == f for i in range(3)):
      return True
    if r+c == 2 and all(B[2-i][i] == f for i in range(3)):
      return True
    return False

  B = [[0] * 3 for _ in range(3)]
  for i, (r, c) in enumerate(M):
    if i % 2 == 0:
      B[r][c] = 'X'
      if check(r, c, 'X'):
        return 'A'
    else:
      B[r][c] = 'O'
      if check(r, c, 'O'):
        return 'B'
  return 'Draw' if len(M) == 9 else 'Pending'
```

{% endtab %}{% endtabs %}
