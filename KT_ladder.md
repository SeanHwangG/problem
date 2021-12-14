{% tabs %}{% tab title='KT_ladder.py' %}

```py
import math
a, theta = map(int, input().split())
print(math.ceil(a / math.sin(theta / 180 * math.pi)))
```

{% endtab %}{% endtabs %}
