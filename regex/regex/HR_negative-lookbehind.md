# [HR_negative-lookbehind](https://www.hackerrank.com/challenges/negative-lookbehind)

* en

  ```en
  Match all the occurences of characters which are not immediately preceded by vowels
  ```

* tc

  ```tc
  Input: abru
  Output: Number of matches : 3   # abr
  ```

## Solution

* py

  ```py
  import re

  pattern = r"(?<![aeiouAEIOU])."
  match = re.findall(pattern, input)

  print("Number of matches :", len(match))
  ```
