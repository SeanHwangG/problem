# [HR_s10-the-central-limit-theorem-2](https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2)

* en

  ```en
  The number of tickets purchased by each student for University X vs. Y football game follows a distribution
  that has a mean of u=2.4 and a standard deviation of δ=2.0.
  A few hours before the game starts, 100 eager students line up to purchase last-minute tickets.
  If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?
  ```

* tc

  ```tc
  250
  100
  2.4
  2.0
  ```

## Solution

* py

  ```py
  import math

  def cumulative(x, mean, sd):
    erf_val = math.erf((x-mean)/(sd * (2**.5)))
    return .5 * (1 + erf_val)

  mu, sigma, n = 2.4, 2.0, 100
  standard_error = sigma / (n ** .5)
  x_bar = 250 / float(n)
  print(f"{cumulative(x_bar, mu,standard_error):.4f}")
  ```
