{% tabs %}{% tab title='BJ_5063.md' %}

* r is expected revenue if you do not advertise, e, is expected revenue if you do advertise, c, is cost of advertising

```txt
Input:
3
0 100 70
100 130 30
-100 -70 40

Output:
advertise
does not matter
do not advertise
```

{% endtab %}{% tab title='BJ_5063.py' %}

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