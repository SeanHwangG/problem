# [HR_s10-binomial-distribution-2](https://www.hackerrank.com/challenges/s10-binomial-distribution-2)

* en

  ```en
  Manufacturer of metal pistons finds that, on average, 12% of pistons are rejected
  What is the probability that a batch of 10 pistons will contain: No more than 2 rejects? / At least 2 rejects?
  ```

* tc

  ```tc
  Input: 12 10
  Output:
  0.891
  0.342
  ```

## Solution

* py

  ```py
  from math import comb

  def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

  p, n = map(int, input().split())
  print(round(sum([b(i, n, p / 100) for i in range(3)]), 3))
  print(round(sum([b(i, n, p / 100) for i in range(2, n+1)]), 3))
  ```
