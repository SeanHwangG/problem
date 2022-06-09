# [HR_s10-standard-deviation](https://www.hackerrank.com/challenges/s10-standard-deviation)

* en

  ```en
  Print standard deviation of given array up to 1st decimal
  ```

* tc

  ```tc
  Input: 5
  10 40 30 50 20

  Output: 14.1
  ```

## Solution

* py

  ```py
  import statistics as stats

  N = int(input())
  X = list(map(int, input().split()))

  print(f"{stats.pstdev(X):.1f}")
  ```
