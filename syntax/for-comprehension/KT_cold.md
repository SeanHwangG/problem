# [KT_cold](https://open.kattis.com/problems/cold)

* en

  ```en
  Print number of negative numbers
  ```

* kr

  ```kr
  음수의 개수를 구하라
  ```

* tc

  ```tc
  Input: 3
  5 -10 15
  Output: 1
  ```

## Solution

* py

  ```py
  input()
  print(len(n for n in map(int, input().split()) if n < 0))
  ```
