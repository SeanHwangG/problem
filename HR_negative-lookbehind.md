{% tabs %}{% tab title='HR_negative-lookbehind.py' %}

```py
import re

pattern = r"(?<![aeiouAEIOU])."
match = re.findall(pattern, input)

print("Number of matches :", len(match))
```

{% endtab %}{% endtabs %}
