# [HR_s10-mcq-2](https://www.hackerrank.com/challenges/s10-mcq-2)

* en

  ```en
  Two toss of six-sided dice, find probability that values rolled by each die will be different, two dice sum to 6
  ```

* tc

  ```tc
  Output: 1/9
  ```

## Solution

* py

  ```py
  from fractions import Fraction
  poss = 0

  for d1 in range(1, 7):
    for d2 in range(1, 7):
      if d1 != d2 and d1 + d2 == 6:
        poss += 1
        print(f"{d1} + {d2} = {d1 + d2}")

  print(f"Probability: {Fraction(poss, 36)}")
  ```
