# [HR_capturing-non-capturing-groups](https://www.hackerrank.com/challenges/capturing-non-capturing-groups)

Should have or more consecutive repetitions of ok

```txt
Input: okokok! cya
Output: true
```

## Solution

* py

  ```py
  import re
  pattern = r'(ok){3,}'
  print(str(bool(re.search(pattern, input()))).lower())
  ```
