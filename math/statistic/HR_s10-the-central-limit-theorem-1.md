# [HR_s10-the-central-limit-theorem-1](https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1)

* en

  ```en
  Elevator can transport a maximum of A pounds, B boxes must be transported via the elevator
  Box weight is normally distributed with a mean = C, STD=D
  What is the probability that all B boxes can be safely loaded into the freight elevator and transported
  ```

* tc

  ```tc
  Input: 9800
  49
  205
  15
  Output:
  0.0098
  ```

## Solution

* py

  ```py
  from math import erf
  sample, n_samples, mean, std = (int(input()) for _ in range(4))
  sample_mean, sample_std = n_samples * mean, (n_samples**.5) * std

  cdf = lambda x: .5 + .5 * erf((x - sample_mean) / 2 ** .5 / sample_std)
  print(round(cdf(sample), 4))
  ```

* r

  ```r
  input <- file('stdin','r')
  pounds <- as.numeric(readLines(input, n=1))
  n <- as.numeric(readLines(input, n=1))
  mean <- as.numeric(readLines(input, n=1))
  sd <- as.numeric(readLines(input, n=1))
  mean <- n*mean
  sd <- sd*sqrt(n)
  cat(format(round(pnorm(pounds, mean, sd),digits=4),nsmall=4))
  ```
