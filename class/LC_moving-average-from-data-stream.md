# [LC_moving-average-from-data-stream](https://leetcode.com/problems/moving-average-from-data-stream)

Given a stream of integers and window size, calculate the moving average of all integers in the sliding window

```txt
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
```

## Solution

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
