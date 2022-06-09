# [HR_s10-geometric-distribution-1](https://www.hackerrank.com/challenges/s10-geometric-distribution-1)

* en

  ```en
  Probability that a machine produces a defective product is 1/3.
  What is the probability that the 1st defect is found during the 5th inspection?
  ```

* tc

  ```tc
  Input:
  1 3
  5

  Output: 0.066
  ```

## Solution

* py

  ```py
  probability = list(map(int, input().split()))
  p = probability[0] / probability[1]
  q, n = 1 - p, int(input())

  print(round(q ** (n - 1) * p, 3))
  ```
