# [HR_capturing-non-capturing-groups](https://www.hackerrank.com/challenges/capturing-non-capturing-groups)

* en

  ```en
  Should have or more consecutive repetitions of ok
  ```

* tc

  ```tc
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
