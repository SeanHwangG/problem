{% tabs %}{% tab title='KT_taisformula.py' %}

```py
pa, pb = None, None
ret = 0
for _ in range(int(input())):
  a, b = map(float, input().split())
  if pa != None:
    ret += (a - pa) * (b + pb) / 2 / 1000
  pa, pb = a, b
print(ret)
```

{% endtab %}{% endtabs %}
