# [HR_valid-pan-format](https://www.hackerrank.com/challenges/valid-pan-format)

* en

  ```en
  <char>\<char>\<char>\<char>\<char>\<digit>\<digit>\<digit>\<digit>\<char>
  ```

* tc

  ```tc
  Input: 3
  ABCDS1234Y
  ABAB12345Y
  avCDS1234Y

  Output: YES
  NO
  NO
  ```

## Solution

* py

  ```py
  import re
  for i in range(int(input())):
    print("YES" if re.match(r'[A-Z]{5}[0-9]{4}[A-Z]{1}', input()) else "NO")
  ```
