# [KT_isithalloween](https://open.kattis.com/problems/isithalloween)

* en

  ```en
  If input is OCT 31 or DEC 25 print 'yup' else print 'nope'
  ```

* tc

  ```tc
  Input: OCT 31
  Output: yup
  ```

## Solution

* py

  ```py
  s = input()
  print("yup" if s == 'OCT 31' or s == 'DEC 25' else "nope")
  ```
