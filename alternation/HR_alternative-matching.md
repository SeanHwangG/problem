# [HR_alternative-matching](https://www.hackerrank.com/challenges/alternative-matching)

Must start with Mr., Mrs., Ms., Dr. or Er.
Rest of string must contain only one or more English alphabetic letters (upper and lowercase)

```txt
Input: Mr.DOSHI
Output: true
```

## Solution

```py
import re
pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[A-Za-z]+$'  # Do not delete 'r'.

print(str(bool(re.search(pattern, input()))).lower())
```
