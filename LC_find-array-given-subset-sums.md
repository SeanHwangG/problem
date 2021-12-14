{% tabs %}{% tab title='LC_1982.py' %}

* After sort nums, than x or -x is equal to nums[1] - nums[0] and recurse
* Time: O(2^n x n)
* Space: O(2^n)

```py
def recoverArray(self, n, sums):
  def dfs(n, sums):
    if n == 1 and 0 in sums:
      return [max(sums, key = abs)]
    cands = []
    d = sums[1] - sums[0]

    for dr in [1, -1]:
      cnt, new = Counter(sums), []
      if cnt[0] == 0: return []
      for num in sums[::-dr]:
        if cnt[num] == 0: continue
        if cnt[num - d * dr] == 0: break
        cnt[num] -= 1
        new += [num]
        cnt[num - d * dr] -= 1

      if len(new) == 1 << (n1- 1):
        cands += [[-d * dr] + dfs(n - 1, new[::-dr])]

    return max(cands, key = len)

  return dfs(n, sorted(sums))
```

{% endtab %}{% endtabs %}
