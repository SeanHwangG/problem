{% tabs %}{% tab title='LC_1643.py' %}

```py
from math import comb
def kthSmallestPath(self, destination: List[int], k: int) -> str:
  r, c = destination
  ret, remDown = [], r
  for i in range(r + c):
    remSteps = r + c - (i + 1)
    com = comb(remSteps, remDown)
    if com >= k:
      ret.append("H")
    else:
      remDown -= 1
      k -= com
      ret.append("V")
  return ''.join(ret)
```

{% endtab %}{% endtabs %}
