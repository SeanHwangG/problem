```py
def maxArea(self, h: int, w: int, horizontals: List[int], verticals: List[int]) -> int:
  H = sorted([0] + horizontals + [h])
  V = sorted([0] + verticals + [w])
  return max(j - i for i, j in zip(H, H[1:])) * max(j - i for i,j in zip(V, V[1:])) % (10 ** 9 + 7)
```
