# [HR_saying-hi](https://www.hackerrank.com/challenges/saying-hi)

First character must be the letter H or h
Second character must be the letter I or i
Third character must be a single space
Fourth character must not be the letter D or d

```txt
Input:
5
Hi Alex how are you doing
hI dave how are you doing
Good by Alex
hidden agenda
Alex greeted Martha by saying Hi Martha

Output: Hi Alex how are you doing
```

## Solution

```py
import re, sys
for s in filter(re.match(r"(?i:hi\s[^d])", sys.stdin)):
  print(s.strip())
```
