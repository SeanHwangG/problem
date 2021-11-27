{% tabs %}{% tab title='HR_s10-the-central-limit-theorem-1.py' %}

```py
from math import erf
sample, n_samples, mean, std = (int(input()) for _ in range(4))
sample_mean, sample_std = n_samples * mean, (n_samples**.5) * std

cdf = lambda x: .5 + .5 * erf((x - sample_mean) / 2 ** .5 / sample_std)
print(round(cdf(sample), 4))
```

{% endtab %}{% endtabs %}
