{% tabs %}{% tab title='KT_pot.py' %}

```py
n_line = int(input())
ret = 0
for _ in range(n_line):
  n = int(input())
  ret += (n // 10) ** (n % 10)
print(ret)
```

{% endtab %}{% endtabs %}
