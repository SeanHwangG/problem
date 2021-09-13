{% tabs %}{% tab title='KT_fiftyshades.md' %}

* Count number of lines with rose or pink (Ignore case)

```txt
Input:
12
pink
tequilaSunrose
mExicanPInK
Coquelicot
turqrose
roSee
JETblack
pink
babypink
pInKpinkPinK
PInkrose
lazerlemon

Output: 9
```

{% endtab %}{% tab title='KT_fiftyshades.py' %}

```py
count = 0
for _ in range(int(input())):
  st = input().lower()
  if 'pink' in st or 'rose' in st:
    count += 1

print(count if count != 0 else "I must watch Star Wars with my daughter")
```

{% endtab %}{% endtabs %}
