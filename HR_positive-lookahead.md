{% tabs %}{% tab title='HR_positive-lookahead.py' %}

```py
import re

Test_String = input()

pattern = r"o(?=oo)"
match = re.findall(pattern, Test_String)

print("Number of matches :", len(match))
```

{% endtab %}{% endtabs %}
