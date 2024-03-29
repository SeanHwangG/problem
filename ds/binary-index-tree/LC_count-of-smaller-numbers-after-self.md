# [LC_count-of-smaller-numbers-after-self](https://leetcode.com/problems/count-of-smaller-numbers-after-self)

* en

  ```en
  Given int array nums and you have to return a new counts array
  Counts array has the property where counts[i] is the number of smaller elements to the right of nums[i]
  ```

* tc

  ```tc
  Input: nums = [5,2,6,1]
  Output: [2,1,1,0]
  ```

## Solution

* py

  ```py
  class BIT:
    def __init__(self, n):
      self.n = n + 1
      self.sums = [0] * self.n

    def update(self, i, delta):
      while i < self.n:
        self.sums[i] += delta
        i += i & (-i)

    def query(self, i):
      res = 0
      while i > 0:
        res += self.sums[i]
        i -= i & (-i)
      return res

  def countSmaller(self, li):
    ranks, bit, ret = {e : i + 1 for i, e in enumerate(sorted(li))}, self.BIT(len(li)), []
    for e in reversed(li):
      ret.append(bit.query(ranks[e] - 1))
      bit.update(ranks[e], 1)
    return ret[::-1]
  ```
