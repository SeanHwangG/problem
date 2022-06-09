# [KT_romans](https://open.kattis.com/problems/romans)

* en

  ```en
  One mile is 1000 * 5280 / 4854 pace, Print pace when given miles (decimal point is rounded off)
  ```

* kr

  ```kr
  1 마일은 1000 * 5280 / 4854 페이스이다. 마일이 주어졌을 때 페이스를 출력하라. (소수점은 반올림 한다)
  ```

* tc

  ```tc
  Input: 20.267
  Output: 22046
  ```

## Solution

* py

  ```py
  n = float(input())
  print(int(n * 5280000 / 4854 + 0.5))
  ```
