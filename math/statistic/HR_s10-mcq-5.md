# [HR_s10-mcq-5](https://www.hackerrank.com/challenges/s10-mcq-5)

```en
You draw 2 cards from a standard-card deck 52 without replacing them
What is the probability that both cards are of the same suit?
```

```txt
Output: 4/17
```

## Solution

* py

  ```py
  from fractions import Fraction
  from itertools import combinations
  cards = [(t, n) for t in "HDCS" for n in range(1, 14)]
  combs, s = list(combinations(cards, 2)), 0
  for a, b in combs:
    if a[0] == b[0]:
      s += 1
  print(Fraction(s, len(combs)))
  ```
