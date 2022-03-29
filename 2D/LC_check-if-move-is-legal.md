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
