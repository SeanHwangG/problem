```py
class MovingAverage:
  def __init__(self, size):
    self.size = size
    self.arr = []

  def next(self, val):
    if len(self.arr) == self.size:
      self.arr.pop(0)

    self.arr.append(val)
    return sum(self.arr) / len(self.arr)
```
