# [HR_split-number](https://www.hackerrank.com/challenges/split-number)

* en

  ```en
  There might either be a hyphen, or a space between the segments
  Country and local area codes can have 1-3 numerals each and the number section can have 4-10 numerals each
  ```

* tc

  ```tc
  Input:
  2
  1 877 2638277
  91-011-23413627

  Output:
  CountryCode=1,LocalAreaCode=877,Number=2638277
  CountryCode=91,LocalAreaCode=011,Number=23413627
  ```

## Solution

* py

  ```py
  import re
  for i in range(int(input())):
    a, b, c = (re.sub(r"[ -]", " ", input())).split()
    print(f"CountryCode={a},LocalAreaCode={b},Number={c}")
  ```
