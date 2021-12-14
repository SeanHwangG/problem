{% tabs %}{% tab title='KT_qaly.py' %}

```py
n_line = int(input())
ret = 0
for _ in range(n_line):
  a, b = map(float, input().split())
  ret += a * b
print(ret)
```

{% endtab %}{% endtabs %}
