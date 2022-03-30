# [HR_matching-ending-items](https://www.hackerrank.com/challenges/matching-ending-items)

Should consist of only lowercase and uppercase letters (no numbers or symbols)
Should end in s

```txt
Input: Kites
Output: true
```

## Solution

```py
import re
pattern = r'^[a-zA-Z]*s$'
print(str(bool(re.search(pattern, input()))).lower())
```
