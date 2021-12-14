{% tabs %}{% tab title='LC_305.py' %}

```py
def numIslands2(self, m, n, positions):
  counts, main, land = [], {}, {}
  for i, j in positions:
    p = i, j
    main[p], land[p] = p, [p]
    for q in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
      p, q = main[p], main.get(q)
      if not q or p == q:
        continue
      if len(land[p]) < len(land[q]):
        p, q = q, p
      land[p] += land[q]
      for l in land.pop(q):
        main[l] = p
    counts += len(land),
  return counts
```

{% endtab %}{% endtabs %}
