{% tabs %}{% tab title='AC_arc124_b.py' %}

```py
from collections import Counter

N = int(input())
a = list(map(int, input().split()))
b = sorted(map(int, input().split()))

X = set()
for j in range(N):
  x = a[0] ^ b[j]
  X.add(x)

ans = []
for x in sorted(X):
  c = sorted([av ^ x for av in a])
  if b == c:
    ans.append(x)

print(len(ans))
if ans:
  print(*ans, sep="\n")
```

{% endtab %}{% endtabs %}
