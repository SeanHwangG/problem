{% tabs %}{% tab title='HR_s10-geometric-distribution-1.py' %}

```py
probability = list(map(int, input().split()))
p = probability[0] / probability[1]
q, n = 1 - p, int(input())

print(round(q ** (n - 1) * p, 3))
```

{% endtab %}{% endtabs %}
