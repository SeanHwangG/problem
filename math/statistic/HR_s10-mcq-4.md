# [HR_s10-mcq-4](https://www.hackerrank.com/challenges/s10-mcq-4)

* en

  ```en
  Suppose a family has 2 children, one of which is a boy
  What is the probability that both children are boys?
  ```

* tc

  ```tc
  Output: 1 / 3
  ```

## Solution

* py

  ```py
  from fractions import Fraction
  poss = ["BG", "BB", "GB", "GG"]
  print(f"Probability: {Fraction(sum(p == 'BB' for p in poss), sum('B' in p for p in poss))}")
  ```
