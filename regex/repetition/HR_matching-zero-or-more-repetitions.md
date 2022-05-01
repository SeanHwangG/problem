# [HR_matching-zero-or-more-repetitions](https://www.hackerrank.com/challenges/matching-zero-or-more-repetitions)

Begin with 1 or 2 digits
After that, 3 or more letters (both lowercase and uppercase)
End with up to 3 symbol(s)

```txt
Input: 14
Output: true
```

## Solution

* py

  ```py
  import re
  pattern = r'^\d{1,2}[a-zA-Z]{3,}.{0,3}$'
  print(str(bool(re.search(pattern, input()))).lower())
  ```
