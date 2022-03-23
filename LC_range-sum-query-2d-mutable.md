```py
class NumMatrix(object):
  def __init__(self, G):
    for row in G:
      for col in range(1, len(row)):
        row[col] += row[col - 1]
    self.G = G

  def update(self, row, col, val):
    original = self.G[row][col]
    if col != 0:
      original -= self.G[row][col - 1]

    for y in range(col, len(self.G[0])):
      self.G[row][y] += val - original

  def sumRegion(self, row1, col1, row2, col2):
    ret = 0
    for x in range(row1, row2 + 1):
      ret += self.G[x][col2]
      if col1 != 0:
        ret -= self.G[x][col1-1]
    return ret
```
