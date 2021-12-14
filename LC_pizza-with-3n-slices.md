{% tabs %}{% tab title='LC_1388.py' %}

```py
def maxSizeSlices(self, A):
  @lru_cache(None)
  def dp(i, j, k, cycle=0):
    if k == 1: return max(A[i: j + 1])
    if j - i + 1 < k * 2 - 1: return -float('inf')
    return max(dp(i + cycle, j - 2, k - 1) + A[j], dp(i, j - 1, k))
  return dp(0, len(A) - 1, len(A) // 3, 1)
```

{% endtab %}{% endtabs %}
