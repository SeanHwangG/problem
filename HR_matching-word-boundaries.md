{% tabs %}{% tab title='HR_matching-word-boundaries.py' %}

```py
import re
pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}{% endtabs %}
