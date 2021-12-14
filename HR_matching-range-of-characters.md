{% tabs %}{% tab title='HR_matching-range-of-characters.py' %}

```py
import re
pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}{% endtabs %}
