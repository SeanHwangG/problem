# [HR_s10-normal-distribution-2](https://www.hackerrank.com/challenges/s10-normal-distribution-2)

```en
Grades for a exam taken by students have a mean of 70 and a STD of 10, find probabilities
Higher than 80, 60 / lower than 60
```

```txt
Input: 70 10

Output:
80
60
```

## Solution

* py

  ```py
  import math
  mean, std = 70, 10
  cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

  print(round((1 - cdf(80)) * 100, 2))
  print(round((1 - cdf(60)) * 100, 2))
  print(round((cdf(60)) * 100, 2))
  ```
