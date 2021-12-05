{% tabs %}{% tab title='LC_782.md' %}

* Given an n x n binary grid board. In each move, swap any two rows with each other, or any two columns with each other
* Return the minimum number of moves to transform the board into a chessboard board. If impossible, return -1
* A chessboard board is a board where no 0's and no 1's are 4-directionally adjacent.

```txt
Input: board =
[[0,1,1,0],
 [0,1,1,0],
 [1,0,0,1],
 [1,0,0,1]]

Output: 2
```

{% endtab %}{% tab title='LC_782.py' %}

1. In a valid chess board, there are 2 and only 2 kinds of rows and one is inverse to the other
    * (ex: if there is a row 01010011 in the board, any other row must be either 01010011 or 10101100)
1. Every row and column has half ones.
    * If N = 2 * K + 1, every row and every column has K ones and K + 1 zeros or K + 1 ones and K zeros

```py
def movesToChessboard(self, b):
  N = len(b)
  if any(b[0][0] ^ b[i][0] ^ b[0][j] ^ b[i][j] for i in range(N) for j in range(N)): return -1
  if not N // 2 <= sum(b[0]) <= (N + 1) // 2: return -1
  if not N // 2 <= sum(b[i][0] for i in range(N)) <= (N + 1) // 2: return -1
  col = sum(b[0][i] == i % 2 for i in range(N))
  row = sum(b[i][0] == i % 2 for i in range(N))
  if N % 2:
    if col % 2: col = N - col
    if row % 2: row = N - row
  else:
    col = min(N - col, col)
    row = min(N - row, row)
  return (col + row) // 2
```

{% endtab %}{% endtabs %}
