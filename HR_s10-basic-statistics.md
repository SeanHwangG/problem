{% tabs %}{% tab title='HR_s10-basic-statistics.py' %}

```py
import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))
```

{% endtab %}{% endtabs %}
