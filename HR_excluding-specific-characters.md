{% tabs %}{% tab title='HR_excluding-specific-characters.py' %}

```py
import re

pattern = r'^[^\d][^aeiou][^bcDF]\S[^AEIOU][^.,]$'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}{% endtabs %}
