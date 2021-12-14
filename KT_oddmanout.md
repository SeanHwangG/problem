{% tabs %}{% tab title='KT_oddmanout.py' %}

```py
for test in range(1, int(input()) + 1):
  N = int(input())
  ret = 0
  for x in map(int, input().split()):
    ret ^= x
  print(f"Case #{test}: {ret}")
```

{% endtab %}{% endtabs %}
