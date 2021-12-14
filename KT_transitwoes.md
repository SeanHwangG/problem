{% tabs %}{% tab title='KT_transitwoes.py' %}

```py
cur, t, n = map(int, input().split())
D = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
for d, b, c in zip(D, B, C):
  cur += d
  cur += (cur % c)
  cur += b
if cur + D[-1] < t:
  print("yes")
else:
  print("no")
```

{% endtab %}{% endtabs %}
