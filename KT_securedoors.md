{% tabs %}{% tab title='KT_securedoors.py' %}

```py
N = int(input())
se = set()
for _ in range(N):
  typ, name = input().split()
  if typ == 'entry':
    if name in se:
      print(name, 'entered', '(ANOMALY)')
    else:
      print(name, 'entered')
      se.add(name)
  else:
    if name in se:
      print(name, 'exited')
      se.remove(name)
    else:
      print(name, 'exited', ('(ANOMALY)' if name not in se else ''))
```

{% endtab %}{% endtabs %}
