# [HR_s10-geometric-distribution-2](https://www.hackerrank.com/challenges/s10-geometric-distribution-2)

* en

  ```en
  Probability that machine produces a defective product is 1/3
  What is the probability that 1st defect is found during the first 5 inspections?
  ```

* tc

  ```tc
  Input:
  1 3
  5

  Output: 0.868
  ```

## Solution

* py

  ```py
  frac = list(map(int, input().split()))
  p = frac[0] / frac[1]
  n = int(input())
  q = 1 - p
  print(round(1 - q ** n,3))
  ```
