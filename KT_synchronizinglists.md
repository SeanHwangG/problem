{% tabs %}{% tab title='KT_synchronizinglists.py' %}

```py
while True:
  n = int(input())

  if n == 0:
    break

  l1 = [int(input()) for _ in range(n)]
  l2 = list(sorted([int(input()) for _ in range(n)]))
  rank = {}
  for i, e in enumerate(sorted(l1)):
    rank[e] = i
  for e in l1:
    print(l2[rank[e]])
  print()
```

{% endtab %}{% endtabs %}
