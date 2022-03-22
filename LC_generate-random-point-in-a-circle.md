{% tabs %}{% tab title='LC_478.py' %}

```py
import math
import random
def __init__(self, radius, x_center, y_center):
  self.radius = radius
  self.x_center = x_center
  self.y_center = y_center
  random.seed()
def randPoint(self):
  degree = random.uniform(0, 2 * math.pi)
  dist = (2 * random.uniform(0, self.radius ** 2 / 2.0)) ** (1/2.0)
  x = dist * math.cos(degree)
  y = dist * math.sin(degree)
  return [self.x_center + x, self.y_center + y]
```

{% endtab %}{% endtabs %}