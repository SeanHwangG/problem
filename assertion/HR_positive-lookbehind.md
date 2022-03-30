# [HR_positive-lookbehind](https://www.hackerrank.com/challenges/positive-lookbehind)

Write a regex which can match all the occurences of digit which are immediately preceded by odd digit

```txt
Input: 123Go!
Output: 1
```

## Solution

```py
import re
Test_String = input()
pattern = r"(?<=[13579])\d"
match = re.findall(pattern, Test_String)

print("Number of matches :", len(match))
```
