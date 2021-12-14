{% tabs %}{% tab title='HR_ip-address-validation.py' %}

```py
import re

number = int(input())
RE_IPV4 = r'^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
RE_IPV6 = r'^([a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4})$'
for n in range(number):
  string = input()
  if re.search(RE_IPV4, string):
    print('IPv4')
  elif re.search(RE_IPV6, string):
    print('IPv6')
  else:
    print('Neither')
```

{% endtab %}{% endtabs %}
