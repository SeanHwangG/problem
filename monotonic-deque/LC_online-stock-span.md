# [LC_online-stock-span](https://leetcode.com/problems/online-stock-span)

Write class StockSpanner which collects daily price quotes for some stock
Return span of that stock's price for the current day

```txt
Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
```

## Solution

```py
class StockSpanner:
  def __init__(self):
    self.stack = []

  def next(self, price):
    res = 1
    while self.stack and self.stack[-1][0] <= price:
      res += self.stack.pop()[1]
    self.stack.append([price, res])
    return res
```
