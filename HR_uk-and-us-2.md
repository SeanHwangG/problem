```py
import re
text = '\n'.join(input() for _ in range(int(input())))
for i in range(int(input())):
  s1 = input()
  s2 = s1.replace('our','or')
  print(len(re.findall(rf"\b({s1}|{s2})\b", text)))
```
