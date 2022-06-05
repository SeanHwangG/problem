# [HR_matching-one-or-more-repititions](https://www.hackerrank.com/challenges/matching-one-or-more-repititions)

```en
Begin with  or more digits
After that, should have 1 or more uppercase letters
Should end with 1 or more lowercase letters
```

```txt
Input: 1Qa
Output: true
```

## Solution

* py

  ```py
  import re
  pattern = r'^\d+[A-Z]+[a-z]+$'
  print(str(bool(re.search(pattern, input()))).lower())
  ```
