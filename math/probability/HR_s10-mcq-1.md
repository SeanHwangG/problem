# [HR_s10-mcq-1](https://www.hackerrank.com/challenges/s10-mcq-1)

* en

  ```en
  Two toss of fair six-sided dice, find the probability that their sum will be at most 9
  ```

* tc

  ```tc
  Output: 5/6
  ```

## Solution

* py

  ```py
  from fractions import Fraction
  poss = 0

  for d1 in range(1, 7):
    for d2 in range(1, 7):
      if (d1 + d2) <= 9:
        poss += 1
        print(f"{d1} + {d2} = {d1 + d2}")

  print(f"Probability: {Fraction(poss, 36)}")
  ```
