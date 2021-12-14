{% tabs %}{% tab title='BJ_5063.py' %}

```py
for _ in range(int(input())):
  r, e, c = map(int, input().split())
  if r > e - c:
    print('do not advertise')
  elif r == e - c:
    print('does not matter')
  else:
    print('advertise')
```

{% endtab %}{% endtabs %}
