# [LC_the-dining-philosophers](https://leetcode.com/problems/the-dining-philosophers)

5 silent philosophers sit at round table with bowls of spaghetti with Forks placed between each pair of adjacent philosophers
Design behaviour ST no philosopher will starve
Each can forever continue to alternate between eating and thinking
Assuming that no philosopher can know when others may want to eat or think

```txt
Input: n = 1
Output: [[4,2,1],[4,1,1],[0,1,1],[2,2,1],[2,1,1],[2,0,3],[2,1,2],[2,2,2],[4,0,3],[4,1,2],[0,2,1],[4,2,2],[3,2,1],
  [3,1,1],[0,0,3],[0,1,2],[0,2,2],[1,2,1],[1,1,1],[3,0,3],[3,1,2],[3,2,2],[1,0,3],[1,1,2],[1,2,2]]
```

## Solution

* py

  ```py
  from threading import Lock
  class DiningPhilosophers:

    def __init__(self):
      self.locks = [Lock() for _ in range(5)]

    def wantsToEat(self, philosopher: int,
            pickLeftFork: 'Callable[[], None]',
            pickRightFork: 'Callable[[], None]',
            eat: 'Callable[[], None]',
            putLeftFork: 'Callable[[], None]',
            putRightFork: 'Callable[[], None]') -> None:
      if philosopher != 0:
        first, second = philosopher, (philosopher + 1) % 5
      else:
        second, first = philosopher, (philosopher + 1) % 5
      with (self.locks[first], self.locks[second]):
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
  ```
