# [KT_3dprinter](https://open.kattis.com/problems/3dprinter)

* en

  ```en
  Make 3d printer or prodcut using 3d printer
  What is min possible number of days needed to print at least 𝑛 statues?
  ```

* tc

  ```tc
  Input: 5
  Output: 4
  ```

## Solution

* py

  ```py
  from math import ceil, log
  line = int(input())
  print(int(ceil(log(line, 2) + 1)))
  ```
