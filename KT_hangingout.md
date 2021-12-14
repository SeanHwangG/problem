{% tabs %}{% tab title='KT_hangingout.py' %}

```py
max_n, n_line = map(int, input().split())
cur, ret = 0, 0
for _ in range(n_line):
  st, n = input().split()
  n = int(n)
  if st == 'enter':
    if n + cur <= max_n:
      cur += n
    else:
      ret += 1
  else:
    cur -= n
print(ret)
```

{% endtab %}{% endtabs %}
