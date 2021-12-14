{% tabs %}{% tab title='HR_matching-specific-characters.py' %}

```py
import re
pattern = r'^[123][120][xs0][30Aa][xsu][.,]$'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}{% endtabs %}
