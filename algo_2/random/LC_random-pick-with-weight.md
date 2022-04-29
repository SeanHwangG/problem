# [LC_random-pick-with-weight](https://leetcode.com/problems/random-pick-with-weight)

Given arr of positive integers w where w[i] describes the weight of ith index (0-indexed)
pickIndex(): return random integer in [0, w.length - 1], integer proportional to its weight in w array

```txt
Input
["Solution","pickIndex"]
[[[1]],[]]

Output
[null,0]
```

## Solution

* py

```py
from bisect import bisect_left

def __init__(self, w: List[int]):
  self.numbers = []
  total, count = sum(w), 0
  count = 0
  for index, value in enumerate(w):
    count += value
    self.numbers.append(count / total)

def pickIndex(self) -> int:
    return bisect_left(self.numbers, random.random(), 0, len(self.numbers) - 1)
```
