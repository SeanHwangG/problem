{% tabs %}{% tab title='LC_363.py' %}

```py
from sortedcontainers import SortedList

def maxSumSubmatrix(self, M, k):
  def countRangeSum(nums, U):
    SList, ans = [0], -float("inf")
    for s in accumulate(nums):
      idx = bisect_left(SList, s - U)
      if idx < len(SList): ans = max(ans, s - SList[idx])
      bisect.insort(SList, s)
    return ans

  m, n, ans = len(M), len(M[0]), -float("inf")

  for i, j in product(range(1, m), range(n)):
    M[i][j] += M[i-1][j]

  M = [[0] * n] + M
  for r1, r2 in combinations(range(m + 1), 2):
    row = [j - i for i, j in zip(M[r1], M[r2])]
    ans = max(ans, countRangeSum(row, k))

  return ans
```

{% endtab %}{% endtabs %}
