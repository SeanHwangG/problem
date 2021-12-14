{% tabs %}{% tab title='LC_1494.py' %}

```py
class Solution:
  def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
    post, pre = defaultdict(list), [0] * n
    for a, b in dependencies:
      pre[b-1] += 1
      post[a-1] += b-1,

    @lru_cache(None)
    def dfs(mask, pre):
      if not mask: return 0

      take = []
      for i in range(n):
        if mask & 1 << i and pre[i] == 0:
          take += i,

      res = inf
      for c in combinations(take, min(k, len(take))):
        m, d = mask, list(pre)
        for a in c:
          m ^= 1 << a
          for b in post[a]:
            d[b] -= 1
        res = min(res, 1 + dfs(m, tuple(d)))
      return res

    return dfs((1 << n) - 1, tuple(pre))
```

{% endtab %}{% endtabs %}
