{% tabs %}{% tab title='LC_1478.py' %}

* Time; O(KNN)
* Space; O(N)

```py
def minDistance(self, A: List[int], k: int) -> int:
  A.sort()
  n, B = len(A), [0]
  for i, a in enumerate(A):
    B.append(B[i] + a)

  def cal(i, j):
    m1, m2 = (i + j) // 2, (i + j + 1) // 2
    return (B[j + 1] - B[m2]) - (B[m1 + 1] - B[i])

  dp = [cal(0, j) for j in range(n)]  # minimum distance of i + 1 first house
  for k in range(2, k + 1):
    for j in range(n - 1, k - 2, -1):
      for i in range(k - 2, j):
        dp[j] = min(dp[j], dp[i] + cal(i + 1, j))
  return int(dp[-1])
```

{% endtab %}{% endtabs %}
