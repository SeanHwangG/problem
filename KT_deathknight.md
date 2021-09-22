{% tabs %}{% tab title='KT_deathknight.md' %}

* Given N lines, count number of lines without CD

```txt
Input:
3
DCOOO
DODOCD
COD

Output: 2
```

{% endtab %}{% tab title='KT_deathknight.py' %}

```py
n = int(input())
ret = 0
for _ in range(n):
  if 'CD' not in input():
    ret += 1
print(ret)
```

{% endtab %}{% endtabs %}
