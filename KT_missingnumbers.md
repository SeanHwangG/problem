{% tabs %}{% tab title='KT_missingnumbers.py' %}

```py
n = int(input())
gap = False
prev = 0
for i in range(n):
  a = int(input())
  for j in range(prev + 1, a):
    print(j)
    gap = True
  prev = a
if not gap:
  print('good job')
```

{% endtab %}{% endtabs %}
