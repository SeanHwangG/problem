* Binary Search

```py
def minArea(self, image: List[List[str]], x: int, y: int) -> int:
  def first(lo, hi, check):
    class Checker:
      __getitem__ = staticmethod(check)
    return bisect.bisect(Checker(), False, lo, hi)
  top    = first(0, x,             lambda x: '1' in image[x])
  bottom = first(x, len(image),    lambda x: '1' not in image[x])
  left   = first(0, y,             lambda y: any(row[y] == '1' for row in image))
  right  = first(y, len(image[0]), lambda y: all(row[y] == '0' for row in image))
  return (bottom - top) * (right - left)
```
