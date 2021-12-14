{% tabs %}{% tab title='KT_beavergnaw.py' %}

```py
import math
while True:
  a, b = map(int, input().split())
  if a == b == 0:
    break
  print((a * a * a - 6 * b / math.pi) ** (1/3))
```

{% endtab %}{% endtabs %}
