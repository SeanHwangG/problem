{% tabs %}{% tab title='KT_lastfactorialdigit.py' %}

```py
n_test = int(input())
for _ in range(n_test):
  n = int(input())
  ret = 1
  for i in range(1, n + 1):
    ret *= i
  print(ret % 10)
```

{% endtab %}{% endtabs %}
