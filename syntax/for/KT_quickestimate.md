# [KT_quickestimate](https://open.kattis.com/problems/quickestimate)

* en

  ```en

  ```

* kr

  ```kr
  첫줄에 n, 다음 n 줄의 문자가 주어질 때 문자의 길이를 각각 출력하라
  ```

* tc

  ```tc
  Input: 2
  ab
  a
  Output: 2
  1
  ```

## Solution

* py

 ```py
  n_line = int(input())
  for _ in range(n_line):
    x = input()
    print(len(x))
  ```
