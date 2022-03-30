# [HR_matching-start-end](https://www.hackerrank.com/challenges/matching-start-end)

Must start with a digit and end with . symbol
Should be characters long only

```txt
Input: 0qwer.
Output: true
```

## Solution

```py
import re

pattern = r'^\d\w\w\w\w\.$'
print(str(bool(re.search(pattern, input()))).lower())
```
