# [HR_s10-mcq-3](https://www.hackerrank.com/challenges/s10-mcq-3)

* en

  ```en
  One ball is drawn from each of the 3 urns.
  4 red and 3 black / 5 red and 4 black / 4 red and 4 black
  What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?
  ```

* tc

  ```tc
  Output: 17/42
  ```

## Solution

* py

  ```py
  x = {"Red":4/7, "Black":3/7}
  y = {"Red":5/9, "Black":4/9}
  z = {"Red":4/8, "Black":4/8}

  first = x["Red"] * y["Red"] * z["Black"]
  second = x["Red"] * y["Black"] * z["Red"]
  third = x["Black"] * y["Red"] * z["Red"]

  print(first + second + third)
  ```
