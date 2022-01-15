{% tabs %}{% tab title='HR_s10-normal-distribution-1.py' %}

```py
import math
mean, std = 20, 2
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

print(f'{cdf(19.5):.3f}')         # Less than 19.5
print(f'{cdf(22) - cdf(20):.3f}') # Between 20 and 22
```

{% endtab %}{% endtabs %}
