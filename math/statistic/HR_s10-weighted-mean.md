# [HR_s10-weighted-mean](https://www.hackerrank.com/challenges/s10-weighted-mean)

* en

  ```en
  Given values and weights, printed weighted mean
  ```

* tc

  ```tc
  Input: 5
  10 40 30 50 20
  1 2 3 4 5

  Output: 32.0
  ```

## Solution

* py

  ```py
  size = int(input())
  numbers = list(map(int, input().split()))
  weighted = list(map(int, input().split()))

  sum_items = 0
  for i in range(size):
    sum_items = sum_items + (numbers[i] * weighted[i])

  print(round(sum_items / sum(weighted), 1))
  ```
