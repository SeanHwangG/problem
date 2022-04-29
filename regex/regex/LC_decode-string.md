# [LC_decode-string](https://leetcode.com/problems/decode-string)

Encoding rule is: k[encoded_string], where encoded_string inside square brackets is being repeated exactly k times
Note that k is guaranteed to be a positive integer

```txt
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

## Solution

```py
import re
def decodeString(self, s: str) -> str:
  while '[' in s:
    s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
  return s
```
