{% tabs %}{% tab title='HR_split-number.py' %}

```py
import re
for i in range(int(input())):
  a, b, c = (re.sub(r"[ -]", " ", input())).split()
  print(f"CountryCode={a},LocalAreaCode={b},Number={c}")
```

{% endtab %}{% endtabs %}
