{% tabs %}{% tab title='KT_whatdoesthefoxsay.py' %}

```py
n_test = int(input())
for _ in range(n_test):
  li = input().split()
  s = input()
  ignore = set()
  while s != 'what does the fox say?':
    ignore.add(s.split()[-1])
    s = input()
  for e in li:
    if e not in ignore:
      print(e, end=' ')
```

{% endtab %}{% endtabs %}
