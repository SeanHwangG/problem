# [LC_largest-component-size-by-common-factor](https://leetcode.com/problems/largest-component-size-by-common-factor)

* en

  ```en
  There is edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1
  Return the size of the largest connected component in the graph
  ```

* tc

  ```tc
  Input: nums = [20,50,9,63]
  Output: 2
  ```

## Solution

* py

  ```py
  import collections
  import math
  class UF:
    def __init__(self, N):
      self.parent = list(range(N))
      self.size = [1] * N

    def find(self, x):
      if self.parent[x] != x:
        self.parent[x] = self.find(self.parent[x])
      return self.parent[x]

    def union(self, x, y):
      px, py = self.find(x), self.find(y)
      if px != py:
        size_x, size_y = self.size[px], self.size[py]
        if size_x < size_y:
          self.parent[px] = py
          self.size[py] += size_x
        else:
          self.parent[py] = px
          self.size[px] += size_y
  def largestComponentSize(self, A: List[int]) -> int:
    factor2i = collections.defaultdict(int)
    uf = UF(len(A))
    for i, num in enumerate(A):
      for factor in range(2, int(math.sqrt(num) + 1)):
        if num % factor == 0:
          for fac in (factor, num // factor):
            if fac in factor2i:
              uf.union(i, factor2i[fac])
            else:
              factor2i[fac] = i
      if num not in factor2i:
        factor2i[num] = i
      else:
        uf.union(i, factor2i[num])
    return max(uf.size)
  ```
