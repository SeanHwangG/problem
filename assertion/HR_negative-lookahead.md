# [HR_negative-lookahead](https://www.hackerrank.com/challenges/negative-lookahead)

Match all characters which are not immediately followed by that same character

```txt
Input: gooooo
Output: 2
```

## Solution

```py
import re

Test_String = input()
pattern = r"(.)(?!\1)"
match = re.findall(pattern, Test_String)

print("Number of matches :", len(match))
```
