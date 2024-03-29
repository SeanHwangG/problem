# [LC_generate-random-point-in-a-circle](https://leetcode.com/problems/generate-random-point-in-a-circle)

* en

  ```en
  Print random point inside circle
  ```

* tc

  ```tc
  Input:
  ["Solution", "randPoint", "randPoint", "randPoint"]
  [[1.0, 0.0, 0.0], [], [], []]

  Output:
  [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
  ```

## Solution

* py

  ```py
  import math
  import random
  def __init__(self, radius, x_center, y_center):
    self.radius = radius
    self.x_center = x_center
    self.y_center = y_center
    random.seed()
  def randPoint(self):
    degree = random.uniform(0, 2 * math.pi)
    dist = (2 * random.uniform(0, self.radius ** 2 / 2.0)) ** (1/2.0)
    x = dist * math.cos(degree)
    y = dist * math.sin(degree)
    return [self.x_center + x, self.y_center + y]
  ```
