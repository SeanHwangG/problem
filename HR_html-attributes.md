{% tabs %}{% tab title='HR_html-attributes.py' %}

```py
import re
from collections import defaultdict

tags = defaultdict(set)

for _ in range(int(input())):
  for tag, attrs in re.findall(r'<(\w+)(.*?)?>', input()):
    tags[tag].update(re.findall(r'\s(\w+)=', attrs))

for tag, attrs in sorted(tags.items()):
  print(f"{tag}:{','.join(sorted(attrs))}")
```

{% endtab %}{% endtabs %}
