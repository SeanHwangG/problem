# [HR_matching-specific-characters](https://www.hackerrank.com/challenges/matching-specific-characters)

* en

  ```en
  \must be of length: 6
  First character: 1, 2 or 3
  Second character: 1, 2 or 0
  Third character: x, s or 0
  Fourth character: 3, 0 , A or a
  Fifth character: x, s or u
  Sixth character: . or ,
  ```

* tc

  ```tc
  Input: 1203x.
  Output: true
  ```

## Solution

* py

  ```py
  import re
  pattern = r'^[123][120][xs0][30Aa][xsu][.,]$'
  print(str(bool(re.search(pattern, input()))).lower())
  ```
