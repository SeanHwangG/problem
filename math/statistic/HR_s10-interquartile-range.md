# [HR_s10-interquartile-range](https://www.hackerrank.com/challenges/s10-interquartile-range)

* en

  ```en
  Given values and frequencies print quratile Q1-Q3 range
  ```

* tc

  ```tc
  Input:
  6
  6 12 8 10 20 16
  5 4 3 2 1 5

  Output: 9.0
  ```

## Solution

* py

  ```py
  import statistics as st
  n = int(input())
  X = list(map(int, input().split()))
  F = list(map(int, input().split()))

  S = list(sorted(X[i] for i in range(n) for _ in range(F[i])))

  n = len(S)
  n2 = int(n/2)
  print(round(float(st.median(S[-n2:])-st.median(S[:n2])),1))
  ```
