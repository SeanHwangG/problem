# [LC_asteroid-collision](https://leetcode.com/problems/asteroid-collision)

Find state of asteroids after all collisions. If 2 asteroids meet, smaller will explode
If both are same size, both will explode. Two asteroids moving in same direction will never meet

```txt
Input: asteroids = [5,10,-5]
Output: [5,10]

Input: asteroids = [10,2,-5]
Output: [10]
```

## Solution

```py
def asteroidCollision(self, asteroids):
  res = []
  for asteroid in asteroids:
    while len(res) and asteroid < 0 and res[-1] > 0:
      if res[-1] == -asteroid:
        res.pop()
        break
      elif res[-1] < -asteroid:
        res.pop()
        continue
      elif res[-1] > -asteroid:
        break
    else:
      res.append(asteroid)
  return res
```
